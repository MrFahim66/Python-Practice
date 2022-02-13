string_input = str(input())
splitted_string = string_input.split()

dictionary = {}

list_string = list(splitted_string)
print("Words:", list_string)

for word in splitted_string:
    for i in range(len(splitted_string)):
        splitted_string[i] = splitted_string[i].lower()

    if (word[0] not in dictionary.keys()):
        dictionary[word[0]] = []
        dictionary[word[0]].append(word)
    else:
        if (word not in dictionary[word[0]]):
            dictionary[word[0]].append(word)

print(dictionary)