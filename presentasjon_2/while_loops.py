secret = "python"
guess = ""

print("Gjett ordet! (skriv 'quit' for å avslutte)")

while guess != secret:
    guess = input("Skriv gjetning: ")

    if guess == "quit":
        print("Du avsluttet spillet.")
        break
    elif guess == secret:
        print("Riktig! Du vant!")
    else:
        print("Feil, prøv igjen...")

