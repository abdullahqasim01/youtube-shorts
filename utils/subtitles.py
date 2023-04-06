import whisper
from typing import Iterator, TextIO

def format_timestamp(seconds: float, always_include_hours: bool = False):
    assert seconds >= 0, "non-negative timestamp expected"
    milliseconds = round(seconds * 1000.0)

    hours = milliseconds // 3_600_000
    milliseconds -= hours * 3_600_000

    minutes = milliseconds // 60_000
    milliseconds -= minutes * 60_000

    seconds = milliseconds // 1_000
    milliseconds -= seconds * 1_000

    hours_marker = f"{hours}:" if always_include_hours or hours > 0 else ""
    return f"{hours_marker}{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def write_srt(transcript: Iterator[dict], file: TextIO):
    for i, segment in enumerate(transcript, start=1):
        print(
            f"{i}\n"
            f"{format_timestamp(segment['start'], always_include_hours=True)} --> "
            f"{format_timestamp(segment['end'], always_include_hours=True)}\n"
            f"{segment['text'].strip().replace('-->', '->')}\n",
            file=file,
            flush=True,
        )

def load(model_name: str = "small"):
    return whisper.load_model(model_name)

def generate_subtitles(audio: str, srt_path: str, model_name: str = "small"):
    
    model = whisper.load_model(model_name)

    result = model.transcribe(audio, fp16=False)
    
    with open(srt_path, "w", encoding="utf-8") as srt:
        write_srt(result["segments"], file=srt)


if __name__ == '__main__':
    generate_subtitles("C:\\Users\\User\\Desktop\\yoututbe-shorts\\utils\\data\\audio.mp3", "subtitles.srt")