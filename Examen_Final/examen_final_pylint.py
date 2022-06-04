import pylint

options = ["--disable=no-member, line-too-long, f-string-without-interpolation, inconsistent-return-statements", 'examen_final']
pylint.run_pylint(argv=options)
