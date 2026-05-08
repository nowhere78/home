import os
from dotenv import load_dotenv

load_dotenv()

access = os.getenv("UPBIT_ACCESS_KEY", "")
secret = os.getenv("UPBIT_SECRET_KEY", "")

print(f"Access Key Length: {len(access)}")
print(f"Secret Key Length: {len(secret)}")

if access.strip() != access:
    print("Warning: Access Key has leading/trailing spaces!")
if secret.strip() != secret:
    print("Warning: Secret Key has leading/trailing spaces!")

if "ACCESS_KEY" in access or "SECRET_KEY" in secret:
    print("Warning: Keys still contain placeholder text!")
