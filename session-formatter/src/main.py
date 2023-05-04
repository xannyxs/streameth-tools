import sys
import json
import subprocess
from typing import Any


def open_session(session_path: str) -> Any:
    with open(session_path) as file:
        data = json.load(file)

    return data


def main() -> None:
    json_file = open_session(sys.argv[1])

    if 'video' in json_file:
        print('Summarizing video...')
        subprocess.run(['python3', './summarize-video_to_text/src/main.py', json_file['video'], 'test'])
    else:
        print('Video does not exist in file')
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Need an argument to a JSON file')
        sys.exit(1)

    main()
