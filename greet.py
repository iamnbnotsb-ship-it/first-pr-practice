import sys


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    name = name.strip()
    if not name:
        return "Hello, world!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet(sys.argv[1] if len(sys.argv) > 1 else ""))
