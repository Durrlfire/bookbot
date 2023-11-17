def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print("--- Begin report of books/frankenstein.txt ---")
    count = word_count(text)
    print(f"{count} words found in the document")
    total_amount = word_occur(text)
    print("--- End report ---")
   


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)

def word_occur(text):
    char_occur = {}
    for t in text.lower():
        if t.isalpha():
            if t in char_occur:
                char_occur[t] += 1
            else:
                char_occur[t] = 1
    #print(char_occur)
    list_report = list(char_occur.items())
    list_report = sorted(list_report, key=lambda item: item[1] , reverse = True)
    #print(list_report)
    for t in list_report:
        print(f"The character {t[0]} appears {t[1]} times")

    



    
main()
