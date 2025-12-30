import random
words = (
    "apple", "banana", "cherry", "orange", "grapes", "mango", "papaya",
    "lemon", "peach", "pear", "plum", "melon", "kiwi", "guava", "apricot",
    "carrot", "potato", "tomato", "onion", "garlic", "pepper", "spinach",
    "cabbage", "broccoli", "cucumber", "lettuce", "pumpkin", "radish",
    "zebra", "tiger", "lion", "monkey", "elephant", "giraffe", "panda",
    "rabbit", "horse", "donkey", "kangaroo", "leopard", "cheetah",
    "python", "javascript", "coding", "computer", "keyboard", "screen",
    "school", "college", "teacher", "student", "library", "notebook",
    "planet", "galaxy", "universe", "rocket", "astronaut"
)
word = random.choice(words)

tries = 6
result = ""
allguesses = ""


while tries > 0:
    guesses = input("guess the word: ")
    allguesses += guesses
    result = ""

    for i in word:
        if i in allguesses:
            result += i
        else:
            result += "_"
    if result == word:
        print("You won!")
        break
    print(result)
    tries -= 1
    print(f"you have {tries} tries left")

    if tries == 0:
        print(f"the correct answer is {word}")

        break