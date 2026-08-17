from pathlib import Path
import shlex
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SCRAPER = ROOT / "siemprelistos-scraper" / "scraper_siemprelistos.py"

print("=== SiempreListos Scraper ===")
print()
print("Introduce los argumentos que quieres pasar al scraper.")
print("Ejemplo: --output-dir descargas_scouts --delay 1")
print()

args = input("> ")

if not args.strip():
    print("No se introdujeron argumentos.")
    sys.exit(0)

command = [
    sys.executable,
    str(SCRAPER),
    *shlex.split(args),
]

subprocess.run(command, check=True)