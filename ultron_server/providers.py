"""LLM provider routing: Gemini primary, Groq fallback."""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class ProviderReply:
    text: str
    provider: str
    model: str


class ProviderError(RuntimeError):
    pass


class ProviderRouter:
    def __init__(self) -> None:
        self.gemini_key = os.getenv("GEMINI_API_KEY", "").strip()
        self.gemini_model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        self.groq_key = os.getenv("GROQ_API_KEY", "").strip()
        self.groq_model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

    def status(self) -> dict[str, bool]:
        return {"gemini_configured": bool(self.gemini_key), "groq_configured": bool(self.groq_key)}

    async def complete(self, messages: list[dict[str, str]]) -> ProviderReply:
        failures: list[str] = []
        if self.gemini_key:
            try:
                from google import genai
                from google.genai import types
                client = genai.Client(api_key=self.gemini_key)
                prompt = "\n".join(f"{m['role']}: {m['content']}" for m in messages)
                response = await client.aio.models.generate_content(
                    model=self.gemini_model,
                    contents=prompt,
                    config=types.GenerateContentConfig(temperature=0.7),
                )
                if response.text:
                    return ProviderReply(response.text, "gemini", self.gemini_model)
                failures.append("Gemini returned an empty response")
            except Exception as exc:  # provider failures trigger fallback
                failures.append(f"Gemini: {type(exc).__name__}: {exc}")
        else:
            failures.append("Gemini API key is not configured")

        if self.groq_key:
            try:
                from groq import AsyncGroq
                client = AsyncGroq(api_key=self.groq_key)
                response = await client.chat.completions.create(
                    model=self.groq_model,
                    messages=messages,
                    temperature=0.7,
                )
                answer = response.choices[0].message.content or ""
                if answer:
                    return ProviderReply(answer, "groq", self.groq_model)
                failures.append("Groq returned an empty response")
            except Exception as exc:
                failures.append(f"Groq: {type(exc).__name__}: {exc}")
        else:
            failures.append("Groq API key is not configured")
        raise ProviderError("No provider could answer. " + " | ".join(failures))
