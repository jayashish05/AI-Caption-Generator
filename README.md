# AI Caption Generator

AI Caption Generator is a powerful tool designed to automatically generate engaging captions for your images using advanced artificial intelligence. Whether you're a social media manager, content creator, or just looking to add a creative touch to your pictures, this project helps you generate unique, context-aware captions in seconds.

## Features

- 🧠 AI-powered caption generation
- 📷 Supports various image formats
- 🌍 Multilingual capabilities
- 🎨 Customizable caption styles (funny, inspirational, descriptive, etc.)
- ⚡ Fast and easy-to-use interface
- 🔗 API support for integration

## Demo

Try it out here: https://ai-caption-generator-ibm.streamlit.app/


<img width="1470" alt="Screenshot 2025-07-03 at 11 16 35 PM" src="https://github.com/user-attachments/assets/39e6444c-a9c2-48d9-a82a-b855b1805c55" />
<img width="1470" alt="Screenshot 2025-07-03 at 11 16 42 PM" src="https://github.com/user-attachments/assets/44ebbfee-c524-4c09-b453-9806d43357f8" />


## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-caption-generator.git
   cd ai-caption-generator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Set up your API keys or environment variables**  
   If the project requires external AI APIs, follow the instructions in `.env.example` to set up your environment variables.

### Usage

#### Command Line

```bash
python generate_caption.py --image path/to/image.jpg --style descriptive
```

#### Web Interface

1. Start the server:
   ```bash
   python app.py
   ```
2. Open your browser and go to `http://localhost:5000`

#### API

Send a POST request to `/api/generate` with your image and options.

## Configuration

- **Caption Style:** Choose from various preset styles or add your own.
- **Language Support:** Set preferred output language.


## Acknowledgments

- Community contributors

---

*Ready to generate smarter captions? Give it a try and let your images speak!*
