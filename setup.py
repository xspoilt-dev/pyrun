from Cython.Build.BuildExecutable import build
import subprocess
import os
import platform

print("Building Executable...")
build('pyrun.py')
if platform.system() == "Linux":
    if os.environ.get("PREFIX"):
        print("Setting up pyrun as a global command in Termux...")
        termux_path = os.path.join(os.environ['PREFIX'], 'bin', 'pyrun')
        subprocess.run(['mv', 'pyrun', termux_path])
        subprocess.run(['chmod', '+x', termux_path])
        print(f"Executable moved to {termux_path} and set as executable.")
    else:
        print("Setting up pyrun as a global command on Linux...")
        subprocess.run(['mv', 'pyrun', '/usr/local/bin/pyrun'])
        subprocess.run(['chmod', '+x', '/usr/local/bin/pyrun'])
        print("Executable moved to /usr/local/bin and set as executable.")

elif platform.system() == "Windows":
    print("Setting up pyrun as a global command on Windows...")
    user_path = os.environ['USERPROFILE'] + "\\AppData\\Local\\pyrun"
    os.makedirs(user_path, exist_ok=True)
    subprocess.run(['move', 'pyrun.exe', user_path], shell=True)
    subprocess.run(
        f'setx PATH "%PATH%;{user_path}"', shell=True, check=True
    )
    print("Executable moved to AppData\\Local and added to PATH.")

else:
    print("Unsupported OS.")
