"""ULTRON HTTP API."""
from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .memory import add_message, clear_messages, get_messages
from .providers import ProviderError, ProviderRouter

app = FastAPI(title="ULTRON API", version="0.1.0")
providers = ProviderRouter()


class ChatRequest(BaseModel):
    conversation_id: str = Field(default="main", min_length=1, max_length=128)
    message: str = Field(min_length=1, max_length=20000)


class ChatResponse(BaseModel):
    conversation_id: str
    response: str
    provider: str
    model: str


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "assistant": "ULTRON", "providers": providers.status()}


@app.post("/v1/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    history = get_messages(request.conversation_id, limit=30)
    messages = [{"role": item["role"], "content": item["content"]} for item in history]
    messages.append({"role": "user", "content": request.message})
    try:
        reply = await providers.complete(messages)
    except ProviderError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    add_message(request.conversation_id, "user", request.message)
    add_message(request.conversation_id, "assistant", reply.text)
    return ChatResponse(conversation_id=request.conversation_id, response=reply.text,
                        provider=reply.provider, model=reply.model)


@app.get("/v1/memory/{conversation_id}")
async def memory(conversation_id: str) -> dict:
    return {"conversation_id": conversation_id, "messages": get_messages(conversation_id)}


@app.delete("/v1/memory/{conversation_id}")
async def delete_memory(conversation_id: str) -> dict:
    clear_messages(conversation_id)
    return {"conversation_id": conversation_id, "cleared": True}
