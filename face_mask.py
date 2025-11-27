import streamlit as st
from main import prediction
from PIL import Image
import cv2

st.set_page_config(page_title="Face Mask Detection", layout="centered")

st.title(':blue[Face Mask Detection]')
st.subheader(":blue[Click on the option below]")


if "show_uploader" not in st.session_state:
    st.session_state.show_uploader = False

if "show_camera" not in st.session_state:
    st.session_state.show_camera = False

if st.button("Upload an Image"):
    st.session_state.show_uploader = True
    st.session_state.show_camera = False

if st.button("Click an Image"):
    st.session_state.show_camera = True
    st.session_state.show_uploader = False

if st.session_state.show_uploader:
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:    
        pred = prediction(uploaded_file, 'button1')
        labels = (pred > 0.5).astype(int)
        if labels[0] == [0]:
            st.subheader('Image is with mask')
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
        else:
            st.subheader('Image is without mask')
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)

elif st.session_state.show_camera:
    capture = cv2.VideoCapture(0)
    isTrue, frame = capture.read()
    if isTrue:
        cv2.imwrite("captured_image.jpg", frame)
        img = cv2.imread("captured_image.jpg")
        cv2.waitKey(1000)
        capture.release()
        cv2.destroyAllWindows()
        pred = prediction(img, 'button2')
        labels = (pred > 0.5).astype(int)
        if labels[0] == [0]:
            st.subheader('Image is with mask')
            image = Image.open("captured_image.jpg")
            st.image(image, use_container_width=True)
        else:
            st.subheader('Image is without mask')
            image = Image.open("captured_image.jpg")
            st.image(image, use_container_width=True)
    else:
        print("Error: Failed to capture image.")

