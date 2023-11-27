# utils/hebrew_conversion.py

def replace_final_forms(hebrew_string):
    words = hebrew_string.split()

    final_letters = {'מ': 'ם', 'נ': 'ן', 'צ': 'ץ', 'פ': 'ף', 'כ': 'ך'}

    result = []
    for word in words:
        if len(word) > 1:  # Exclude one-letter words
            for non_final, final in final_letters.items():
                if word.endswith(non_final):
                    word = word[:-1] + final
        result.append(word)

    return ' '.join(result)
