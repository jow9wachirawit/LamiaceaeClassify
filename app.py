''''''
from json import load
from tkinter.filedialog import Open
import warnings
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

st.title("Program Classify Lamiaceae")

#def load_image():
    #uploaded_file = st.file_uploader(label='Pick an image to test')
   # if uploaded_file is not None:
  #      image_data = uploaded_file.getvalue()
 #       st.image(image_data)
#def main():
  #  st.title('Image upload demo')
 #   load_image()


#if __name__ == '__main__':
  #  main()

#from glob import glob
#from pathlib import Path

#def load_model():
  #model = tf.kerasmod

#learn_inf = load(googlenet_model-2.pkl)

#learn_inf.predict(load_image()) 

from fastai.vision.all import (load_learner, PILImage,)

import glob
import streamlit as st
from PIL import Image
from random import shuffle
import urllib.request
