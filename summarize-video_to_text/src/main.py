import argparse
import subprocess
import whisper


def download_m3u8_video_as_wav(m3u8_url: str, output_wav: str) -> None:
    command = [
        "ffmpeg",
        "-i", m3u8_url,
        "-vn",
        "-c:a", "pcm_s16le",
        "-ar", "44100",
        "-ac", "2",
        output_wav
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Successfully downloaded and converted audio from {m3u8_url} to {output_wav}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while downloading and converting audio from {m3u8_url} to {output_wav}: {e}")


def convert_speech_to_text(output_wav: str) -> None:
    model = whisper.load_model("base")
    result = model.transcribe(output_wav)
    text = result["text"]

    with open("output.txt", 'w') as file:
        file.write(text)

    print(f"Successfully saved speech-to-text result")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download audio from an M3U8 URL and save it as a WAV file using ffmpeg")
    parser.add_argument("m3u8_url", help="URL of the M3U8 file")
    parser.add_argument("output_wav", help="Path to the output WAV file")

    args = parser.parse_args()

    download_m3u8_video_as_wav(args.m3u8_url, args.output_wav)
    convert_speech_to_text(args.output_wav)


if __name__ == "__main__":
    main()
