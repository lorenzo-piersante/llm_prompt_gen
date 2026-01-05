📂 Symfony Prompt Context Tool

A simple Python utility to generate a context-rich text file for LLMs based on a local Symfony project.

🛠️ Functionality

    Version Detection: Extracts PHP, Symfony, Doctrine, Twig, and PHPUnit versions from composer.json.

    Tree Mapping: Scans the project directory and builds a visual tree (skipping vendor, var, etc.).

    Senior Persona: Includes a pre-written prompt header focused on Clean Architecture and pragmatic engineering.

🚀 Usage

    Set your project path in the script:
    Python

    project_path = os.path.expanduser("~/projects/my_project")

    Run the script: python main.py

    A .txt file named after your project will be generated in the same folder.

📄 Output Structure

    Project Info: Versions and dependencies.

    Directory Tree: Visual map of your src/, config/, and templates/.

    Instruction Set: High-level instructions for the AI.