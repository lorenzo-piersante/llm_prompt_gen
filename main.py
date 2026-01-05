import json
import os

def generate_symfony_prompt():
    project_path = os.path.expanduser("~/projects/clean_architecture_symfony")
    
    if not os.path.exists(project_path):
        return f"Error: Project directory not found at {project_path}"

    project_name = os.path.basename(os.path.abspath(project_path))
    composer_path = os.path.join(project_path, 'composer.json')
    
    if not os.path.exists(composer_path):
        return "Error: composer.json not found."

    with open(composer_path, 'r') as f:
        data = json.load(f)

    req = data.get('require', {})
    php_ver = req.get('php', 'Not found.')
    symfony_ver = req.get('symfony/framework-bundle', 'Not found.')
    doctrine_ver = req.get('doctrine/orm', 'Not found.')
    twig_ver = req.get('twig/twig', 'Not found.')
    
    req_dev = data.get('require-dev', {})
    phpunit_ver = req_dev.get('phpunit/phpunit', 'Not found.')

    structure = []
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in ['vendor', 'var', '.git', 'node_modules', 'public']]
        
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

    prompt_content = f"""Project name: {project_name}
PHP: {php_ver}
Symfony: {symfony_ver}
Doctrine: {doctrine_ver}
Twig: {twig_ver}
PHPUnit: {phpunit_ver}

Project structure:
{chr(10).join(structure)}

---
Act as a senior backend engineer with a great expertise in software architecture and design.
Be careful to find simple and readable solutions while avoiding unnecessary complexity and premature optimization.
Pragmatically adhere to Clean Architecture principles, considering the existing code base and its implications.
Request file content if more context is needed and suggest potential valuables refactoring of existing code related to the request.

Request: <insert your specific request here>
"""

    output_file = f"{project_name}.txt"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(prompt_content)
        return f"Success! Prompt generated at: {os.path.abspath(output_file)}"
    except Exception as e:
        return f"Error saving file: {e}"

if __name__ == "__main__":
    print(generate_symfony_prompt())
