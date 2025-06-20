import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions import get_files_info


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]

    if len(sys.argv) == 3:
        if sys.argv[2] == "--verbose":
            response = client.models.generate_content(
                model='gemini-2.0-flash-001',
                contents=messages
            )

            prompt_tokens = response.usage_metadata.prompt_token_count
            response_tokens = response.usage_metadata.candidates_token_count

            print(f"User prompt: {sys.argv[1]}")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")
            print(response.text)

    elif len(sys.argv) == 2:
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages
        )
        print(response.text)




    else:
        print('Wrong arguments, Usage: python3 main.py <"prompt"> --verbose(optional)')
        sys.exit(1)


if __name__ == "__main__":
    main()
