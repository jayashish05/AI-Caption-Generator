import streamlit as st
import os
from PIL import Image
import base64
from io import BytesIO
import requests
import time

GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY")

def generate_caption_with_gemini(image_base64, tone='default'):
    if not GEMINI_API_KEY:
        return "⚠️ Please set your GEMINI_API_KEY in Streamlit secrets."

    tone_prompts = {
        'default': "Generate a concise and descriptive caption for this image in 1-2 sentences.",
        'funny': "Generate a humorous and witty caption for this image.",
        'emotional': "Generate an emotional and touching caption for this image.",
        'professional': "Generate a professional and formal caption for this image.",
        'short': "Generate a very short caption for this image (10 words max)."
    }

    prompt = tone_prompts.get(tone, tone_prompts['default'])

    try:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": GEMINI_API_KEY
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt},
                        {
                            "inline_data": {
                                "mime_type": "image/jpeg",
                                "data": image_base64
                            }
                        }
                    ]
                }
            ],
            "generation_config": {
                "temperature": 0.4,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 100
            }
        }

        with st.spinner("✨ Generating caption..."):
            response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            candidates = result.get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                for part in parts:
                    if "text" in part:
                        return part["text"].strip()
            return "No caption found."
        else:
            return f"Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"

colors = {
    "bg": "#1e1e2f",
    "text": "#f1f1f1",
    "card": "#2d2d44",
    "accent": "#8B80FF",
    "button": "#8B80FF",
    "button_text": "#ffffff",
    "info_text": "#f1f1f1"
}

st.markdown(f"""
    <style>
        .stApp {{
            background-color: {colors['bg']};
            color: {colors['text']};
        }}
        .main-title {{
            text-align: center;
            color: {colors['accent']};
            font-size: 2.5rem;
            margin-top: 0;
        }}
        .sub-info {{
            text-align: center;
            color: {colors['text']};
            margin-bottom: 2rem;
        }}
        .card {{
            background-color: {colors['card']};
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }}
        .caption-box {{
            background-color: {colors['card']};
            color: {colors['text']};
            border-left: 5px solid {colors['accent']};
            padding: 1rem;
            margin-top: 1rem;
            border-radius: 10px;
        }}
        .stButton>button {{
            background-color: {colors['button']} !important;
            color: {colors['button_text']} !important;
            font-weight: bold;
            border-radius: 20px;
            padding: 0.5rem 1.5rem;
            border: none;
            box-shadow: 0 3px 8px rgba(0,0,0,0.15);
        }}
        .stButton>button:hover {{
            opacity: 0.9;
            cursor: pointer;
        }}
        .stAlert>div {{
            color: {colors['info_text']} !important;
        }}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🖼️ AI Caption Generator</h1>", unsafe_allow_html=True)
st.markdown("<div class='sub-info'>Upload an image and let AI generate the perfect caption!</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)
    tone = st.selectbox("Choose a caption style:", ["Standard", "Humorous", "Emotional", "Professional", "Short"])

    if st.button("✨ Generate Caption"):
        buffered = BytesIO()
        image.convert("RGB").save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        caption = generate_caption_with_gemini(img_str, tone.lower())
        st.markdown(f"<div class='caption-box'>{caption}</div>", unsafe_allow_html=True)
else:
    st.info("📸 Please upload an image to begin.")
