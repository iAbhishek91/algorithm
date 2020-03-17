# Guess the secret word, you have only three tries

secret_game = "draft"

guess = ""
allowed_try = 3

while guess != secret_game and allowed_try > 0:
    guess = input("Enter the secret word: ")
    if guess == secret_game:
        print("congratulation!")
    else:
        allowed_try -= 1
        print(f"{'try again... ' if allowed_try > 0 else 'you lost'}, {allowed_try} tries left.")
