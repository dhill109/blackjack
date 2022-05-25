"""
Jaspreet Singh Dhillon

"""
import time
import random
def main():
    print( f'\n{"Welcome to Black Jack":*^50}')
    while True:
        user_c1 = (random.randint(1, 10))
        user_c2 = (random.randint(1, 10))
        dealer_c1 = (random.randint(1, 10))
        dealer_c2 = (random.randint(1, 10))
        value1 = user_c1 + user_c2
        value2 = dealer_c1 + dealer_c2
        print(50 * "-")
        new_game = input("\n\nDo you wish to start a new game? (y/n): ").upper()
        if new_game == "Y":
            time.sleep(1)
            print(f"\n\nYou draw a {user_c1} and a {user_c2}. Your total is {value1}.\n")
            time.sleep(1)
            print(f"\nThe dealer draws a {dealer_c1} and a hidden card.\n")
            hos = input("\nHit or stand? (h/s): ").upper()
            while True:
                if hos == "H" and value1 < 21:
                    user_c3 = (random.randint(1, 10))
                    value1 += user_c3
                    print(f"\n\nHit! you draw a {user_c3}. Your total is {value1}.")
                    if value1 < 21:
                        hos = input("\n\nHit or stand? (h/s): ").upper()
                    continue
                elif value1 == 21 or hos == "S":
                    print("\n\nYou Stand")
                    time.sleep(2)
                    value2 = dealer_c1 + dealer_c2
                    print(f"\n\nThe dealer reveals the hidden card of {dealer_c2} and has a total of {value2}.\n")
                    while True:
                        if value2 <= 16:
                            dealer_c3 = (random.randint(1, 10))
                            value2 += dealer_c3
                            time.sleep(2)
                            print(f"\nDealer Hit! the dealer draws {dealer_c3}. The dealer's total is {value2}.\n")
                            if value2 > 21:
                                time.sleep(2)
                                print("\nDealer Busts! You win..!\n\n")
                            else:
                                continue
                        elif value2 >= 17 and value2 <= 21:
                            time.sleep(2)
                            print("\nDealer stands.\n")
                            time.sleep(2)
                            print(f"\nYou have a total of {value1} and the dealer has {value2}.\n")
                            time.sleep(2)
                            if value1<=value2:
                                print("\nDealer win!\n\n")
                                break
                            else:
                                print("\nCongrats! you win\n\n")
                                break
                        elif value2 == 21:
                            print(f"\nYour total is {value1} and the dealer\'s total is {value2}.\n")
                            time.sleep(2)
                            print("\nDealer Wins!\n\n")
                            break
                        else:
                            break
                elif value1 > 21:
                    print(f"\n\nYou have a total of {value1} and the dealer has {value2}.\n")
                    print("\nDealer win. You Bust!\n")
                    break
                else:
                    print("\nWrong Entry.\nPlease enter correct value only (h for Hit, s for Stand).\n")
                break
        elif new_game == "N":
            print("\nThanks for playing\nGood Bye...")
            print(50 * "-")
            exit()
        else:
            print("\nWrong Entry. Please enter correct value only (y for Yes/n for No).\n")
    print(50 * "-")
if __name__ == '__main__':
    main()
