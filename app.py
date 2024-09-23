import os
from flask import Flask, request, jsonify,render_template
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array,load_img
from PIL import Image


app = Flask(__name__,template_folder='templates')
model = load_model("model/Chicken_fecal_with_callbacks.keras")

@app.route('/')
def index():
    return render_template('index.html')


def pre_process(file):
     # this will convert the live file into an image
    image = Image.open(file.stream)
    # this we need to run to convert the image into array
    image = img_to_array(image)
    image = image/255.0
    image = image.reshape((1,224,224,3))
    return image


@app.route('/upload',methods=['GET','POST'])
def predictions():
    if request.method == 'POST':
        file = request.files['file']
        image_pred = pre_process(file)
        img_pred = model.predict(image_pred)

        result = np.argmax(img_pred)

        if result == 0:
            result = 'Coccidiosis'
        else:
            result = 'Healthy'

        return render_template('index.html',result=result)
    
@app.route('/retrain',methods=['GET'])
def retrain():
    os.system('dvc repro')
    return jsonify({'message': 'Model retrained successfully'})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)


