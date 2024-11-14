#allow to install automatically required pakages at startup
import subprocess, sys
try :
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], shell=False)
except :
    print("Could not install the requirements, please verify your pip installation\nIf you use wsl, it's recommended to create a virtual environment")
    raise

# check if MySQL is installed
try :
    subprocess.call(["mysql", "--version"],stdout=subprocess.DEVNULL)
except:
    print("MySQL is not installed, please install and configure it before running this script")
    exit()


import ScrapPySQL

DBConn = MySQL.DBConnection()