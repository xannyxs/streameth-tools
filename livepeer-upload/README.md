# LivePeer Video Uploader

This script uploads videos to the LivePeer platform, either individually or in bulk from a directory.

## Usage

```
python3 upload-video.py /path/to/directory_or_video
```

Provide the path to either a single video file or a directory containing video files.

## Description

The script performs the following steps:

1. Determines if the provided path is a single video file or a directory.
2. If it's a video file, the script uploads it to LivePeer.
3. If it's a directory, the script uploads all video files within the directory to LivePeer.

## Example

To upload a single video:

```
python3 upload-video.py /path/to/video.mp4
```

To upload all videos within a directory:

```
python3 upload-video.py /path/to/directory
```
