def handle_message(message: str) -> str:
    parts = message.strip().split()

    if not parts:
        return "ERROR empty message"

    command = parts[0].upper()

    if command == "PING":
        return "PONG"

    if command == "ECHO":
        # TODO: return the text after ECHO
        return ""

    if command == "UPPER":
        # TODO: convert the remaining text to uppercase
        return ""

    if command == "ADD":
        # TODO: add two integers like: ADD 1 2
        return "0"

    return "ERROR unknown command"
