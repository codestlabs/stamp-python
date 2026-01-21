import os
import subprocess
import sys
class PhysicsSetup:
    def __init__(self):
        self.root_dir = r'C:\Physics'
        self.script_name = 'physics.py'
        self.icon_name = 'physics.ico'
        self.exe_name = 'physics.exe'
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.script_path = os.path.join(self.current_dir, self.script_name)
        self.icon_path = os.path.join(self.current_dir, self.icon_name)
        self.dist_path = os.path.join(self.root_dir, 'dist')
        self.final_exe_path = os.path.join(self.root_dir, self.exe_name)
    def build_and_run(self):
        try:
            os.makedirs(self.root_dir, exist_ok=True)
            print(f"dir ensured: {self.root_dir}")
        except OSError as e:
            pass
        pyinstaller_command = [
            sys.executable,  
            '-m', 'PyInstaller',
            '--onefile',    
            '--icon', self.icon_path, # Path is now a separate item, no quotes
            '--distpath', self.root_dir, # Path is now a separate item, no quotes
            self.script_path
        ]
        try:
            result = subprocess.run(
                pyinstaller_command,
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode != 0:
                print(result.stdout)
                print(result.stderr)
                return    
        except FileNotFoundError:
            print("Error: PyInstaller or Python executable not found.")
            return 
        except Exception as e:
            print(f"An unexpected error occurred during compilation: {e}")
            return   
        try:
            subprocess.Popen([
                'start', 
                'cmd', 
                '/k', 
                f'cd /d C:\ && {self.final_exe_path} && exit'
            ], shell=True)
            print(f"Application launched: {self.exe_name}")
        except Exception as e:
            print(f"Warning: Failed to launch application executable via 'start cmd /k'. Please run manually: {self.final_exe_path}. Error: {e}")

if __name__ == '__main__':
    PhysicsSetup().build_and_run()
