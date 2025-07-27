import openai
import os

openai.api_type = "azure"
openai.api_base = os.getenv("https://chris-mdj3qdm6-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2025-01-01-preview")
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("4GVUpoI7aKvsRTJMuIH39QKh1mNC9owUTWbrHLqUeuUitefgP3k5JQQJ99BGACHYHv6XJ3w3AAAAACOGVzdh")

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        engine="my-gpt-deploy",  # This should match your deployment name in Azure OpenAI
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
