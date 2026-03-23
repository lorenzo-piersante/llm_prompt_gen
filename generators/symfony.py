import os
from utils import FileSystemUtils


class SymfonyPlugin:
    @staticmethod
    def get_name() -> str:
        return "PHP Symfony"

    @staticmethod
    def build_role() -> str:
        return "Act as a Senior Backend Engineer with great expertise in software architecture, PHP, and the Symfony framework."

    @staticmethod
    def build_context(project_path: str) -> str:
        composer_path = os.path.join(project_path, 'composer.json')
        data = FileSystemUtils.read_json(composer_path)

        if not data:
            return "Error parsing composer.json. No dependency versions available."

        req = data.get('require', {})
        req_dev = data.get('require-dev', {})

        versions = {
            "PHP": req.get('php', 'Not found.'),
            "Symfony": req.get('symfony/framework-bundle', 'Not found.'),
            "Doctrine": req.get('doctrine/orm', 'Not found.'),
            "Twig": req.get('twig/twig', 'Not found.'),
            "PHPUnit": req_dev.get('phpunit/phpunit', 'Not found.')
        }

        return "Environment Versions:\n" + "\n".join([f"- {k}: {v}" for k, v in versions.items()])

    @staticmethod
    def get_ignore_dirs() -> list[str]:
        return ['.git', 'node_modules', 'vendor', 'var', 'public', 'bin']

    @staticmethod
    def build_constraints() -> list[str]:
        return [
            "Find simple and readable solutions avoiding unnecessary complexity and premature optimization.",
            "Pragmatically adhere to Clean Architecture principles, considering the existing code base and its implications.",
            "Request file content if more context is needed.",
            "Suggest potential valuable refactoring of existing code related to the request."
        ]

    @staticmethod
    def build_output_format() -> str:
        return "Output only the refactored or generated code blocks. Include inline comments explaining complex logic. Do not write an introductory or concluding explanation."