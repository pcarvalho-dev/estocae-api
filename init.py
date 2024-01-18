import os

os.system(f"docker-compose down --volumes --remove-orphans && docker-compose up --build")
