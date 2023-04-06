import subprocess

def generate_video(video_input: str, audio_input: str, subtitle_input: str, video_output: str):
    command = f"ffmpeg -i {video_input} -i {audio_input} -c:v libx264 -c:a copy -map 0:v -map 1:a -shortest -aspect 9:16 -v error output_temp.mp4"
    subprocess.call(command, shell=True)
    command = f"ffmpeg -i output_temp.mp4 -vf \"subtitles={subtitle_input}:force_style='FontName=Arial,FontSize=24'\" -c:a copy -v error {video_output}"
    subprocess.call(command, shell=True)

if __name__ == "__main__":
    generate_video("video.mp4", "output.mp3", "output.srt", "output_final.mp4")