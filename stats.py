def word_count(text):
    count = len(text.split())
    return count
    
def letter_tally(letters):
    tally = {}
    for letter in letters:
        letter = letter.lower()
        if letter not in tally:
            tally[letter] = 1
        else:
            tally[letter] += 1
    return tally

def sort_tally(tally_dict):
    
    sorted = []
    for char, count in tally_dict.items():
        entry = {"char": char, "num": count}
        sorted.append(entry)

    sorted.sort(reverse=True, key=sort_sorted)
    return sorted

def sort_sorted(item):
    return item["num"]