import pdfplumber

counter = 0
x = (input("Enter a word you want to search for: ")).strip().lower()
with pdfplumber.open('pdf1.pdf') as pdf:
    pages = pdf.pages
    for page in pages:
        text = page.extract_text().lower()
        words = text.split(" ")
        for word in words:
            # counter += words.count(x) can be used instead of for loop
            if word == x:
                counter +=1
    print(f'The word {x} occurs {counter} times in PDF ')


