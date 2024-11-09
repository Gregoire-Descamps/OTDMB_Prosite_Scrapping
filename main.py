#allow to install automatically required pakages at startup
import subprocess, sys
try :
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
except :


    subprocess.Popen(["sudo", "apt", "install", "python3-venv"], shell=True)
    subprocess.check_call(["wsl.exe", "source", "env/bin/activate"], shell=False)
    subprocess.check_call(["-m", "pip", "install", "-r", "requirements.txt"], shell=False)


import MySQL

MySQL.CreateEngine("MySQL://localhost/PrositeLocalDB")

