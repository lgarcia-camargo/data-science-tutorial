import json
import openai



with open('openai_keys.json', 'r') as f:
    keys = json.load(f)

openai.api_key = keys['bearer_key']

BASE_MODEL = 'text-davinci-003'
FINE_TUNED_MODEL = 'davinci:ft-research-2023-03-30-02-29-33'


def get_response(name, x, model=BASE_MODEL, temp=0):
    #function to request and return tet from model
    prompt = f'You are an interviewer of {name}. Say something about what {name} told you and ask a question furthering the conversation with the goal being to learn about the person\'s life (family, intersts, work, childhood, etc.). This is what {name} said: {x}'
    response = openai.Completion.create(
        engine = model,
        prompt = prompt,
        max_tokens = 50,
        temperature = temp,
        n = 1
    )
    
    return response['choices'][0]['text']


name = input('Hello, what is your name?\n')
p = input(f'Hello {name}, I am Gina and I will be interviewing you about your life. What have you been up to today?\n')
while p != 'exit':
    response = get_response(name, p)
    p = input(response+'\n')
