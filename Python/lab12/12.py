
sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in sentence:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1

words = len(sentence.split())
letters = vowels + consonants
percentage = (vowels / letters) * 100

print("=" * 44)
print("DOCUMENT ANALYSIS REPORT")
print("=" * 44)
print("Sentence:", sentence)
print("Total characters:", len(sentence))

print()
print("--- Character Breakdown ---")
print("Words:              ", words)
print("Vowels:             ", vowels)
print("Consonants:         ", consonants)
print("Digits:             ", digits)
print("Spaces:             ", spaces)
print("Special characters: ", special)

print()
print("--- Summary ---")
print("Total letters:", letters)
print("Vowel percentage:", str(round(percentage, 1)) + "%")

print()
print("=" * 44)
print("Analysis Complete!")
print("=" * 44)