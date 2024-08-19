import platform
import os


class Security:
    @staticmethod
    def get_os():
        if platform.system() == "Linux":
            if os.path.exists("/data/data/com.termux"):
                return "Termux"
            else:
                return "Linux"
        elif platform.system() == "Windows":
            return "Windows"
        else:
            return "Unknown OS"
        
if Security.get_os()=='Windows':
    os.system('cd Windows && python run.py') 
elif Security.get_os()=='Linux':
    os.system('cd Linux && python3 run.py')
elif Security.get_os()=='Termux':
    os.system('cd Termux && python3 run.py')
    