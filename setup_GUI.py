import subprocess
import os

PROJECTNAME = 'SpotiToTube'
VERSION = '0.1'
AUTHOR = 'David \'rEaliZe\' M.'

# Aktualisiere die Abhängigkeiten mit 'pip freeze'
print("Aktualisiere Abhängigkeiten mit 'pip freeze'...")
with open("requirements.txt", "w") as requirements_file:
    subprocess.check_call(["pip", "freeze"], stdout=requirements_file)

# Führe PyInstaller aus
print("Führe PyInstaller aus...")
cmd = [
    "pyinstaller",
    "--onefile",   # Eine einzelne ausführbare Datei erstellen
    # Hier können Sie weitere PyInstaller-Optionen hinzufügen
    "--noconsole", 
    # "--windowed",
    "--name", f"{PROJECTNAME}_V{VERSION}",
    # "--icon", f"{os.path.abspath('assets/VC_Logo.ico')}",
    "--add-data", f"../../packages;packages",# ; os.path.abspath('GUI/')",
    "--add-data", f"../../GUI/*.py:GUI",# ; os.path.abspath('GUI/')",
    # "--exclude-module", "pathlib",
    "--hidden-import", 'spotipy',
    "--hidden-import", 'ytmusicapi',
    "--hidden-import", 'pandas',
    # "--upx-dir", "path/to/upx",
    # "--additional-hooks-dir", "path/to/hooks",
    # "--clean",
     "--distpath", "",
    "--specpath", "build/spec",
    # "--workpath", "work_directory",
    # "--log-level", "INFO",
    "main.py"
]
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError as e:
    raise SystemExit(e)