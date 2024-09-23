import os
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image  # Import PIL Image
import io

app = Flask(__name__, template_folder='templates')
model = load_model("model/Chicken_fecal_with_callbacks.keras")

@app.route('/')
def index():
    return render_template('index.html')

def pre_process(file):
    # Read the file into a PIL Image
    image = Image.open(file.stream)  # Ensure it's in RGB format
    image = image.resize((224, 224))  # Resize the image
    image = img_to_array(image)  # Convert to numpy array
    image = image / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Expand dimensions to add batch size of 1
    return image

@app.route('/upload', methods=['GET', 'POST'])
def predictions():
    if request.method == 'POST':
        file = request.files['file']
        image_pred = pre_process(file)  # Pass the file object directly
        img_pred = model.predict(image_pred)

        result = np.argmax(img_pred)

        if result == 0:
            result = 'Coccidiosis'
        else:
            result = 'Healthy'

        return render_template('index.html', result=result)

@app.route('/retrain', methods=['GET'])
def retrain():
    os.system('dvc repro')
    return jsonify({'message': 'Model retrained successfully'})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
