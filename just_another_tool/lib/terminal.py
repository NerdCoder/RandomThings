import subprocess

def execute(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    flag = True
    try:
        output, error = proc.communicate() # timeout=15
    except error:
        flag = False
        proc.kill()
        output, error = proc.communicate()
    return output, error, flag
