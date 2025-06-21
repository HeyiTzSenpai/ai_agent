import os


def get_file_content(working_directory, file_path):
    abs_file_path = os.path.abspath(file_path)
    abs_working_directory = os.path.abspath(working_directory)

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{abs_file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{abs_file_path}"'

    MAX_CHARS = 10000

    try:
        with open(abs_file_path, "r") as file:

            file_content_string = file.read()

            if len(file_content_string) > MAX_CHARS:
                file_content_string = file_content_string[:MAX_CHARS]

                return f"Reading from file path: {abs_file_path}\n\n{file_content_string}"

            return f"Reading from file path: {abs_file_path}\n\n{file_content_string}"

    except OSError:
        return f'Error: something went wrong while trying to access the contents of {abs_file_path}'
