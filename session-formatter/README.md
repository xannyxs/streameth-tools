# Video Description Generator

This script generates short video descriptions using ChatGPT and saves them in the corresponding JSON files. It takes a JSON file or a directory containing JSON files as input.

## Usage

```
python3 main.py <input_path>
```

`<input_path>` can be either a JSON file or a directory containing JSON files.

## Description

The script first checks if the video exists in the JSON data. If not, it skips processing. If a `gpt-description` is already present, the script does not generate a new description.

For each valid video, the script creates a temporary directory and generates a summary using the `summarize-video_to_text/src/main.py` script. The generated summary is then added to the JSON data as a `gpt_description` field, and the updated JSON data is saved back to the file.

## Example

To generate video descriptions for a single JSON file:

```
python3 main.py example.json
```

To generate video descriptions for all JSON files in a directory:

```
python3 main.py json_files_directory/
```
