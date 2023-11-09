#anagram is where both the strings have each characters of the same frequency
#danger and garden is an example of an anagram

def isanagram(s1,s2):
    if(len(s1)!=len(s2)):
        return False

    # return sorted(s1) == sorted(s2)
    freq1 = {} #declaring dictionaries for mapping purpose
    freq2 = {}

    #using dictionary(hash table) for  assigning the character as key and no of times it repeated as values
    # {
    #     char1:value1
    # }
    for char in s1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    for char in s2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    return not any(
        key not in freq2 or value != freq2[key] for key, value in freq1.items()
    )



s1 = input("Enter a string\n")
s2 = input("Enter second string\n")

if isanagram(s1,s2):
    print(f"\nThe {s1} and {s2} are Anagrams")
else:
    print(f"{s1} and {s2} are not anagram")