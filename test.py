import google.generativeai as genai
import re  # Import the regular expressions library

genai.configure(api_key="Enter the key")
model = genai.GenerativeModel("gemini-1.5-flash")
prompt = "Generate a single positive and motivational quote by a well-known author, including the author's name for citation."
response = model.generate_content(prompt)

# Use regular expression to remove asterisks around the author's name
formatted_quote = re.sub(r'\*\*(.*?)\*\*', r'\1', response.text)
print(formatted_quote)
