import streamlit as st
from PIL import Image
import torch
import requests
from io import BytesIO

# Set page title
st.title("Object Detection with Bounding Boxes")

# Load YOLOv5 model with caching
@st.cache_resource
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    model.conf = 0.6  # Set confidence threshold
    return model

model = load_model()

# Image input options
option = st.radio("Select input method:", ("Upload an image", "Enter image URL"))

image = None

if option == "Upload an image":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
else:
    url = st.text_input("Enter image URL:")
    if url:
        try:
            response = requests.get(url)
            image = Image.open(BytesIO(response.content)).convert('RGB')
        except:
            st.error("Error: Could not download image from URL")

# Process and display image
if image is not None:
    with st.spinner('Detecting objects...'):
        # Perform inference
        results = model(image)
        
        # Render results
        results.render()  # Add bounding boxes to image
        
        # Convert to PIL image
        img_with_boxes = Image.fromarray(results.ims[0])
        
    # Display results
    st.image(img_with_boxes, caption="Detected Objects", use_container_width=True)
    
    # Show detection summary
    df = results.pandas().xyxy[0]
    if not df.empty:
        st.write(f"Detected {len(df)} object(s):")
        st.write(df[['name', 'confidence']].rename(columns={
            'name': 'Object Type',
            'confidence': 'Confidence'
        }))
    else:
        st.warning("No objects detected with current confidence threshold")