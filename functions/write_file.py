import os.path


def write_file(working_directory, file_path, content):
    abs_work_dir_path = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(file_path)

    if not abs_filepath.startswith(abs_work_dir_path):
        return f'Error: Cannot write to "{abs_filepath}" as it is outside the permitted working directory'

    try:
        directory = os.path.dirname(abs_filepath)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with open(abs_filepath, "w") as file:
            file.write(content)

        return f'Successfully wrote to "{abs_filepath}" ({len(content)} characters written)'


    except OSError:
        return f'Error: something went wrong while trying to create a new directory:  {abs_filepath}'
