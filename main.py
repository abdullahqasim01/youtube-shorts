from utils import audio, subtitles, video, script, upload
import os
import time

def main():
    #generate the script

    print("generating script")
    script_text = script.generate_script("tell me a nostalgia fact about tv for 30 second youtube shorts")
    print("script generated")

    #generate the audio
    print("generating audio")
    audio.generate_audio(script_text, "audio.mp3")
    print("audio generated")
    #generate the subtitles

    print("generating subtitles")
    subtitles.generate_subtitles("audio.mp3", "subtitles.srt")
    print("subtitles generated")
    #generate the video

    print("generating video")
    video.generate_video("video.mp4", "audio.mp3", "subtitles.srt", "output.mp4")
    print("video generated")


    #upload the video
    print("uploading video")
    video_data = {
        "file": "output.mp4",
        "title": "test # 1",
        "description": "#shorts \n none",
        "keywords":"no",
        "privacyStatus":"public"
    }
    upload.upload_video(video_data)
    print("video uploaded")

    print("cleaning up")
    os.remove("audio.mp3")
    os.remove("subtitles.srt")
    os.remove("output_temp.mp4")
    os.remove("output.mp4")
    print("done")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(60*60*24)