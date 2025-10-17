import os
import requests
from tqdm import tqdm
import random

# -------------------------------
# CONFIG
# -------------------------------
AI_SAVE_DIR = "data/ai_generated"
REAL_SAVE_DIR = "data/real_images"

NUM_IMAGES = 200   # Number of images per category
AI_SOURCE = "https://thispersondoesnotexist.com"
REAL_SOURCE = "https://picsum.photos/256"

os.makedirs(AI_SAVE_DIR, exist_ok=True)
os.makedirs(REAL_SAVE_DIR, exist_ok=True)

# -------------------------------
# Helper Function
# -------------------------------
def download_images(url_func, save_dir, label, allow_redirects=False):
    print(f"\n Downloading {NUM_IMAGES} {label} images...")
    success, fail = 0, 0
    for i in tqdm(range(NUM_IMAGES)):
        try:
            url = url_func()
            response = requests.get(url, timeout=10, allow_redirects=allow_redirects)
            if response.status_code == 200:
                # Ensure proper file extension
                filename = f"{label}_{i+1}.jpg"
                with open(os.path.join(save_dir, filename), "wb") as f:
                    f.write(response.content)
                success += 1
            else:
                fail += 1
        except Exception as e:
            fail += 1
    print(f" {success} {label} images downloaded successfully,  {fail} failed.")

# -------------------------------
# Download AI-generated faces
# -------------------------------
def ai_url():
    return f"{AI_SOURCE}?cache_bust={random.randint(0,999999)}"

download_images(ai_url, AI_SAVE_DIR, "ai", allow_redirects=False)

# -------------------------------
# Download Real Images
# -------------------------------
def real_url():
    return f"{REAL_SOURCE}?sig={random.randint(0,999999)}"

#  Follow redirects for Unsplash
download_images(real_url, REAL_SAVE_DIR, "real", allow_redirects=True)

print("\n Dataset download complete!")
print(f" AI images saved to: {AI_SAVE_DIR}")
print(f" Real images saved to: {REAL_SAVE_DIR}")
