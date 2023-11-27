from collections import defaultdict
from itertools import permutations
from tqdm import tqdm
from utils.hebrew_conversions import replace_final_forms
import time

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

def preprocess_words(words):
    sorted_words_dict = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        sorted_words_dict[sorted_word].append(word)
    return sorted_words_dict

def find_anagrams(phrase, sorted_words_dict):
    start_time = time.time()

    phrase_letters = ''.join(sorted(phrase.lower().split()))
    single_word_anagrams = set()
    two_word_anagrams = set()

    for perm in tqdm(permutations(phrase_letters), desc="Finding Anagrams", unit="permutation"):
        candidate = ''.join(perm)

        # Check for single-word anagrams
        if candidate in sorted_words_dict:
            single_word_anagrams.update(sorted_words_dict[candidate])

        # Check for two-word anagrams
        for word in sorted_words_dict:
            if word in candidate:
                for first_word in sorted_words_dict[word]:
                    remainder = candidate.replace(first_word, '')
                    if remainder in sorted_words_dict:
                        for second_word in sorted_words_dict[remainder]:
                            two_word_anagrams.add(f"{first_word} {second_word}")

    end_time = time.time()
    search_time = end_time - start_time

    return list(single_word_anagrams), list(two_word_anagrams), search_time

if __name__ == "__main__":
    file_path = "words.txt"  # Update with your file path
    phrase = input("Enter a phrase to find anagrams: ").strip()

    if not phrase:
        print("Please enter a valid phrase.")
    else:
        words = read_words_from_file(file_path)

        if words:
            sorted_words_dict = preprocess_words(words)
            single_word_anagrams, two_word_anagrams, search_time = find_anagrams(phrase, sorted_words_dict)

            if single_word_anagrams:
                print(f"Single word anagrams for '{phrase}':")
                for anagram in single_word_anagrams:
                    print(replace_final_forms(anagram))
            else:
                print(f"No single word anagrams found for '{phrase}'.")

            if two_word_anagrams:
                print(f"\nTwo-word anagrams for '{phrase}':")
                for anagram in two_word_anagrams:
                    print(replace_final_forms(anagram))
            else:
                print(f"No two-word anagrams found for '{phrase}'.")

            print(f"\nSearch time: {search_time:.6f} seconds")
        else:
            print("Unable to process due to file reading issues.")
