import readline  # noqa: F401
import argparse
from .llm import llm


def chat(args):
    """
    Function to start a chat.
    """
    print("Starting the conversation. Type 'quit' or 'exit' to leave.")
    chat_helper = llm()
    exit_commands = {"quit", "exit"}

    while True:
        user_input = input("\n\033[92mYou:\033[0m ").lower()
        if user_input.lower() in exit_commands:
            print("\n\033[91mExiting the chat...\033[0m")
            break

        try:
            response = chat_helper.send_message(user_input)
            print(f"\n\033[95mAI: {response}\033[0m")

        except (ValueError, KeyboardInterrupt) as e:
            print(f"\nError: {e}\nInterrupted by user. Exiting...")
            break


def parse_args():
    """
    Function to parse command line arguments.
    """
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest="command")
    commands.required = True

    chat_parser = commands.add_parser("chat")
    chat_parser.set_defaults(func=chat)

    return parser.parse_args()


def main():
    """
    Main function to execute the program.
    """
    args = parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
