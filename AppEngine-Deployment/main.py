import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import CustomObjectScope
from tensorflow.keras.initializers import glorot_uniform
from scipy.misc import imresize, imread
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, request, jsonify
import os
import base64
from io import BytesIO

app = Flask(__name__)


with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
    model = load_model('weights/model_weights.h5')

def evaluate_image(image_array):
	class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
	image_array_re = imresize(image_array, (28, 28))
	image_array_re = image_array_re.reshape(1, 28, 28, 1)
	preds = model.predict(image_array_re)
	category_int = np.argmax(preds, axis=1)
	return class_names[int(category_int)]

@app.route('/predict', methods=['POST'])
def predict():
	input_file = request.files.get('file')
	if not input_file:
	    return BadRequest("File is not present in the request")
	if input_file.filename == '':
	    return BadRequest("Filename is not present in the request")
	if not input_file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
	    return BadRequest("Invalid file type")

	input_buffer = BytesIO()
	input_file.save(input_buffer)
	image_array = imread(input_buffer, mode='L')
	category = evaluate_image(image_array)
	return jsonify({'Category': str(category)})

@app.route('/')
def index():
    return "This is just an index page and nothing else!"
