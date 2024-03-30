import textwrap
from google.generativeai import genai

# Manually provide the API key
GOOGLE_API_KEY = "Your_Api_Key"

genai.configure(api_key=GOOGLE_API_KEY)


def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)


model = genai.GenerativeModel('gemini-pro')
# model = genai.GenerativeModel('gemini-pro-vision')
while True:
    ques = input("Enter Your question: ")
    response = model.generate_content(ques)

    try:
        response.text
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
    print(to_markdown(response.text))
