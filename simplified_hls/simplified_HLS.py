import subprocess
from pathlib import Path
from typing import Union


def process_videos(input_dir: Union[str, Path]) -> None:
    input_dir = Path(input_dir)
    output_dir = input_dir
    files = list(input_dir.glob('**/*.mp4'))

    for file in files:
        file_no_ext = file.stem
        output_subdir = output_dir / file_no_ext
        output_subdir.mkdir(parents=True, exist_ok=True)

        print(file)
        print(output_subdir)
        print(file_no_ext)

        command = [
            "ffmpeg",
            "-i", str(file),
            "-vf", "scale=w=640:h=360",
            "-c:v:0", "libx264", "-b:v:0", "1000k", "-preset:v:0", "fast",
            "-c:a:0", "aac", "-b:a:0", "96k",
            "-vf", "scale=w=1280:h=720",
            "-c:v:1", "libx264", "-b:v:1", "3000k", "-preset:v:1", "fast",
            "-c:a:1", "aac", "-b:a:1", "96k",
            "-vf", "scale=w=1920:h=1080",
            "-c:v:2", "libx264", "-b:v:2", "5000k", "-preset:v:2", "fast",
            "-c:a:2", "aac", "-b:a:2", "96k",
            "-map", "0:v:0", "-map", "0:a", "-map", "0:v:0", "-map", "0:a", "-map", "0:v:0", "-map", "0:a",
            "-var_stream_map", "v:0,a:0 v:1,a:1 v:2,a:2",
            "-f", "hls",
            "-hls_time", "10",
            "-hls_list_size", "0",
            "-hls_allow_cache", "1",
            "-hls_flags", "single_file",
            "-master_pl_name", "master.m3u8",
            f"{output_subdir}/output_%v.m3u8"
        ]

        subprocess.run(command, check=True)
        sys.exit(1)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python script_name.py <input_directory>")
    else:
        input_dir = sys.argv[1]
        process_videos(input_dir)


