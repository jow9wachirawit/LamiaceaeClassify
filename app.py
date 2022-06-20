from fastai.vision.all import *
import glob
from random import shuffle
import urllib.request
import streamlit as st
import pathlib

#temp = pathlib.PosixPath
#pathlib.PosixPath = pathlib.WindowsPath

image1 = Image.open('image1.jpg')
# title
st.title("Lamiaceae Classify")
# load model
# model_url = "https://github.com/KaiZer003/ProjectpythonDeploy/raw/c78341c53f34ce6ec7b6498b9e8057023eaec320/googlenet_model-2.pkl"
# urllib.request.urlretrieve(model_url,"model.pkl")
learn_inf = load_learner('model.pkl',cpu=True)

def predict(img, learn):
    # make prediction
    pred, pred_idx, pred_prob = learn_inf.predict(img)
    # Display the prediction
    st.success(f"This is {pred}  with the probability of {pred_prob[pred_idx]*100:.02f}%")
    # Display the test image
    st.image(img, use_column_width=True)

#title sidebar
st.sidebar.title('Enter Lamiaceae Classify')

# image source selection
option = st.sidebar.radio('',['Use your own image'])
valid_images = glob.glob('images/valid/*/*')
shuffle(valid_images)
if option == 'Use your own image':
    st.sidebar.write('### Select an image to upload')
    fname = st.sidebar.file_uploader('',
                                     type=['png', 'jpg', 'jpeg'],
                                     accept_multiple_files=False)
    if fname is None:
        st.subheader('give me your besil')
        st.image(image1, caption='image by jannoon028', width=None)
        st.sidebar.write("AI Builders page [link](https://www.facebook.com/aibuildersx)")
        st.sidebar.write("Lamiaceae Classify at Github [link](https://github.com/KaiZer003/ProjectpythonDeploy)")
        st.stop()
# open image
img = PILImage.create(fname)
# infer
predict(img, learn_inf)

