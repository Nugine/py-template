from pathlib import Path
import sys
import re
import os

IGNORED_ENTRIES = [".cache", ".venv", "uv.lock", "__pycache__", ".git"]


def iter_all_files(path: Path):
    for entry in path.iterdir():
        if entry.name in IGNORED_ENTRIES:
            continue

        if entry.is_file():
            yield entry
        elif entry.is_dir():
            yield from iter_all_files(entry)


def replace_in_file(path, project_name):
    print(path)
    with open(path, "r") as f:
        content = f.read()

    pairs = [
        (r"(?<!Nugine/)py-template", project_name),
        (r"(?<!Nugine/)py_template", project_name.replace("-", "_")),
    ]

    for regex, string in pairs:
        content = re.sub(regex, string, content)

    with open(path, "w") as f:
        f.write(content)


if __name__ == "__main__":
    project_name = sys.argv[1]

    os.rename("src/py_template", f"src/{project_name.replace('-', '_')}")

    for file in iter_all_files(Path.cwd()):
        replace_in_file(file, project_name)

    os.system("uv sync")

    print("Done!")
