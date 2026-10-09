words = {"thiago", "rodrigo", "arley"} 

def main():
    game()

def game():
    while True:
        asw = user_guess()
        if asw:
            break
        else: print("Burro pra caraio")
    print("Parabens Caralhoooooo")
        

def user_guess():
    guess = str(input("Chuta o nome de alguém da fatec: ")).strip().lower()
    if guess in words:
        return True
    else:
        return False
main()

