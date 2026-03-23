import json
import os


class FileSystemUtils:

    @staticmethod
    def read_json(file_path: str) -> dict:
        if not os.path.exists(file_path):
            return {}
        try:
            with open(file_path, 'r', encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    @staticmethod
    def build_directory_tree(project_path: str, ignore_dirs: list[str]) -> str:
        project_name = os.path.basename(os.path.abspath(project_path))
        structure = []

        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]

            relative_path = os.path.relpath(root, project_path)
            if relative_path == ".":
                level = 0
                dir_name = project_name
            else:
                level = relative_path.count(os.sep) + 1
                dir_name = os.path.basename(root)

            indent = ' ' * 4 * level
            structure.append(f"{indent}📁 {dir_name}/")

            sub_indent = ' ' * 4 * (level + 1)
            for f in files:
                structure.append(f"{sub_indent}📄 {f}")

        return chr(10).join(structure)

    @staticmethod
    def write_file(file_path: str, content: str) -> tuple[bool, str]:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True, f"Success! Prompt generated at: {os.path.abspath(file_path)}"
        except Exception as e:
            return False, f"Error saving file: {e}"