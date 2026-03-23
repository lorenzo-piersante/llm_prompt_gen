import os
from utils import FileSystemUtils

class PromptOrchestrator:

    @staticmethod
    def generate_prompt(project_path: str, plugin_class) -> tuple[bool, str]:
        """Centralized assembly using static methods from the provided plugin class."""
        if not os.path.exists(project_path):
            return False, f"Error: Project directory not found at {project_path}"

        project_name = os.path.basename(os.path.abspath(project_path))

        # 1. Role
        role = plugin_class.build_role()

        # 2. Context
        context_details = plugin_class.build_context(project_path)
        tree = FileSystemUtils.build_directory_tree(project_path, plugin_class.get_ignore_dirs())
        context = f"{context_details}\n\nProject Structure:\n{tree}"

        # 3. Task
        task = "[INSERT YOUR SPECIFIC TASK HERE]"

        # 4. Constraints
        constraints_list = plugin_class.build_constraints()
        constraints = "\n".join([f"- {c}" for c in constraints_list])

        # 5. Output Format
        output_format = plugin_class.build_output_format()

        # Assembly
        prompt_content = f"""### Role
{role}

### Context
{context}

### Task
{task}

### Constraints
{constraints}

### Output Format
{output_format}
"""

        output_file = f"{project_name}.txt"

        return FileSystemUtils.write_file(output_file, prompt_content)