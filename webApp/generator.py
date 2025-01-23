import time
import random
import requests

BASE_URL = "http://127.0.0.1:5000"  # L'URL où tourne votre Flask local

def main():
    while True:
        box_id = random.choice([1, 2])
        tel_id = random.randint(1, 3)
        url = f"{BASE_URL}/{box_id}/{tel_id}"

        try:
            resp = requests.get(url)
            print(f"Increment -> {url} [status={resp.status_code}]")
        except Exception as e:
            print(f"Erreur lors de la requête : {e}")

        time.sleep(0.5)  # Attendre 2 secondes avant la prochaine incrémentation

if __name__ == "__main__":
    main()
