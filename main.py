import os
from generators.core import PromptOrchestrator
from generators.symfony import SymfonyPlugin


class App:

    @staticmethod
    def run():
        plugins = [SymfonyPlugin]

        print("Select a project type to generate a prompt context:")
        for i, plugin in enumerate(plugins):
            print(f"{i + 1}. {plugin.get_name()}")

        choice = input("\nEnter the number of your choice: ")

        try:
            selected_index = int(choice) - 1
            if 0 <= selected_index < len(plugins):
                selected_plugin = plugins[selected_index]

                project_path = input("Enter the full path to your project directory: ")
                project_path = os.path.expanduser(project_path.strip())

                success, message = PromptOrchestrator.generate_prompt(project_path, selected_plugin)
                print(f"\n{message}")
            else:
                print("\nInvalid selection. Exiting.")
        except ValueError:
            print("\nPlease enter a valid number. Exiting.")


if __name__ == "__main__":
    App.run()