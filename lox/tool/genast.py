import sys
import os


class GenerateAST:
    # script away your syntax trees from this
    @staticmethod
    def main():
        try:
            args = sys.argv
            if len(args) != 1:
                print("Usage: genast <output directory>")
                os.exit(64)

        except Exception as e:
            print(e)
