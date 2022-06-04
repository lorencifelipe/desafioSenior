from configparser import Interpolation
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from wordcloud import WordCloud
import os


def genCloud(wordFreq):
    dir = os.getcwd()
    mask = np.array(Image.open(dir+"/mail.jpg"))
    wc = WordCloud(background_color="white", max_words=len(
        wordFreq), max_font_size=256, random_state=42, mask=mask)
    wc.generate_from_frequencies(wordFreq)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    if not os.path.exists(dir+"/graphics"):
        os.makedirs("graphics")
    os.chdir(dir+"/graphics")
    if not os.path.isfile(dir+"/graphics/cloud.png"):
        plt.savefig("cloud.png")
    os.chdir(dir)
