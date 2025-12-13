def count_words(text):
    words = text.split()
    total_words = len(words)
    return f"Found {total_words} total words"

''' Start with an empty dictionary,
Loop over each character in lower_case,
And update the count for that character in the dictionary? '''
def num_chars(text):
    lower_case = text.lower()
    lower_case_dict = {}
    for char in lower_case:
        if char in lower_case_dict:
            lower_case_dict[char] += 1
        else:
            lower_case_dict[char] = 1
    return lower_case_dict  


def sort_on(item):
    return item["num"]

def report(dict):
    result = []
    for i in dict:
        result.append({"char": i, "num": dict[i]})
    result.sort(key=sort_on, reverse = True)
    return result    