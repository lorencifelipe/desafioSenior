from configparser import Interpolation
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from wordcloud import WordCloud
import os

#Generate Word Cloud
def cloud(wordFreq):
    wc = WordCloud(background_color="black", max_words=len(
        wordFreq), max_font_size=256, random_state=42, width=600, height=600)
    wc.generate_from_frequencies(wordFreq)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
