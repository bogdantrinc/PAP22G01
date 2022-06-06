import subprocess

from subprocess import run

result = run(['dir'], shell=True, text=True, capture_output=True)
print(type(result))
# print(result)
print(result.stdout)

result = run(['ping', '8.8.8.8', '-n', '1'], text=True, capture_output=True)
print(result.stdout)

from subprocess import Popen
result = Popen(['ping', '8.8.4.4', '-n', '1'], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = result.communicate()
print(stdout, stderr)

result = Popen(['ping', 'abc:/d'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = result.communicate()
print(stderr)

try:
    result = Popen(['notepad F:/text.x'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except FileNotFoundError:
    pass

result = Popen(['notepad', 'F:/text.x'], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

try:
    stdout, stderr = result.communicate()
except subprocess.SubprocessError:
    pass

print(stderr)

