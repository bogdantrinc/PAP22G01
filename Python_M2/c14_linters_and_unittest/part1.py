import pylint

options = ["--disable=unnecessary-lambda,missing-function-docstring", 'file0.py']
pylint.run_pylint(argv=options)
