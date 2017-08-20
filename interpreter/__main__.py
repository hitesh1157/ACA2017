import argparse
import logging

import execfile

parser = argparse.ArgumentParser(
    prog="A py-py Interpreter",
    description="Run Python scripts with a Python bytecode interpreter.",
)
parser.add_argument(
    '-m', dest='module', action='store_true',
     help="script is a module name, not a file name.",
)
parser.add_argument(
    '-v', '--verbose', dest='verbose', action='store_true',
    help="Trace the execution of the bytecode.",
)
parser.add_argument(
    'script',
    help="scriptname.py module to execute",
)
parser.add_argument(
    'args', nargs=argparse.REMAINDER,
    help="Arguments to pass to the program.",
)
args = parser.parse_args()

if args.module:
    run_fn = execfile.run_python_module
else:
    run_fn = execfile.run_python_file

level = logging.DEBUG if args.verbose else logging.WARNING
logging.basicConfig(level=level)

argv = [args.script] + args.args
run_fn(args.script, argv)
