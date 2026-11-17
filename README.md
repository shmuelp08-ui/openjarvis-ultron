# ULTRON
Android-first personal AI built on the actual OpenJarvis framework.

This repository contains the upstream OpenJarvis source tree, adapted and rebranded for ULTRON, plus the ULTRON API/backend integration.

## Upstream foundation
The framework source is imported from https://github.com/open-jarvis/OpenJarvis.
Original copyright and attribution notices are retained. See LICENSE and NOTICE.

## ULTRON provider configuration
Gemini is the primary hosted model provider; Groq is the fallback. Configure GEMINI_API_KEY and GROQ_API_KEY in your environment. Never commit real secrets.

## Development
The upstream framework requires Python 3.11–3.13. Install the project and optional extras as documented in the upstream package configuration. The ULTRON API lives in ultron_server/.
