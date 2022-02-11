from django.core.management.utils import get_random_secret_key

if __name__ == "__main__":
    with open("./backend/secret.key", "w") as f:
        key = get_random_secret_key()
        f.write(key)