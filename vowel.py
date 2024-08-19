# PROGRAM TO COUND THE NUMBER OF EACH VOWEL 
# USING DICTIONARY
 
a = " Harry Potter And The Prisoner Of Azkaban"
vowels = "aeiou"
a = a.casefold()

count = {}.fromkeys(vowels,0)
for i in a:
    if i in count:
        count[i] += 1 
print(count) 

# out put of this program {'a': 5, 'e': 2, 'i': 1, 'o': 3, 'u': 0}

# second solution : using list and dictionary comprehension 
a = " Harry Potter And The Prisoner Of Azkaban"
vowels = "aeiou"
a = a.casefold()

count = {key:sum([1 for char in a if char == key])for key in vowels }
print(count)