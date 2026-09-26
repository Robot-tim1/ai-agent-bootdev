import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Execute a specified Python file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to Execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "list of optional arguments",
                }
            },
            "required": ["file_path"],
        },
    },
}

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        working_dir_abs = os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not os.path.commonpath([working_dir_abs, absolute_file_path]) == working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        command = ["python", absolute_file_path]
        if args is not None:   
            command.extend(args)

        result = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd="/home/tim/workspace/tim/python-projects/ai-agent-bootdev/calculator")
        format_return = ""
        if result.returncode != 0:
            format_return += f"Process exited with code {result.returncode}\n\n"
        if not result.stdout and not result.stderr:
            format_return += "No output produced\n"
        else:
            format_return += f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        return format_return
    except Exception as e:
        return f"Error: executing Python file: {e}"