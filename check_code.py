import subprocess

print("Bandit: \n*******")
res = subprocess.run(['bandit', '*.py'], shell=False)
    

print("Pip-audit: \n**********")
subprocess.run(['pip-audit'], shell=False)