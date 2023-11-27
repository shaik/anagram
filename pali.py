def read_words_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line.strip() for line in file]
        return words
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def find_palindromes(words):
    palindromes = [word for word in words if word.lower() == word.lower()[::-1]]
    return palindromes

if __name__ == "__main__":
    file_path = "words.txt"  # Update with your file path

    words = read_words_from_file(file_path)

    if words:
        palindromes = find_palindromes(words)

        if palindromes:
            print("Palindromes in the list:")
            for i, palindrome in enumerate(palindromes, 1):
                print(f"{i}. {palindrome}")
        else:
            print("No palindromes found in the list.")
    else:
        print("Unable to process due to file reading issues.")
