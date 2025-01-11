import pypdf

word = input("Enter the word to search for > ")

file = pypdf.PdfReader("pdf1.pdf")
occurrences = 0
for page in file.pages:
    text = page.extract_text()
    occurrences += text.count(word)

print(f"The word '{word}' appears {occurrences} times.")