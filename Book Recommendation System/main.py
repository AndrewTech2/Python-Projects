import google.generativeai as genai

genai.configure(api_key='AIzaSyCNS5oZwCN1fs3KNj60SU1dNit1YLi91iU')
model = genai.GenerativeModel("gemini-1.5-flash")

summary = input("Enter a brief summary of a book you like:\n")


response = model.generate_content(f'Return a Python dictionary (name, short description) with similar books, considering the summary: "{summary}". Return only the dictionary, and nothing else.').text
books = eval(response[response.index("{"):response.index("}")+1])
print()
print("Recommended books:")
for book in books:
    print(f"- {book}: {books[book]}")