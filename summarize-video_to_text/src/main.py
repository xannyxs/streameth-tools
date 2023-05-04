import argparse
import os
import subprocess
import sys
import whisper
import openai
from os.path import dirname, join
from dotenv import load_dotenv


def process_text_file(transcribed_text: str) -> str:
    content = transcribed_text.replace('um', '').replace('uh', '').replace(',', '').replace('  ', ' ')

    words = content.split()
    word_count = len(words)

    if word_count > 1700:
        print('Content too long, will trim file')
        words = words[:1700]
        content = ' '.join(words)

    return content


def summarize_text(input_text: str, output_file: str) -> None:
    openai.api_key = os.environ.get('CHATGPT_API_KEY')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Summarize this for a description for a video:\n\n{input_text}"}
        ],
        temperature=0.4,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    summary = response.choices[0].message["content"].strip()
    if os.path.exists(output_file):
        with open(output_file, 'w') as file:
            file.write(summary)
    else:
        with open(output_file, 'x') as file:
            file.write(summary)


def download_m3u8_video_as_wav(m3u8_url: str, output_name: str) -> None:
    command = [
        "ffmpeg",
        "-i", m3u8_url,
        "-vn",
        "-c:a", "pcm_s16le",
        "-ar", "44100",
        "-ac", "2",
        f'{output_name}.wav'
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Successfully downloaded and converted audio from {m3u8_url} to {output_name}.wav")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while downloading and converting audio from {m3u8_url} to {output_name}.wav: {e}")


def convert_speech_to_text(input_wav: str) -> str:
    model = whisper.load_model("base")
    result = model.transcribe(input_wav)
    text = result["text"]

    print(f"Successfully saved speech-to-text result")
    return text


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download audio from an M3U8 URL, convert it to WAV, transcribe it, trim, and summarize")
    parser.add_argument("m3u8_url", help="URL of the M3U8 file")
    parser.add_argument("output_name", help="Path to the output WAV file")

    args = parser.parse_args()

    download_m3u8_video_as_wav(args.m3u8_url, args.output_name)
    transcribed_text = convert_speech_to_text(f"{args.output_name}.wav")
    shortend_text = process_text_file(transcribed_text)
    summarize_text(shortend_text, f'{args.output_name}.txt')


if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '../../.env.local')
    load_dotenv(dotenv_path)

    main()
