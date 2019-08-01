# Module to run programs
import subprocess

def run_program(name):
    try: 
        cp = subprocess.run(["./apps/" + name], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return cp.stdout
    except subprocess.CalledProcessError:
        return "CalledProcessError"
    except OSError:
        return "OSError"