import modules


print("\nHello, what is your name?")
myName = input()
print(f"\nWelcome {myName}, please select a menu between 1-3:")


def main():
    choose_menu = input()
    if choose_menu == "1":
        modules.divisible_list()
    elif choose_menu == "2":
        modules.guess_number()
    elif choose_menu == "3":
        modules.exit()
        quit()


modules.head_menu()
