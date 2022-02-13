# defining function for ease of work
def CountCharacters(listname):
    char_count = 0
    for i in range(0, 4):
        char_count += len(OwnList[i])  # counting characters using loop
    return char_count  # returning character count


# defining function for ease of work
def CountVowels(listName):
    vowels = 'AEIOUaeiou'
    vowel_count = sum([1 for char in ''.join(listName) if char in vowels])  # counting vowels
    return vowel_count  # returning vowel count


# Name : Fahim
# District : Dhaka
# ID : 201-15-13674
# University : Daffodil International University

OwnList = ['Fahim', 'Dhaka', '201-15-13674', 'Daffodil International University']

# printing
print("Number of Character:", CountCharacters(OwnList))
print("Number of Vowels:", CountVowels(OwnList))
