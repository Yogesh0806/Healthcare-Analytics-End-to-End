'''
utils.py    Reusable helper functions for Healthcare Analysis Project
'''

from pathlib import Path 
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent.parent

IMAGE_DIR = BASE_DIR / "Images"
IMAGE_DIR.mkdir(exist_ok = True)
