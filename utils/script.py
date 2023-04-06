import openai

openai.api_key = ""

def generate_script(prompt: str):
    response = openai.Completion.create(engine="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0.7,
                                        max_tokens=200) 
    return response['choices'][0]['text']

if __name__ == "__main__":
    print(generate_script("tell me a nostalgia fact for 30 second youtube shorts"))