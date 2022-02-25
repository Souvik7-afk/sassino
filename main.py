import datetime 
import pyttsx3
import speech_recognition as sr 
from tkinter import *
import random

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=2
        audio=r.listen(source)
    try:
        print("recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"you said : {query}") 
        #speak("you said ",query)
    except Exception as Error:
        print("sorry sir, i dont understand..")
        return "None"
    return query

def rockpaper():
    

    root = Tk()
    root.title("ROCK, PAPER, SCISSOR GAME")
    width = 690
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    root.config(bg="green")

# ++++++++++++++++++++IMAGES++++++++++++++++++++++++++
    blank_image = PhotoImage(file="resources/blank.png")
    rock_player = PhotoImage(file="resources/rock_player.png")
    rock_player_ado = rock_player.subsample(3, 3)
    paper_player = PhotoImage(file="resources/paper_player.png")
    paper_player_ado = paper_player.subsample(3, 3)
    scissor_player = PhotoImage(file="resources/scissor_player.png")
    scissor_player_ado = scissor_player.subsample(3, 3)
    rock_computer = PhotoImage(file="resources/rock_computer.png")
    paper_computer = PhotoImage(file="resources/paper_computer.png")
    scissor_computer = PhotoImage(file="resources/scissor_computer.png")


# ++++++++++++++++++++METHODS++++++++++++++++++++++++++
    def Rock():
        global player_option
        player_option = 1
        player_image.configure(image=rock_player)
        MatchProcess()


    def Paper():
        global player_option
        player_option = 2
        player_image.configure(image=paper_player)
        MatchProcess()


    def Scissor():
        global player_option
        player_option = 3
        player_image.configure(image=scissor_player)
        MatchProcess()


    def MatchProcess():
        computer_option = random.randint(1, 3)
        if computer_option == 1:
            computer_image.configure(image=rock_computer)
            RockCom()

        elif computer_option == 2:
            computer_image.configure(image=paper_computer)
            PaperCom()

        elif computer_option == 3:
            computer_image.configure(image=scissor_computer)
            ScissorCom()


    def RockCom():
        if player_option == 1:
            status_label.config(text="Game Tie")
        elif player_option == 2:
            status_label.config(text="Player Win")
        elif player_option == 3:
            status_label.config(text="Computer Win")


    def PaperCom():
        if player_option == 1:
            status_label.config(text="Computer Win")
        elif player_option == 2:
            status_label.config(text="Game Tie")
        elif player_option == 3:
            status_label.config(text="Player Win")


    def ScissorCom():
        if player_option == 1:
            status_label.config(text="Player Win")
        elif player_option == 2:
            status_label.config(text="Computer Win")
        elif player_option == 3:
            status_label.config(text="Game Tie")


    def ExitApplication():
        root.destroy()
        exit()


    # ++++++++++++++++++++LABEL WIDGET++++++++++++++++++++++++++
    player_image = Label(root, image=blank_image)
    computer_image = Label(root, image=blank_image)
    player_label = Label(root, text="PLAYER")
    player_label.grid(row=1, column=1)
    player_label.config(bg="blue", fg="white", font=('Times New Roman', 12, 'bold'))
    computer_label = Label(root, text="COMPUTER")
    computer_label.grid(row=1, column=3)
    computer_label.config(bg="blue", fg="white", font=('Times New Roman', 12, 'bold'))
    status_label = Label(root, text="", font=('Times New Roman', 12))
    status_label.config(bg="white", fg="red", font=('Times New Roman', 20, 'bold'))
    player_image.grid(row=2, column=1, padx=30, pady=20)
    computer_image.grid(row=2, column=3, pady=20)
    status_label.grid(row=3, column=2)

    # ++++++++++++++++++++BUTTON WIDGET++++++++++++++++++++++++++
    rock = Button(root, image=rock_player_ado, command=Rock)
    paper = Button(root, image=paper_player_ado, command=Paper)
    scissor = Button(root, image=scissor_player_ado, command=Scissor)
    button_quit = Button(root, text="Quit", bg="Blue", fg="white", font=('Times New Roman', 18, 'bold'), command=ExitApplication)
    rock.grid(row=4, column=1, pady=30)
    paper.grid(row=4, column=2, pady=30)
    scissor.grid(row=4, column=3, pady=30)
    button_quit.grid(row=5, column=2)

    # ++++++++++++++++++++INITIALIZATION++++++++++++ ++++++++++++++
    if __name__ == '__main__':
        root.mainloop()  


speak("say the usename you want to use during the gameplay")
query=takecommand().lower()
speak("welcome abord"+ query)
speak("Hope you enjoy the games. best of luck")


if __name__=="__main__":
    
    #speak("1st game is the egg catcher game. to play this say egg catcher")
    #speak("2nd game is the fidget spinner game. to play this say fidget spinner")
    #speak("3rd game is the screen pet game. to play this say screen pet")
    #speak("4th game is the tic tac toe game. to play this say tic tac toe")
    #speak("5th game is the turtle game. to play this say turtle")
    #speak("6th game is the dots and boxes. to play this say dot")
    #speak("7th game is the rock,paper & scissors game. to play this say rock")
    #speak("8th game is the colours game. to play this say colour ")
    #speak("9th game is the  memory game. to play this say memory")
    #speak("10th game is the tiles game. to play this say tiles")
    #speak("11th game is the dodge game. to play this say dodge")
    #speak("12th game is the snake game. to play this say snake")
    #speak("13th game is the word guess game. to play this say word")
    #speak("14th game is the stack game. to play this say stack")
    #speak("15th game is the balloon game. to play this say balloon")
    #speak("last game is the dino game. to play this say dino")


    speak("say which one you want to play")
    query=takecommand().lower()
    
    if "egg" in query:
        import egg_catcher_game 
    elif "spinner" in query:
        import fidget_spinner_game 
    elif "blush" in query:
        import screen_pet 
    elif "toe" in query:
        import tic_tac_toe_game 
    elif "turtle" in query:
        import turtle_game 
    elif "dot" in query:
        import dots_boxes
    elif "rock" in query:
        rockpaper()
    elif "colours" in query:
        import Colors
    elif "memory" in query:
        import Memory
    elif "tiles" in query:
        import Tiles
    elif "dodge" in query:
        import Dodge
    elif "snake" in query:
        import snake_and_apple
    elif "guess" in query:
        import Guess_the_word
    elif "stack" in query:
        import stack
    elif "balloon" in query:
        import Balloon
    elif "dino" in query:
        import dino
    else:
        speak("game does not exist. sorry sir")