import google.generativeai as genai

genai.configure(api_key="AIzaSyC6FL3epnmHmE5XVd6XQLZok3aeEQge99U")
model = genai.GenerativeModel("gemini-1.5-flash")
prompt = "Generate a single positive and motivational quote by a well-known author, including the author's name for citation."
response = model.generate_content(prompt)
print(response.text)
