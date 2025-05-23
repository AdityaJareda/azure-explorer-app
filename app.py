from flask import Flask, render_template
import os

app = Flask(__name__)

DEFAULT_IMAGE_URL = "https://via.placeholder.com/300x200.png?text=Default+Image"
IMAGE_URL = os.environ.get('APP_IMAGE_URL', DEFAULT_IMAGE_URL)

@app.route('/')
def hello_world():
    page_content = f"""
    <html>
        <head><title>Azure Explorer</title></head>
        <body style='font-family: sans-serif; text-align: center; background-color: #f0f8ff;'>
            <h1>Welcome to Azure Explorer!</h1>
            <p>This application is running in Azure.</p>
            <p>Powered by Python Flask, Docker, and various Azure Services.</p>
            <p>Update 1</p>
            <img src='{IMAGE_URL}' alt='App Image' style='max-width: 300px; margin-top: 20px; border: 1px solid #ccc;'>
            <p><small>Image URL: {IMAGE_URL}</small></p>
        </body>
    </html>
    """
    return page_content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
