# ULTRON

**Personal AI assistant · Android-first · Gemini primary · Groq fallback**

ULTRON is a personal assistant project built around the open-source [OpenJarvis](https://github.com/open-jarvis/OpenJarvis) agent framework. This repository is the ULTRON application layer and integration workspace; upstream OpenJarvis remains separately credited and licensed.

## Current architecture

- **Android client:** native Android app (Kotlin/Compose) planned for voice, chat, permissions, and device actions.
- **Assistant API:** Python/FastAPI service in `ultron_server/`.
- **Primary brain:** Google Gemini, configured with `GEMINI_API_KEY`.
- **Fallback brain:** Groq, configured with `GROQ_API_KEY`; used when Gemini is unavailable or fails.
- **Memory:** local SQLite conversation memory (per installation).
- **Secrets:** environment variables on the server; never commit API keys.

## Run the API locally

Python 3.11+:

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -e .
cp .env.example .env
# Add GEMINI_API_KEY and GROQ_API_KEY to .env
uvicorn ultron_server.app:app --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000/health`.

## API

- `GET /health` — provider readiness.
- `POST /v1/chat` — send a message; Gemini is tried first, Groq is the fallback.
- `GET /v1/memory/{conversation_id}` — read saved conversation history.
- `DELETE /v1/memory/{conversation_id}` — clear a conversation's saved history.

Example:

```json
{ "conversation_id": "main", "message": "Hey ULTRON" }
```

## Android integration status

The backend is the first deliverable. Android voice capture, wake-word/continuous-conversation policy, text-to-speech, accessibility actions, and WhatsApp interaction must be implemented and tested in the Android client with explicit user-granted permissions. The API does not claim to control a locked phone or send WhatsApp messages by itself.

## Upstream attribution

The upstream OpenJarvis project is developed by its original contributors. Its Apache-2.0 license is retained in this repository. This ULTRON integration is a separate project and is not endorsed by the upstream authors.

- Upstream: https://github.com/open-jarvis/OpenJarvis
- Upstream documentation: https://open-jarvis.github.io/OpenJarvis/
- License: Apache-2.0 (see `LICENSE`)
