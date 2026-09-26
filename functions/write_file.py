import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes or overwrites to specified file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to write to, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Content to write or overwrite to file",
                }
            },
            "required": ["file_path", "content"],
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.isdir(absolute_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        if not os.path.commonpath([working_dir_abs, absolute_file_path]) == working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        os.makedirs(os.path.dirname(absolute_file_path), exist_ok=True)
    except Exception as e:
        return f"Error: {e}"

    with open(absolute_file_path, "w") as f:
        try:
            f.write(content)
        except Exception as e:
            return f"Error: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'