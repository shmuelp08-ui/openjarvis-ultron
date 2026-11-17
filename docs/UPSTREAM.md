# OpenJarvis integration notes

ULTRON is intended to use the actual OpenJarvis framework as its agent/runtime foundation, not merely imitate its interface.

Upstream repository: https://github.com/open-jarvis/OpenJarvis  
Upstream license: Apache License 2.0 (the upstream LICENSE is preserved in this repository).

## Integration boundary

The upstream project is a large Python framework with inference engines, agents, tools, memory, scheduling, evaluations, and a desktop/web interface. ULTRON's Android client should be a separate mobile control surface that talks to a secured ULTRON API. Device-only actions (notifications, accessibility, microphone, WhatsApp UI automation) belong in Android and must use user-granted platform permissions.

The first API scaffold in this repository provides Gemini-first/Groq-fallback chat and SQLite conversation history. It is not yet a vendored copy of the OpenJarvis source tree. The next integration stage is to vendor or install a pinned upstream revision, map its agent and memory interfaces behind the ULTRON API, and add parity tests before describing those capabilities as implemented.

Do not remove upstream copyright/license notices when importing or adapting upstream files. Mark modified upstream files as modified, as required by Apache-2.0.
