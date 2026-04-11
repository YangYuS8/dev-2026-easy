from protocol import handle_message


def test_ping() -> None:
    assert handle_message("PING") == "PONG"


def test_echo() -> None:
    assert handle_message("ECHO hello") == "hello"


def test_upper() -> None:
    assert handle_message("UPPER hello world") == "HELLO WORLD"


def test_add() -> None:
    assert handle_message("ADD 2 3") == "5"


def test_unknown_command() -> None:
    assert handle_message("NOPE") == "ERROR unknown command"


def test_empty_message() -> None:
    assert handle_message("") == "ERROR empty message"


def test_add_invalid_args() -> None:
    assert handle_message("ADD 1") == "ERROR invalid arguments"
