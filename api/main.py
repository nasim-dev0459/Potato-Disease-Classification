from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()


MODEL = tf.keras.models.load_model("1.keras")
CLASS_NAMES = ["Potato Early Blight", "Potato Late Blight", "Potato Healthy"]


@app.get("/ping")
async def ping():
    return "Hello, Server is running!"


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = np.array(Image.open(BytesIO(await file.read())))
    img_batch = np.expand_dims(image, 0)

    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)