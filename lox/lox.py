import sys
import os


class Lox:
    @staticmethod
    def main():
        try:
            args = sys.argv
            if len(args) > 1:
                print("Usage: lox [script]")
                os.exit(64)
            elif len(args) == 1:
                Lox.run_file(args[0])
            else:
                Lox.run_prompt()
        except Exception as e:
            print(e)

    @staticmethod
    def run_file(path: str):
        try:
            with open(path, "r") as f:
                bytes = f.read()
            Lox.run(bytes)

        except Exception as e:
            print(e)

    @staticmethod
    def run(source: str):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        for token in tokens:
            print(token)

    @staticmethod
    def run_prompt():
        try:
            while True:
                print("> ", end="")
                line = input()
                if line == "":
                    break
                Lox.run(line)
        except Exception as e:
            print(e)
