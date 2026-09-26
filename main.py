import os
import argparse
import json

from openai import OpenAI
from dotenv import load_dotenv
from prompts import system_prompt

from functions.get_files_info import *
from functions.run_python_file import *
from functions.write_file import *
from functions.get_file_content import *

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
    available_functions = [
        schema_get_files_info,
        schema_run_python_file,
        schema_write_file,
        schema_get_file_content,
    ]
    response = generate_content(messages, available_functions)
    if response.usage is None:
            raise RuntimeError

    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    message = response.choices[0].message

    if message.tool_calls:
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}") # type: ignore
            print(f"Calling function: {tool_call.function.name}({function_args})") # type: ignore
    else:
        print("Response:")
        print(message.content)

def generate_content(messages, available_functions):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )

    return response

if __name__ == "__main__":
    main()
