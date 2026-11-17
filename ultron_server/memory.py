"""Small local SQLite conversation store."""
from __future__ import annotations

import os
import sqlite3
from pathlib import Path
from typing import Any


def _connect() -> sqlite3.Connection:
    db_path = Path(os.getenv("ULTRON_DB_PATH", "./data/ultron.sqlite3"))
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("""CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conversation_id TEXT NOT NULL,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    return conn


def add_message(conversation_id: str, role: str, content: str) -> None:
    with _connect() as conn:
        conn.execute("INSERT INTO messages (conversation_id, role, content) VALUES (?, ?, ?)",
                     (conversation_id, role, content))


def get_messages(conversation_id: str, limit: int = 40) -> list[dict[str, Any]]:
    with _connect() as conn:
        rows = conn.execute(
            "SELECT role, content, created_at FROM messages WHERE conversation_id=? ORDER BY id DESC LIMIT ?",
            (conversation_id, limit),
        ).fetchall()
    return [{"role": r[0], "content": r[1], "created_at": r[2]} for r in reversed(rows)]


def clear_messages(conversation_id: str) -> None:
    with _connect() as conn:
        conn.execute("DELETE FROM messages WHERE conversation_id=?", (conversation_id,))
