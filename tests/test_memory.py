from ultron_server.memory import add_message, clear_messages, get_messages


def test_memory_round_trip(tmp_path, monkeypatch):
    monkeypatch.setenv("ULTRON_DB_PATH", str(tmp_path / "test.sqlite3"))
    add_message("test", "user", "hello")
    rows = get_messages("test")
    assert len(rows) == 1
    assert rows[0]["role"] == "user"
    assert rows[0]["content"] == "hello"
    clear_messages("test")
    assert get_messages("test") == []
