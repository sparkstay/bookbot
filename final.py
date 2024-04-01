def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def count_words():
    words = text.split()
    print(len(words))
    return len(words)
    

main()
