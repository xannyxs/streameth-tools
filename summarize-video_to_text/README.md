# Video Summary Generator

This script downloads audio from an M3U8 URL, converts it to WAV, transcribes the speech to text, trims the text, and summarizes it using ChatGPT.

## Usage

```
python3 main.py <m3u8_url> <output_name>
```

`<m3u8_url>` is the URL of the M3U8 file, and `<output_name>` is the desired name for the output WAV file.

## Description

The script performs the following steps:

1. Downloads audio from the provided M3U8 URL and converts it to a WAV file.
2. Transcribes the audio to text using the `whisper` library.
3. Trims and processes the transcribed text.
4. Summarizes the processed text using ChatGPT.

The summarized text is saved to a file with the same name as the output WAV file but with a `.txt` extension.

## Example

To download audio from an M3U8 URL, convert it to WAV, transcribe it, trim, and summarize the text:

```
python3 main.py https://example.com/video.m3u8 output
```

This command will generate two files: `output.wav` and `output.txt`. The `output.wav` file contains the converted audio, while the `output.txt` file contains the summarized text.
