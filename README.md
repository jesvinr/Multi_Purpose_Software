# Tamil Text to English Image Generator

This project translates Tamil text to English and then generates an image based on the translated text using AI models. It utilizes a serverless architecture with AWS Lambda and provides a user interface using Gradio.

## Features

- Translates Tamil text to English
- Generates images based on the translated English text
- User-friendly interface using Gradio
- Serverless deployment using AWS Lambda

## Technologies Used

- Python
- Gradio (for UI)
- Hugging Face Transformers
- Diffusers
- AWS Lambda

## Models

1. Translation: "Helsinki-NLP/opus-mt-dra-en"
2. Image Generation: "runwayml/stable-diffusion-v1-5"

## Prerequisites

Before running this project, make sure you have the following dependencies installed:

```
pip install gradio diffusers transformers accelerate scipy ftfy sentencepiece
```

## Setup and Deployment

1. Clone this repository
2. Install the required dependencies
3. Set up an AWS Lambda function
4. Deploy the code to AWS Lambda
5. Configure the Gradio interface to interact with the Lambda function

## Usage

1. Open the Gradio interface
2. Enter Tamil text in the input field
3. Click the "Translate and Generate Image" button
4. View the translated English text and the generated image

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- Hugging Face for providing the translation and image generation models
- The Gradio team for their excellent UI framework
- AWS for their serverless Lambda service
