from openai import OpenAI
import os

def user_input():

    user_input = input("What do you want to learn? ")

    print(f'I want to learn about: {user_input}')

    return user_input

def prompt_ai(prompt):

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a language instructor."},
            {"role": "system", "content": "You are teaching the following language: French."},
            {"role": "system", "content": "The user language level is (using CEFR standards A1 to C2): B2."},
            {"role": "system", "content": "Generate a short story about the following user topic."},

            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(completion.choices[0].message)

def check_api_key():
    api_key = os.getenv("OPENAI_API_KEY")


    if api_key:
        print("API Key loaded successfully!")
    else:
        print("API Key not found. Please set the environment variable.")