import tkinter
import random

score   = 0
colours = ['Blue','Brown','Orange','Yellow','Green','Pink','White','Black','Red','Pink','Grey','Silver','Gold']
time    = 60
def gameStart(event):
      
    if time == 60:

        timer() 
    
    main()  

def main():
    global score 
    global time
    if time > 0:

        box.focus_set
    
        if box.get().lower() == colours[1].lower():
        
            score = score + 1
    
        box.delete(0,tkinter.END)    
    
        random.shuffle(colours)
    
        color_label.config(fg = str(colours[1]), text = str(colours[0])) 
    
        score_label.config(text = "Score: " + str(score)) 


def timer():
    global time
    if time > 0: 
  
        time -= 1
        
        time_label.config(text = "Time left: " + str(time)) 
                                  
        time_label.after(1000, timer) 


root = tkinter.Tk() 
  

root.title("Games of Colors") 


root.geometry("400x400") 
  

instructions = tkinter.Label(root, text = "Type in the colour of the words, and not the word text!", font = ('Helvetica', 13)) 
instructions.pack()  
  

score_label = tkinter.Label(root, text = "Press enter to start", font = ('Helvetica', 14)) 
score_label.pack() 
  

time_label = tkinter.Label(root, text = "Time left: " +str(time), font = ('Helvetica', 12)) 
                
time_label.pack() 
  

color_label = tkinter.Label(root, font = ('Helvetica', 60)) 
color_label.pack() 
  

box = tkinter.Entry(root) 
  
 
root.bind('<Return>', gameStart) 
box.pack() 
  

box.focus_set() 
  

root.mainloop()   