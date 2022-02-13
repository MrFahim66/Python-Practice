def Check_Vow(string, vowels):
    final = [each for each in string if each in vowels]
    return len(final)

cnt = 0
while True:
    string_input = str(input())
    if string_input == "Done":
        cnt += 1
        if cnt == 1:
            print("No String Was Entered!")
        break
    else:
        cnt += 1
        num_words = string_input.split()
        print("Number of Words:", len(num_words))
        string3 = string_input
        vowels = "AaEeIiOoUu"
        print("Number of Vowels:",Check_Vow(string3, vowels))
        print("Total Length:", len(string_input))