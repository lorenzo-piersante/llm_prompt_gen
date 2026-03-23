# 📂 Prompt Context Tool

A centralized Python utility to generate context-rich text files for LLMs based on your local projects. 


### 🛠️ Architecture & Features

* **Centralized Orchestration**: The core orchestrator handles file system operations, directory tree building, and string assembly, removing repetitive boilerplate from individual framework generators.
* **Static Namespace Plugins**: Framework-specific logic (like reading a `composer.json` or `package.json`) is isolated into pure aggregator classes with strictly defined static methods.
* **5-Part Output Format**: Every generated prompt guarantees this structure:
    1. **Role**: The AI persona and required expertise.
    2. **Context**: Environment details (dependency versions) + a fully mapped visual directory tree (ignoring `vendor`, `node_modules`, etc.).
    3. **Task**: A designated placeholder for you to type your explicit objective.
    4. **Constraints**: Framework-specific rules (e.g., Clean Architecture, PEP 8).
    5. **Output Format**: Enforces clean, code-first deliverables without conversational filler.

### 🚀 Usage

- Run the interactive script:
```shell
python main.py
```

- Select your project framework from the terminal menu (e.g., 1 for PHP Symfony).
- Enter the absolute path to your local project directory.

A .txt file named after your project will be generated in your current directory. Open it, replace [INSERT YOUR SPECIFIC TASK HERE], and paste the entire text into your LLM of choice.

### 🧩 Adding a New Framework Plugin
To add support for a new framework, simply create a new file in generators/ with a class containing the following static methods and name attribute.

```python
class MyNewPlugin:
    @staticmethod
    def get_name() -> str:
        return "My Framework Name"

    @staticmethod
    def build_role() -> str: 
        return "Act as a Senior..."

    @staticmethod
    def build_context(project_path: str) -> str: 
        return "Environment Details..."

    @staticmethod
    def build_constraints() -> list[str]: 
        return ["Constraint 1", "Constraint 2"]

    @staticmethod
    def build_output_format() -> str: 
        return "Output only code..."
```

Then, register it in the plugins list in main.py.

```python
plugins = [..., MyNewPlugin]
```

📚 Resources on prompt generation:

- OpenAPI: https://developers.openai.com/api/docs/guides/prompt-engineering
- Anthropic: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices