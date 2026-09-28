
# MNIST Digit Recognition - Deep Learning Lab

## Experiment 8: Model Deployment

This project deploys a trained MNIST ANN model using:

- Flask REST API
- Streamlit Web UI
- TensorFlow/Keras

## API Endpoints

### Health Check

GET /health

### Prediction

POST /predict

The prediction endpoint accepts an image and returns:

- Predicted digit
- Confidence

## Running the API

```bash
python app.py
