import subprocess

host = "www.google.com"

res = subprocess.Popen(
    ['ping', '-c', '3', host]
    )

out, error = res.communicate()
print(out)
