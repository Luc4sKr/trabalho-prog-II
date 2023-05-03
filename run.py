import os
from sys import platform

if __name__ == "__main__":

    backend_path = ".\\backend\\server.py"
    frontend_path = ".\\frontend\\dist"

    match platform:
        case ("win32"):
            os.system(f"start cmd /k python {backend_path}")
            os.system(f"start cmd /k python -m http.server -d {frontend_path}")
        
        case ("linux"):
            pass
    
    
    print("==" * 30)
    print("FRONTEND E BACKEND OPERANTES")
    print("==" * 30)