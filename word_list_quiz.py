with open("words_alpha.txt", "r") as words:
    all_words = words.read().splitlines()

length = len(all_words)

print("There are " + str(length) + " words in this word list.")

five_count = 0
for w in all_words:
    if len(w) == 5:
      five_count += 1

print(str(five_count) + " words are exactly 5 letters long.")

seven_count = 0
for w in all_words:
    if len(w) > 7:
        seven_count += 1

print(str(seven_count) + " words are greater than 7 letters long.")

total_char = 0
for w in all_words:
    total_char += len(w)

print("There is a total of " + str(total_char) + " characters used in all words.")

no_e = 0
for w in all_words:
    if "e" not in w:
        no_e += 1

print(str(no_e) + " words do not have the letter 'e'.")

start_end_same = 0
for w in all_words:
    if w[0] == w[-1]:
        start_end_same += 1

print(str(start_end_same) + " words begin and end with the same letter.")

three_a = 0
for w in all_words:
    a_count = 0
    for c in w:
        if c == "a":
            a_count +=1
    if a_count == 3:
        three_a += 1

print("There are " + str(three_a) + " words that have exactly 3 As.")
    
        
no_qu = 0
