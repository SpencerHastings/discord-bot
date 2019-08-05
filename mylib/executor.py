# Module to run programs
import subprocess

DEBUG = True

def run_program(name, args):
    try: 
        if DEBUG:
            print("(cd ./apps/" + name + "/ && make ARGS=\"" + args +  "\" run --silent)")
        cp = subprocess.run(["(cd ./apps/" + name + "/ && make ARGS=\"" + args +  "\" run --silent)"], shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return cp.stdout
    except subprocess.CalledProcessError:
        return "CalledProcessError"
    except OSError:
        return "OSError"

#cp = subprocess.run(["./apps/" + name + "/make ARGS=\"" + args +  "\" run --silent"], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)