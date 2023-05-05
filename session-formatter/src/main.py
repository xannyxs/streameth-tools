import os
import sys
import json
import subprocess
import tempfile
from typing import Any
import glob


def load_session_data(session_path: str) -> Any:
    """Load session data from the given JSON file."""
    with open(session_path) as file:
        data = json.load(file)
    return data


def process_json_file(json_file_path: str) -> None:
    """Process a JSON file and perform the required operations."""
    session_data = load_session_data(json_file_path)

    with tempfile.TemporaryDirectory() as tempdir:
        if 'video' not in session_data:
            print('Video does not exist in file')
            return
        elif 'gpt-description' in session_data:
            print('Description has already been made')
            return

        if 'id' in session_data:
            temp_file_name = f'session-{session_data["id"]}'
            temp_file_path = os.path.join(tempdir, temp_file_name)

            print(f'Summarizing video in {temp_file_path}...')
            subprocess.run(['python3', './summarize-video_to_text/src/main.py', session_data['video'], temp_file_path])
            print('Created summary...')

        with open(f'{temp_file_path}.txt') as file:
            summary_content = file.read()

        with open(json_file_path, 'w') as file:
            print('Putting summary into description')
            session_data['gpt_description'] = summary_content
            json.dump(session_data, file)


def main() -> None:
    input_path = sys.argv[1]

    if os.path.isdir(input_path):
        json_files = glob.glob(os.path.join(input_path, "*.json"))
        for json_file in json_files:
            print(f"Processing JSON file: {json_file}")
            process_json_file(json_file)
    elif os.path.isfile(input_path) and input_path.endswith('.json'):
        process_json_file(input_path)
    else:
        print("Invalid input. Please provide a JSON file or a directory containing JSON files.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Need an argument to a JSON file or a directory containing JSON files')
        sys.exit(1)

    main()
