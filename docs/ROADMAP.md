# ULTRON roadmap

## Foundation committed
- [x] New independent GitHub repository
- [x] ULTRON API scaffold
- [x] Gemini-first provider routing
- [x] Groq fallback
- [x] SQLite conversation history
- [x] API health and chat endpoints
- [x] Upstream attribution and Apache-2.0 license

## Next engineering stages
- [ ] Import/pin the actual OpenJarvis framework source and preserve its license notices.
- [ ] Replace the starter provider/router path with OpenJarvis agent, inference, and memory interfaces.
- [ ] Add authentication and TLS guidance before exposing the API beyond localhost.
- [ ] Add Android app (Kotlin + Jetpack Compose), secure API-key onboarding, and server connection settings.
- [ ] Add streaming chat and cancellation.
- [ ] Add voice input/output with a configurable speech provider.
- [ ] Add Android notification, calendar, and app-intent integrations using explicit permissions.
- [ ] Add WhatsApp handoff/interaction only through supported Android intents and user-authorized accessibility workflows.
- [ ] Add integration tests, CI, release signing, and installable APK workflow.

A roadmap item is not considered implemented until code and tests exist.
