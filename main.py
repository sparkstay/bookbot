#CREATE A SYSTEM THAT RETURNS DATA ABOUT A BOOK(essentially)

#   READ FILE FUNCTION. lesson #13
book_path = "books/frankenstein.txt"
def main():
    # the with statement is how you open files
    with open("books/frankenstein.txt") as f:
         file_contents = f.read()
         #print(file_contents)
    return file_contents

main()

# COUNT WORDS. lesson #14
def count_words(text):
     with open(f"{text}") as f:
          file_contents = f.read()
          words = file_contents.split()
          return len(words)
     
book_length = (count_words(book_path))



#COUNT LETTERS. lesson #15
     #create empty dictionary to add letter counts to
letter_count = {}
def count_letters(text):
    #get text and convert the whole thing to lowercase
    with open(f"{text}") as f:
        file_contents = f.read()
        #confirm file_content type is a str: yes
        #print(type(file_contents))
        lowercase_text = file_contents.lower()
        #confirm contents were converted to lowercase: yes
        #print(lowercase_text)
        #make list of words
        words = lowercase_text.split()
        #then iterate through that list to make a list of letters
        all_letters = []
        for word in words:
             for i in range(len(word)):
                all_letters.append(word[i])
                #confirm you have a list of all the individual, lowercase letters: yes
                #print(all_letters)

        #Now we need to go through the letters list. If the letter doesn't already exist in the dictionary, then we can create a new key/value pair
        #If it does exist already then we will increase the value for that key by 1
        for current_letter in all_letters:
            if  current_letter in letter_count.keys():
                letter_count[current_letter] += 1
            else:
                letter_count[current_letter] = 1
        #confirm it works: yep!
        #print(letter_count)
        return letter_count
        

count_letters("books/frankenstein.txt")

'''
The boot.dev solution: much clearer than mine of course but hey I got there in the end!

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

'''

#PRINT A REPORT. lesson #16
#Convert the letter_count dictionary to a list of dictionaries

#Create empty list to append to
letter_count_list = []
#sort through each letter in the letter count dictionary to create a mini dictionary for it to be appeneded to the letter count list
for letter in letter_count:
    #print(letter)
    mini_dict = {}
    mini_dict['letter'] = letter
    mini_dict['occurrences'] = letter_count[letter]
    letter_count_list.append(mini_dict)
    

def sort_by_occurences(dict):
    return dict["occurrences"]

letter_count_list.sort(reverse=True, key=sort_by_occurences)
#print(letter_count_list)

#OK... now we need to remove any characters that aren't a letter
letter_count_no_symbols = []
for mini_dict in letter_count_list:
    if mini_dict["letter"].isalpha():
        letter_count_no_symbols.append(mini_dict)

#FINALLY... PRINT THE FULL REPORT
print(f"--- Begin report of {book_path} ---")
print(f"{book_length} words found in the document")
for mini_dict in letter_count_no_symbols:
    print(f"The '{mini_dict["letter"]}' character was found {mini_dict["occurrences"]} times")

print("--- End Report ---")