import json
from difflib import get_close_matches

data = json.load(open("data.json"))  #


def searching_the_dictionary(w):  #
    if w in data:
        means = data[w.lower()]
        printing(w, means)
    elif len(get_close_matches(w, data.keys())) > 0:
        x = get_close_matches(w, data.keys())[0]
        print("Do you mean?", x)
        print("Y/n")
        decision = input().lower()
        if decision[0] == 'y':
            searching_the_dictionary(x)
    else:
        print("No word like '", w, "' exists! Please double check it.")


def printing(w, m):  #
    print(w, ":")
    for ele in m:
        print(ele)


word = input("Enter a word you want to search: ")
searching_the_dictionary(word)