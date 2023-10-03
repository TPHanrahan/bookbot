def word_counter(word):
    words = word.split()
    word_count =  len(words)
    return word_count

def letter_count(file):
    alphabet_dict = {}
    file_fixed = file.lower()
    for letter in file_fixed:
        if letter in alphabet_dict:
            alphabet_dict[letter] += 1

        else:
            alphabet_dict[letter] = 1
    return alphabet_dict
    
    
def main():
    book_path = "/home/mumbles/workspace/github.com/TPHanrahan/bookbot/books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    lettercount = letter_count(file_contents)
    wordcount = word_counter(file_contents)
    print(f"--- Begin report of {book_path} ---")
    print(f"{wordcount} words found in the document")
    for i in sorted(lettercount):
        if i.isalpha():
            print(f"The '{i}' character was found {lettercount[i]} times")
    print("--- End Report ---")

main()