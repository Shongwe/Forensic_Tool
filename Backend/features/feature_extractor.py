# feature_extractor.py
import numpy as np
from PIL import Image, ImageFilter
from scipy.fftpack import dct
from scipy.ndimage import sobel

def load_image(path, size=(128,128)):
    img = Image.open(path).convert('RGB')
    if img.size != size:
        img = img.resize(size, Image.LANCZOS)
    return np.array(img).astype(np.float32) / 255.0

def color_moments(img):
    feats = []
    for c in range(3):
        channel = img[:,:,c].flatten()
        m = channel.mean()
        s = channel.std()
        skew = ((channel - m)**3).mean() / (s**3 + 1e-9)
        feats.extend([m, s, skew])
    return np.array(feats, dtype=np.float32)

def noise_residual_stats(img):
    gray = 0.2989*img[:,:,0] + 0.5870*img[:,:,1] + 0.1140*img[:,:,2]
    med = Image.fromarray((gray*255).astype(np.uint8)).filter(ImageFilter.MedianFilter(size=3))
    med = np.array(med).astype(np.float32)/255.0
    residual = gray - med
    return np.array([residual.mean(), residual.std(), np.mean(residual**3), np.mean(residual**4)], dtype=np.float32)

def dct_block_stats(img):
    gray = 0.2989*img[:,:,0] + 0.5870*img[:,:,1] + 0.1140*img[:,:,2]
    H, W = gray.shape
    stats = []
    for i in range(0, H-7, 8):
        for j in range(0, W-7, 8):
            block = gray[i:i+8, j:j+8]
            B = dct(dct(block.T, norm='ortho').T, norm='ortho')
            ac = B.flatten()[1:]
            stats.append(np.mean(np.abs(ac)))
    stats = np.array(stats)
    return np.array([stats.mean(), stats.std(), np.median(stats)], dtype=np.float32)

def lbp_histogram(img):
    gray = 0.2989*img[:,:,0] + 0.5870*img[:,:,1] + 0.1140*img[:,:,2]
    H, W = gray.shape
    lbp = np.zeros((H-2, W-2), dtype=np.uint8)
    for i in range(1,H-1):
        for j in range(1,W-1):
            center = gray[i,j]
            code = 0
            code |= (gray[i-1,j-1] > center) << 7
            code |= (gray[i-1,j  ] > center) << 6
            code |= (gray[i-1,j+1] > center) << 5
            code |= (gray[i  ,j+1] > center) << 4
            code |= (gray[i+1,j+1] > center) << 3
            code |= (gray[i+1,j  ] > center) << 2
            code |= (gray[i+1,j-1] > center) << 1
            code |= (gray[i  ,j-1] > center) << 0
            lbp[i-1,j-1] = code
    hist, _ = np.histogram(lbp, bins=32, range=(0,255))
    hist = hist.astype(np.float32) / (hist.sum()+1e-9)
    return hist

def gradient_stats(img):
    gray = 0.2989*img[:,:,0] + 0.5870*img[:,:,1] + 0.1140*img[:,:,2]
    gx = sobel(gray, axis=0)
    gy = sobel(gray, axis=1)
    mag = np.hypot(gx, gy)
    return np.array([mag.mean(), (mag>0.1).mean()], dtype=np.float32)

def extract_features_for_path(path):
    img = load_image(path)
    parts = []
    parts.extend(color_moments(img).tolist())
    parts.extend(noise_residual_stats(img).tolist())
    parts.extend(dct_block_stats(img).tolist())
    parts.extend(gradient_stats(img).tolist())
    parts.extend(lbp_histogram(img).tolist())
    return np.array(parts, dtype=np.float32)
