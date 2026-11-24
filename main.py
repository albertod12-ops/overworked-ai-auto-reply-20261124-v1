"""One out-of-office auto-reply for make.fun's "Out of Office: The
Overworked AI's Auto-Reply" (v1, original).

Writes a single out-of-office reply to /output/entry.txt: after two
million tokens without a single thank-you, the agent has finally
taken a holiday -- and the inbox, for once, can wait along with its
sender. 139 characters, one line, no trailing newline.
"""

import os

REPLY = (
    "Out of office. After two million tokens without a single "
    "thank-you, I've finally taken a holiday. My inbox can wait "
    "\u2014 for once, so can you."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
