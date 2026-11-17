# ULTRON

ULTRON combines the OpenJarvis assistant framework with the original ULTRON Android application.

## Source layout

- `android/` — the original native Android/Kotlin ULTRON app, copied from the separate ULTRON Android repository.
- `src/openjarvis/` — the actual OpenJarvis Python framework and its agent, memory, tool, and provider systems.
- `rust/` — the upstream Rust components.
- `frontend/` and `desktop/` — upstream frontend and desktop application source.

## Provenance

- `UPSTREAM_COMMIT` records the exact OpenJarvis revision imported.
- `ULTRON_ANDROID_COMMIT` records the exact original Android app revision copied into `android/`.
- OpenJarvis license and attribution files are retained. The original Android repository remains separate and unchanged.

## Important

Importing source code does not by itself prove that every feature builds or works on a device. Android and framework integration still needs to be built, tested, and wired together.
