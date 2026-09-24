import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        if not os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: {e}"

    files = os.listdir(target_dir)
    results: list[str] = []
    for file in files:
        path = os.path.join(target_dir, file)
        results.append(f"- {file}: file_size={os.path.getsize(path)} bytes, is_dir={os.path.isdir(path)}")
    return "\n".join(results)