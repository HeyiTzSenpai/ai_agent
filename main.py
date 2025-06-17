import os
import sys
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) == 2:
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=sys.argv[1]
        )
        print(response.text)

        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    else:
        print('Wrong arguments, Usage: python3 main.py <"prompt">')
        sys.exit(1)



if __name__ == "__main__":
    main()
