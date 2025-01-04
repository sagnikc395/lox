import sys
import os
from typing import List


class GenerateAST:
    @staticmethod
    def defineAST(outputdir: str, baseName: str, types: List[str]):
        try:
            path = os.path.join(outputdir, f"{baseName}.py")

            with open(path, "w", encoding="utf-8") as writer:
                writer.write("from abc import ABC, abstractmethod")
                writer.write("\n")
                writer.write(f"class {baseName}(ABC):\n")
                writer.write("\t")

                for type in types:
                    className = type.split(":")[0]
                    fields = type.split(":")[1]
                    self.defineType(writer, baseName, className, fields)

        except Exception as e:
            print(e)

    # script away your syntax trees from this
    @staticmethod
    def main():
        try:
            args = sys.argv
            if len(args) != 1:
                print("Usage: genast <output directory>")
                os.exit(64)
            outputdir = args[0]
            GenerateAST.defineAST(
                outputdir,
                "Expr",
                [
                    "Binary   : Expr left, Token operator, Expr right",
                    "Grouping : Expr expression",
                    "Literal  : Object value",
                    "Unary    : Token operator, Expr right",
                ],
            )

        except Exception as e:
            print(e)
