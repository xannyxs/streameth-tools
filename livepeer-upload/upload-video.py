import os
import sys
import mimetypes
import datetime
from os.path import join, dirname, basename, isfile, isdir
from LivePeerSDK_Python.LivePeerSDK import LivePeerSDK
from dotenv import load_dotenv


def upload_video(LivePeer: LivePeerSDK, video_path: str) -> None:
    """Uploads a video to LivePeer."""

    print(f"Uploading... {basename(video_path)}")

    assetUrl = LivePeer.createUploadUrl(basename(video_path))
    LivePeer.uploadContent(video_path, assetUrl['url'])


def upload_videos(LivePeer: LivePeerSDK, videos: list[str]) -> None:
    """Uploads a list of videos to LivePeer."""

    for video_path in videos:
        upload_video(LivePeer, video_path)


def get_video_names_from_directory(directory_path: str) -> list[str]:
    """Returns a list of video file paths in the provided directory."""

    video_paths = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if is_video(file_path):
                video_paths.append(file_path)

    return video_paths


def is_video(file_path: str) -> bool:
    """Determines if a file is a video."""

    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type is not None and mime_type.startswith('video')


def get_video() -> list[str]:
    """Retrieves the video(s) from the provided path."""

    input_path = sys.argv[1]

    if isfile(input_path):
        if is_video(input_path):
            video_name = basename(input_path)
            print(f"Video name: {video_name}")
            return [input_path]
        else:
            print("The provided file is not a video.")
            sys.exit(1)
    elif isdir(input_path):
        video_paths = get_video_names_from_directory(input_path)
        if video_paths:
            print("Videos in directory:")
            for video_path in video_paths:
                print(basename(video_path))
            return video_paths
        else:
            print("No video files found in the provided directory.")
            sys.exit(1)
    else:
        print("The provided path is not a valid file or directory.")
        sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 upload-video.py /path/to/directory_or_video")
        sys.exit(1)

    videos = get_video()
    if videos:
        LivePeer = LivePeerSDK(os.environ.get("LIVEPEER_API_KEY"))
        upload_videos(LivePeer, videos)


if __name__ == '__main__':
    dotenv_path = join(dirname(__file__), '../.env.local')
    load_dotenv(dotenv_path)

    main()
