import pylint

options = ["--disable=no-member, line-too-long", 'sample_1.py']
pylint.run_pylint(argv=options)
