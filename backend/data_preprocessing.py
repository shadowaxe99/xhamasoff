```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from PIL import Image
import pytesseract
import cv2
import numpy as np
import pandas as pd

nltk.download('punkt')
nltk.download('stopwords')

# Initialize stemmer
stemmer = PorterStemmer()

# Set of stopwords
stop_words = set(stopwords.words('english'))

def remove_stop_words(data):
    word_tokens = word_tokenize(data)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    return " ".join(filtered_sentence)

def apply_stemming(data):
    word_tokens = word_tokenize(data)
    stems = [stemmer.stem(word) for word in word_tokens]
    return " ".join(stems)

def run_ocr_on_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_image_features(image_path):
    image = cv2.imread(image_path)
    color_hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    color_hist = cv2.normalize(color_hist, color_hist).flatten()
    return color_hist

def preprocess_data(data):
    # Remove stop words
    data = remove_stop_words(data)
    # Apply stemming
    data = apply_stemming(data)
    return data
```