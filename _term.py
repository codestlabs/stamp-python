import subprocess
import time
import sys
class Terminal:
    def PythonRun(command="print()", delay=0.0):
        if delay != 0.0: time.sleep(delay)
        else: pass
        if sys.platform.startswith("win") == True:
            subprocess.run(["start", "cmd.exe", "/k", [sys.executable, "-c", command]], shell=True)
        else:
            subprocess.run([sys.executable, ["-c", command]])
    def Run(command="msinfo32.exe" if sys.platform.startswith("win") == True else f"{sys.executable}", delay=0.0):
        if delay != 0.0: time.sleep(delay)
        else: pass
        if sys.platform.startswith("win") == True:
            subprocess.run(["start", "cmd.exe", ["/k", command]], shell=True)
        else:
            subprocess.run([command], shell=True)
    def clear():
        if sys.platform.startswith("win") == True:
            subprocess.run(["cls"], shell=True)
        else:
            subprocess.run(["clear"], shell=True)