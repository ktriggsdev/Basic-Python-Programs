def main():
    sts = str(input("Input: "))
    without_vowels = shorten(sts)
    print(f"Output: {without_vowels}")

def shorten(word):
    return "".join(
        letter
        for letter in word
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']
    )

if __name__ == "__main__":
    main()