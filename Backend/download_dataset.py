import os
import requests
from tqdm import tqdm
import random

#image location
AIDIR = "data/ai_generated"
REALDIR = "data/real_images"

NUMIMAGES = 200   

#choose AI source
AISOURCES = [
    "https://generated.photos/faces", 
    "https://www.artbreeder.com",      
    "https://www.rosebud.ai",          
    "https://creator.nightcafe.studio",
]

REALSOURCE = "https://picsum.photos/256"

os.makedirs(AIDIR, exist_ok=True)
os.makedirs(REALDIR, exist_ok=True)


def download_images(url_func, save_dir, label, allow_redirects=False):
    print(f"\n Downloading {NUMIMAGES} {label} images...")
    success, fail = 0, 0
    for i in tqdm(range(NUMIMAGES)):
        try:
            url = url_func()
            response = requests.get(url, timeout=10, allow_redirects=allow_redirects)
            if response.status_code == 200:
                filename = f"{label}_{i+1}.jpg"
                with open(os.path.join(save_dir, filename), "wb") as f:
                    f.write(response.content)
                success += 1
            else:
                fail += 1
        except Exception as e:
            fail += 1
    print(f" {success} {label} images downloaded successfully,  {fail} failed.")

# Get images

def ai_url():
    source = random.choice(AISOURCES)
    return f"{source}?cache_bust={random.randint(0,999999)}"

download_images(ai_url, AIDIR, "ai", allow_redirects=False)


def real_url():
    return f"{REALSOURCE}?sig={random.randint(0,999999)}"

download_images(real_url, REALDIR, "real", allow_redirects=True)


print("Dataset download complete!")
print(f"AI images saved to: {AIDIR}")
print(f"Real images saved to: {REALDIR}")