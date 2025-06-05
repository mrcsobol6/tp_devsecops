import subprocess

print("Bandit: \n*******")
subprocess.run(['bandit', '*.py'])

print("Pip-audit: \n**********")
subprocess.run(['pip-audit'])