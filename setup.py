# Verificador de dependencias

import subprocess
import os
def main():


    try:
        subprocess.call(["nmap", "--version"])
    except ImportError:
        print 'Nmap no se tiene instalado... O se encuentra en otro directorio. Porfavor instalar, o especificar el directorio en ~/gpt.conf'
        os.exit(1)

if __name__ == "__main__":
    main()
