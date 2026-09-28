
from flask import Flask, request, jsonify
import numpy as np
from tensorflow import keras
from PIL import Image

app = Flask(__name__)

model = keras.models.load_model("models/baseline_ann.h5")

def preprocess_image(image_file):
    img = Image.open(image_file).convert("L").resize((28, 28))
    arr = np.array(img).astype("float32") / 255.0
    return arr.reshape(1, 784)

@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    processed = preprocess_image(file)

    prediction = model.predict(processed, verbose=0)

    predicted_class = int(np.argmax(prediction))
    confidence = float(np.max(prediction))

    return jsonify({
        "predicted_digit": predicted_class,
        "confidence": round(confidence, 4)
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
