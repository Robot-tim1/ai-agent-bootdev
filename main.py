import os
import argparse

from openai import OpenAI
from dotenv import load_dotenv
from systemprompts.prompts import system_prompt

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": args.prompt,},
        ]
    response = generate_content(messages)
    if response.usage is None:
            raise RuntimeError

    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    print("Response:")
    print(response.choices[0].message.content)

def generate_content(messages):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )

    return response

if __name__ == "__main__":
    main()
