import openai
import requests
import streamlit
import os
import json
from dotenv import load_dotenv 

# Load environment variables from .env file
load_dotenv()

# Access environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
debug = os.getenv("DEBUG")

def BasicGeneration(userPrompt):
    try:
        completion = openai.Completion.create(
            model= 'gpt-3.5-turbo',
            messages=[{'role': 'user', 'text': userPrompt}]
        )

        return completion.choices[0].text
    except Exception as e:
        print(f"Error generating completion: {e}")

prompt = "please explain python programming language in 3 sentences"
response = BasicGeneration(prompt)
print(response)
