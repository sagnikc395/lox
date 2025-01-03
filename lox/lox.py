import sys
import os


class Lox:
    hadError: bool

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

            if Lox.hadError:
                os.exit(65)

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
                Lox.hadError = False

        except Exception as e:
            print(e)

    @staticmethod
    def error(line: int, message: str):
        Lox.report(line, "", message)

    @staticmethod
    def report(line: int, where: str, message: str):
        print(f"[line {line}] Error {where} : {message}")
        Lox.hadError = True
