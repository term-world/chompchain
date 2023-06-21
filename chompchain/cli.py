from .chain import *
from .generate import *

from arglite import parser as cliarg

def main():
    if cliarg.optional.chain:
        return Chain()
    if cliarg.optional.generate:
        generate()
