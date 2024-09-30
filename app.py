from diffusers import DiffusionPipeline
import torch
from transformers import pipeline
import gradio as gr

# translate tamil to english language
def translate_text_to_image(text):
  translator = pipeline("translation", model="Helsinki-NLP/opus-mt-dra-en")
  result = translator(text)
  prompt = result[0]['translation_text']
  return generate_image(prompt)

# generates images based on given prompt
def generate_image(prompt):
  """Generates an image from a text prompt using stable diffusion."""
  pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16).to("cuda")
  image = pipe(prompt).images[0]
  return image


iface = gr.Interface(
    fn=translate_text_to_image,
    inputs=gr.Textbox(lines=2, placeholder="Enter English text here..."),
    outputs="image",
    title="Tamil text to images",
    description="Tamil to english text, english text to image"
)

iface.launch()
