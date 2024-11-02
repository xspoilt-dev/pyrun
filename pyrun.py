# -*- coding: utf-8 -*-
__author__ = "x_spoilt"
__version__ = "1.0.0"
__description__ = "A script to minify and run Python scripts."
__GitHub__ = "xspoilt-dev"

from subprocess import check_call, run, check_output
from sys import executable, argv, exit
from os.path import exists
from importlib.util import find_spec
from ast import parse, Module, FunctionDef, ClassDef, If, Expr, Constant

class _0xA:
    def __init__(self, _0xB, _0xC=False):
        self.__0xB = _0xB
        self.__0xC = _0xC
        self.__0xD()

    def __0xD(self):
        """Ensure astor is installed."""
        if not self.__0xE("astor"):
            print("Installing astor...")
            self.__0xF("astor")
        global astor
        import astor

    def __0xF(self, _0xG):
        """Install the specified package."""
        check_call([executable, "-m", "pip", "install", _0xG])

    def __0xE(self, _0xH):
        """Check if a module is installed."""
        return find_spec(_0xH) is not None

    def __0xI(self):
        """Check and install any missing packages used in the script."""
        with open(self.__0xB, 'r') as f:
            _0xJ = f.readlines()

        _0xK = set()
        for _0xL in _0xJ:
            _0xL = _0xL.strip()
            if _0xL.startswith('import '):
                _0xM = _0xL.split()[1].split('.')[0]
                _0xK.add(_0xM)
            elif _0xL.startswith('from '):
                _0xM = _0xL.split()[1].split('.')[0]
                _0xK.add(_0xM)

        _0xN = [pkg.split('==')[0] for pkg in check_output(
            [executable, "-m", "pip", "freeze"]).decode("utf-8").split('\n')]

        for _0xM in _0xK:
            if not self.__0xE(_0xM) and _0xM not in _0xN:
                print(f"Installing {_0xM}...")
                self.__0xF(_0xM)

    def __0xO(self, _0xP):
        """Remove docstrings and comments from the AST."""
        if isinstance(_0xP, Module):
            _0xP.body = [self.__0xO(_0xQ) for _0xQ in _0xP.body if not self.__0xR(_0xQ)]
        elif isinstance(_0xP, FunctionDef):
            _0xP.body = [self.__0xO(_0xQ) for _0xQ in _0xP.body if not self.__0xR(_0xQ)]
        elif isinstance(_0xP, ClassDef):
            _0xP.body = [self.__0xO(_0xQ) for _0xQ in _0xP.body if not self.__0xR(_0xQ)]
        elif isinstance(_0xP, If):
            _0xP.body = [self.__0xO(_0xQ) for _0xQ in _0xP.body if not self.__0xR(_0xQ)]
            if _0xP.orelse:
                _0xP.orelse = [self.__0xO(_0xQ) for _0xQ in _0xP.orelse if not self.__0xR(_0xQ)]
        return _0xP

    def __0xR(self, _0xQ):
        """Check if a node is a docstring."""
        return isinstance(_0xQ, Expr) and isinstance(_0xQ.value, Constant) and isinstance(_0xQ.value.value, str)

    def __0xS(self):
        """Minify the script by removing docstrings and comments."""
        with open(self.__0xB, 'r') as f:
            _0xT = f.read()

        _0xU = parse(_0xT)
        _0xU = self.__0xO(_0xU)

        _0xV = astor.to_source(_0xU)
        _0xV = "\n".join([_0xW for _0xW in _0xV.splitlines() if _0xW.strip()])

        _0xX = self.__0xB.replace('.py', '_minified.py')
        with open(_0xX, 'w') as f:
            f.write(_0xV)

        print(f"Minified script written to {_0xX}")
        return _0xX

    def __0xY(self):
        """Run the specified script."""
        run([executable, self.__0xB])

    def execute(self):
        """Execute the process of checking, minifying, and running the script."""
        if not exists(self.__0xB):
            print(f"{self.__0xB} does not exist.")
            exit(1)

        self.__0xI()

        if self.__0xC:
            self.__0xB = self.__0xS()

        self.__0xY()


if __name__ == "__main__":
    if len(argv) < 2 or len(argv) > 3:
        print("Usage: pyrun <script_path> [--minify]")
        exit(1)

    _0xB = argv[1]
    _0xC = len(argv) == 3 and argv[2] == '--minify'

    _0xZ = _0xA(_0xB, _0xC)
    _0xZ.execute()
