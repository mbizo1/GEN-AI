import cohere
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

#co = os.getenv('COHERE_API_KEY')
#print(os.getenv('COHERE_API_KEY')) returns NONE
#print(os.environ) returns all Environment

ky = cohere.Client(os.getenv('COHERE_API_KEY')) #getting the API key from env file

def text_output(textIn):
    output = ky.chat(
    model = "command-r-plus",
    message = textIn
)
    return output.text

#print(f"API Key: {ky}")