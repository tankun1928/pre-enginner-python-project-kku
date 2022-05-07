import random
import webbrowser
import time

score = 0
name = ''

def game() :
    global name, score
    name = input("\nEnter your name : ")      #ใส่ชื่อ
    choiceList = ["a", "b", "c" ]             
    score = 0                                 #set คะเเนน
    while True :                              #กำหนดต่าตัวเเปร
        while True :                          
            print("a = hammer✊")
            print("b = paper🖐️")
            print("c = scissor✌️")
            choice = input("Please enter choice : ")      #ใส่ชื่อผู้เล่น
            if choice in choiceList :                     #ดักผู้เล่นพิมอย่างอื่น
                break                                        
            else : 
                print("\n!!! Please enter a b c !!!\n")
        comChoice = (random.choice(choiceList))           #computer random

        if choice == "a" and comChoice == "a" :           #เงื่อนไขต่างๆ
            print("✊ vs ✊")
            print("you tie")
        elif choice == "a" and comChoice == "b" :
            print("✊ vs 🖐️")
            print("you lost")
            break
        elif choice == "a" and comChoice == "c" :
            print("✊ vs ✌️")
            print("you win")
            score += 1
        elif choice == "b" and comChoice == "a" :
            print("🖐️ vs ✊")
            print("you win")
            score += 1
        elif choice == "b" and comChoice == "b" :
            print("🖐️ vs 🖐️")
            print("you tie")
        elif choice == "b" and comChoice == "c" :
            print("🖐️ vs ✌️")
            print("you lost")
            break
        elif choice == "c" and comChoice == "a" :
            print("✌️ vs ✊")
            print("you lost")
            break
        elif choice == "c" and comChoice == "b" :
            print("✌️ vs 🖐️")
            print("you win")
            score += 1
        elif choice == "c" and comChoice == "c" :
            print("✌️ vs ✌️")
            print("you tie")
        print( "\n----------  Your score : ", score, "----------\n  ")         #show score
    print("\n----------||" , name, " total score :", score, " ||---------- ")  #total score
    if score <= 2 :                                                            #เยาะเย้ยผู้เล่นเล่นเเละชม                                                                 
        print("----------||     😢  You Noob  😢    ||----------")
        print('For being noob you get PUNISHMENT!!!')
        print('Ready???')
        print('...')
        time.sleep(2)
        print('.....')
        time.sleep(3)
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ') 
        write_score()          
    else :
        print("----------||     😆  You Pro   😆    ||----------")
        write_score()

        
def write_score():
    with open('rps_scoreboard.txt', 'a') as file:
        file.write(f'{name:>12}{score:>12}\n')

def read_score():
    with open('rps_scoreboard.txt', 'r') as file:
        print(file.read())
    
        
   
def main():
    print("""
██████╗░░█████╗░░█████╗░██╗░░██╗  ██████╗░░█████╗░██████╗░███████╗██████╗░ ░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗ ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
██████╔╝██║░░██║██║░░╚═╝█████═╝░  ██████╔╝███████║██████╔╝█████╗░░██████╔╝ ╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
██╔══██╗██║░░██║██║░░██╗██╔═██╗░  ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗ ░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║ ██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝ ╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░

""")
    game()
    while True :
            score_cmd = input('Do you want to see score? (y/n): ')
            if score_cmd.lower() == 'y':
                print(f'{name:>12}{score:>12}')
            ask = input("wanna play again? (y/n): ")                    #ask player
            if ask == "y" :                                              #การตัดสินใจ play again or dont play
                game()
            elif ask == "n" :
                print()
                print("----------|| 😆 Thanks for playing😆 ||----------")
                read_score()
                break
            else : 
                print("!!! y or n !!!")

if __name__ == '__main__':
    main()