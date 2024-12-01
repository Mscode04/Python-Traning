def counter(Word):
    vowels="aeiouAEIOU"
    vowelCount= 0
    consonantCount= 0
    for char in Word:
        if char.isalpha():
            if char in vowels:
                vowelCount+= 1
            else:
                consonantCount+= 1
    return vowelCount, consonantCount


# Example usage
string = "Love you"
vowels, consonants = counter(string)
print("Number of vowels: ",vowels)
print("Number of consonants: ",consonants)
