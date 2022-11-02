import string #This import statement is the library that contains the method that can capitalize letters of every word

# This line takes in the string from the user
value = input("Please type a string 7 characters long.\n")

# This if statement checks that the string is at least 7 characters long
if len(value) >= 7 :
    # This is how to split a string into its individual characters then you save the value to a variable called split
    split = [*value]
    
    count = 0
    
    # Since the variable split is a list you access the 7th character like this
    print("The seventh character is:")
    print(split[6])
    
    # Since counting in computers starts from index 0, to get the second character we cut the string from index 1 up to the second last character using the colon marks. Then the last character we get using the mathematical expression -1 which takes the final index which we don't know and subtracts one.
    print("The string without its first and last characters:")
    print(value[1:-1])
    
    # Here we use the string library that has the method capwords which capitalizes the first letter of each word.
    print("The first character of each word capitalised:")
    print(string.capwords(value))
    
    # we use the method replace on the string that the user input which takes in the initial character "a" and replaces it with a new character "e"
    print("The string with 'a' replaced with 'e':")
    print(value.replace("a", "e"))
    
    # We use a for loop to loop every character in the string that the user entered, saved in the variable called value, then we use an if statement to check if the current character(char) is equal to any vowel. If it is true it increases the count value by one, then repeats until the last character of the string.
    print("The number of vowels in the string:")
    for char in value :
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" :
            count+=1
    print(count)
else :
    print("String not long enough.")
