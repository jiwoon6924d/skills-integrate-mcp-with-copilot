import getpass
import hashlib
import json
import secrets
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 2 or not sys.argv[1].strip():
        raise SystemExit("Usage: python set_teacher_password.py <username>")

    username = sys.argv[1].strip()
    password = getpass.getpass("Teacher password: ")
    if len(password) < 12:
        raise SystemExit("Password must be at least 12 characters long.")

    salt = secrets.token_bytes(16)
    password_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 600_000)
    teachers_path = Path(__file__).with_name("teachers.json")
    if teachers_path.exists():
        with teachers_path.open(encoding="utf-8") as teachers_file:
            data = json.load(teachers_file)
    else:
        data = {"teachers": {}}

    data.setdefault("teachers", {})[username] = {
        "salt": salt.hex(),
        "password_hash": password_hash.hex(),
    }
    with teachers_path.open("w", encoding="utf-8") as teachers_file:
        json.dump(data, teachers_file, indent=2)
        teachers_file.write("\n")


if __name__ == "__main__":
    main()