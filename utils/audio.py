import gtts

def generate_audio(text: str, output_file: str):
    sound = gtts.gTTS(text, lang='en')
    sound.save(output_file)

if __name__ == "__main__":
    generate_audio("Hello, world!")