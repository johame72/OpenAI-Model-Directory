import openai

openai.api_key = 'YOUR_OPENAI_API_KEY_HERE'

response = openai.Model.list()

print(response)
