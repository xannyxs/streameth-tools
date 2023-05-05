# streameth-pytools

This repository contains a set of scripts for processing and uploading videos, converting speech to text, and summarizing text using GPT-3.5. This is specificly made for StreamETH, but you can ofcourse use it yourself

## Scripts

1. **Video Metadata Processor**: Processes JSON files containing video metadata and adds an AI-generated summary based on the video's content.

2. **Speech to Text and Summarizer**: Downloads audio from an M3U8 URL, converts it to WAV, transcribes it, trims the transcript, and summarizes the text using GPT-3.5.

3. **LivePeer Video Uploader**: Uploads videos to the LivePeer platform, either individually or in bulk from a directory.

## Usage

Each script has a specific usage instruction:

- **Video Metadata Processor**: `python3 video_metadata_processor.py /path/to/json_file_or_directory`
- **Speech to Text and Summarizer**: `python3 speech_to_text_and_summarizer.py m3u8_url output_name`
- **LivePeer Video Uploader**: `python3 upload-video.py /path/to/directory_or_video`

Please refer to the individual script READMEs for more details on their respective functionalities and example usage.

Ensure you have the required dependencies installed and the appropriate API keys set in your environment variables or `.env.local` file.
