import openai
import os

openai.api_type = "azure"
openai.api_base = "https://chris-mdj3qdm6-eastus2.openai.azure.com/openai"
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        engine="gpt-4.1",  # This should match your deployment name in Azure OpenAI
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]