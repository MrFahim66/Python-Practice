dele = []
newstr = ' "This is the String that is Not Declared in the Given Code!" '
# newstr was not defined in given code

replace = "$"
# string replace method requires two arguments as strings but none given

string = input("Enter Any String: ")
ele = ('a', 'e', 'i', 'o', 'u')

for x in string.lower():
    if x in ele:
        dele.append(x)
        newstr = newstr.replace(x, replace)  # Error 1: 'newstr' is not defined, Error 2: replace method arguments are not valid

print(f'New String is: {newstr} from {string}')
print(f'Deleted are: {dele}')
