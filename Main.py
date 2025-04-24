import gradio as gr
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Last inn ResNet50-modellen
model = load_model('RESNET_w_rotate_15epochs_true.h5')


def predictGender(img):
    try:
        if isinstance(img, np.ndarray):
            img = Image.fromarray(img)
        else:
            img = Image.open(img)

        img = img.resize((224, 224))

        img_array = np.array(img)

        if img_array.shape == (224, 224, 3):
            img_array = img_array.astype('float32') / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)
            print(f"Prediksjon: {prediction}")

            if prediction <= 0.5:
                gender = 0
            else:
                gender = 1

            if gender == 1:
                return f"Du er en kvinne med {prediction[0][0] * 100:.2f}% sannsynlighet"
            else:
                return f"Du er en mann med {(1-prediction[0][0]) * 100:.2f}% sannsynlighet"

    except Exception as e:
        print(f"Could not process image {img}: {e}")
        return f"Feil under behandling av bildet: {e}"


def get_image(input_img):
    return predictGender(input_img)

user_image = gr.Interface(fn=get_image, inputs=gr.Image(type="numpy"), outputs="text")

user_image.launch(share=True)