import google.generativeai as genai
import re  # Import the regular expressions library
import os
from dotenv import load_dotenv  # Import dotenv
import time

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
prompt = "You’re a creative writer with a passion for crafting unique and uplifting quotes. You have a talent for capturing the essence of positivity in a few impactful words, inspiring others with your wisdom and creativity. You have a big memory of the famous quotes in the world. Your goal is to generate one positive quote that can uplift and motivate people in their daily lives. I am going to put the quote directly on twitter. Directly generate the quote with the citation of the author, the one who said the quotes do not include emojis or hashtags. Remeber not to generate the same quotes generate unique quotes with each request I make."

i = 10

for x in range(i):
    time.sleep(5)
    response = model.generate_content(prompt)
    # Use regular expression to remove asterisks around the author's name
    formatted_quote = re.sub(r'\*\*(.*?)\*\*', r'\1', response.text)
    print(formatted_quote)

