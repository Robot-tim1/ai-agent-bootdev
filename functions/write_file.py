import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        if not os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        os.makedirs(os.path.dirname(target_file), exist_ok=True)
    except Exception as e:
        return f"Error: {e}"

    with open(target_file, "w") as f:
        try:
            f.write(content)
        except Exception as e:
            return f"Error: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'