import os


def get_files_info(working_directory, directory=None):
    directory_full_path = os.path.abspath(directory)
    working_directory_full_path = os.path.abspath(working_directory)

    if not directory_full_path.startswith(working_directory_full_path):
        return f'Error: Cannot list "{directory_full_path}" as it is outside the permitted working directory'

    elif not os.path.isdir(directory_full_path):
        return f'Error: "{directory_full_path}" is not a directory'

    try:

        dir_contents = os.listdir(directory)
        string_contents = ""

        for content in dir_contents:
            full_path = os.path.join(directory, content)

            string_contents += f"{content}: file_size={os.path.getsize(full_path)}bytes, is_dir={os.path.isdir(full_path)}\n"

    except OSError:
        return f'Error: something went wrong while trying to access or list the contents of {directory_full_path}'

    return string_contents
