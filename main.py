from tkinter import *
import random
from tkinter import messagebox
from PIL import Image, ImageTk
#Defining Variables.
user_list = [] #List used to append names in results pages.
asked = [] #List used to append the questions.

#Dictionary that contains the keys and values of questions 1-10.
question_bank = {
  1:["Which word in the dictionary is spelled incorrectly?", #item 1, index 0 will be the questions
      'a. temparature', #item 2, index 1 will be the first choice
      'b. damged', #item 3, index 2 will be the second choice
      'c. incorrectly', #item 4, index 3 will be the third choice
      'd. focus' #item 4, index 4 will be the write statement we need to display the right statement if the user eneters wrong choice
      ,3] #item 7, index 5 will be the position of the right answer index where right answer sits), this will be our check if answer correct or no
  
 ,2:["Which of the following can be arranged into a English word?",
      'a. H R G S T',
      'b. R I L S A',
      'c. T O O M T',
      'd. W Q R G S'
      ,2]
  
 ,3:["The day before, the day before yesterday after Saturday. What day is it today?",
      'a. Thursday',
      'b. Friday',
      'c. Sunday',
      'd. Saturday'
      ,2]
    
 ,4:["When counting from 1-100, how many times will you come across the number 7?",
      'a. 18',
      'b. 19',
      'c. 20',
      'd. 21'
      ,3]
        
 ,5:["What's the 9th shape going to be?",
      'a.',
      'b.',
      'c.',
      'd.'
      ,2]
    
 ,6:["If you rearrange the letter “CIFAIPC” you would have the name of an:",
      'a.City',
      'b.Animal',
      'c.Ocean',
      'd.River'
      ,3]
   
 ,7:["Which one of the five is least like the other four?",
      'a.Dog',
      'b.Mouse',
      'c.Lion',
      'd.Snake'
      ,4]
  
 ,8:["What's next?",
      'a.',
      'b.',
      'c.',
      'd.'
      ,3]
  
 ,9:["What's the next pattern?",
      'a.',
      'b.',
      'c.',
      'd.'
      ,2]
  
 ,10:["What word is the opposite of happy",
      'a.unfortunate',
      'b.lucky',
      'c.joyful',
      'd.contended'
      ,1]
}

def ran():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    ran()
#main page
class Start:
  def __init__(self, parent):
    self.img_file = Image.open("333.png")                  
    self.img_file.resize((700,600))
    self.img_file = ImageTk.PhotoImage(self.img_file)
   
    self.b1 = Button(parent,image=self.img_file, border = 0, command = self.inst)
    self.b1.place(x=268,y=450)
   
  def inst(self):
   self.b1.destroy()
   Name(window)

    #name page
class Name:
  def __init__(self, parent):
    self.quiz_frame = Frame(parent, bg="purple")
    self.quiz_frame.pack(fill="both", expand=1)
    self.heading_label = Label(self.quiz_frame, text = "Intelligence Quiz", font = ("Tw Cen", "18", "bold"), bg = "purple")
    self.heading_label.grid(row = 2)
    self.user_label = Label ( self.quiz_frame, text = "Please enter your name below",  font = ("Tw Cen", "16"), bg = "purple")
    self.user_label.grid(row = 3, padx= 70, pady = 20)
	 
    self.entry_box = Entry(self.quiz_frame)
    self.entry_box.grid(row = 4, pady = 20)

    self.continue_button = Button (self.quiz_frame, text = "Continue", bg = "darkseagreen1", command=self.name_collection)
    self.continue_button.grid(row = 5, pady = 20)

    
  
  
    #Name Colection which checks if .
  def name_collection(self):
      name=self.entry_box.get()
      #This is used to make sure the characters entered by the user are string variables and less than 10 characters.
      if str.isalpha(name) == True and len(name) >0 and len(name) <=5:
        user_list.append(name)
        self.quiz_frame.destroy() #destroy the starter
        Question(window)
        
      elif str.isalpha(name) == False and len(name) >0:
        #Error messages pop up in a message box (imported technique) when incorrect values are collected from the user.
        messagebox.showerror("Name error:", "Please check that you are only using letters and no other characters or numerals.")
      elif len(name) <1:
        messagebox.showerror("Name error:", "Please check that you have entered a name.")
      elif len(name) >5:
        messagebox.showerror("Name error:", "Please check that you have entered a name up to  characters.")
      

  
class Question:
  def __init__(self, parent):
      #Setting up the frame.
      self.quiz_frame = Frame(parent)
      window.geometry("1050x600") #Geometry used to create a fixed window size/window dimensions.
      self.quiz_frame.pack(fill = "both", expand = True) #So that place technique can work.

      ran() #Method to randomise the questions.

      self.value=IntVar() #Holds the value of radio buttons.

#Setting the file image as the background.
      self.bg_image = Image.open("purple.png") 
      self.bg_image = ImageTk.PhotoImage(self.bg_image)      
      self.bg_label = Label(self.quiz_frame, image = self.bg_image)
      self.bg_label.place(x = 0, y = 0) #Make label fit the parent window always

#Question label that is configured to say different questions in the dictionary keys.
      self.question_label = Label(self.quiz_frame, text = "Q: " + question_bank[qnum][0], font = ("Helvitica","16", "bold"), foreground = 'white', bg = '#FFD700', highlightbackground = 'white', pady = 5, width = 52, highlightthickness = 2, wraplength = 700) #Attributes.
      self.question_label.place(x = 200, y = 40) #Widget Placement.

      #Radio buttons are configured to be the answers of each question and hold values of those options in the dictionary keys.
      #Option 1 button.
      self.option1 = Radiobutton(self.quiz_frame, text = question_bank[qnum][1], font = ("Helvetica","12", "bold"), foreground = 'white', value = 1, padx = 5, pady = 5, variable = self.value, background = "#FFD700", activebackground = 'light gray',  indicatoron = 0, selectcolor = 'light gray', highlightbackground = '#d8e9da', highlightthickness = 2, relief = RAISED, justify = "left", width = 35, height = 6, wraplength = 300) #Attributes.
      self.option1.place(x = 200, y = 160) #Widget Placement.

      #Option 2 button.
      self.option2 = Radiobutton(self.quiz_frame, text = question_bank[qnum][2], font = ("Helvetica","12", "bold"), foreground = 'white', value = 2, padx = 5, pady = 5, variable = self.value, background = "#FFD700", activebackground = 'light gray',  indicatoron = 0, selectcolor = 'light gray', highlightbackground = '#d8e9da',  highlightthickness = 2, relief = RAISED, justify = "left", width = 35, height = 6, wraplength = 300) #Attributes.
      self.option2.place(x = 600, y = 160) #Widget Placement.

      #Option 3 button.
      self.option3 = Radiobutton(self.quiz_frame, text = question_bank[qnum][3], font = ("Helvetica","12", "bold"), foreground = 'white', value = 3, padx = 5, pady = 5, variable = self.value, background = "#FFD700", activebackground = 'light gray',  indicatoron = 0, selectcolor = 'light gray', highlightbackground = '#d8e9da', highlightthickness = 2, relief = RAISED, justify = "left", width = 35, height = 6, wraplength = 300) #Attributes.
      self.option3.place(x = 200, y = 340) #Widget Placement.

      #Option 4 button.
      self.option4 = Radiobutton(self.quiz_frame, text = question_bank[qnum][4], font = ("Helvetica","12", "bold"), foreground = 'white', value = 4, padx = 5, pady = 5, variable = self.value, background = "#FFD700", activebackground = 'light gray',  indicatoron = 0, selectcolor = 'light gray', highlightbackground = '#d8e9da', highlightthickness = 2, relief = RAISED, justify = "left", width = 35, height = 6, wraplength = 300) #Attributes.
      self.option4.place(x = 600, y = 340) #Widget Placement.

      #Question counter label.
      self.questioncounter_label = Label(self.quiz_frame, text = "Q Num: ", font = ("Helvetica", "14", "bold"), highlightbackground = 'white', highlightthickness = 2, pady = 5, padx = 5) #Attributes.
      self.questioncounter_label.place(x = 20, y = 180) #Widget Placement.

      #QNumber calculated label.
      self.qnumber_label = Label(self.quiz_frame, text = 1, font = ("Helvetica", "14", "bold"), highlightbackground = 'white', highlightthickness = 2, pady = 5, padx = 5) #Attributes.
      self.qnumber_label.place(x = 120, y = 180) #Widget Placement.

      #Score label.
      self.score_label = Label(self.quiz_frame, text = "TOTAL SCORE", font = ("Helvetica", "14", "bold"), pady = 5) #Attributes.
      self.score_label.place(x = 20, y = 280) #Widget Placement.

      #Calculated Score label.
      self.numberscore_label = Label(self.quiz_frame, text = 0, font = ("Helvetica", "16", "bold"), pady = 5) #Attributes.
      self.numberscore_label.place(x = 85, y = 310) #Widget Placement.

      #Answertext label
      self.answertext_label = Label(self.quiz_frame, text = "....", font = ("Helvetica", "14", "bold"),pady = 5, justify = 'center', wraplength = 480) #Attributes.
      self.answertext_label.place(x = 360, y = 480) #Widget Placement.

      #Exit to menu button.
      self.exit_button = Button(self.quiz_frame, text = "EXIT TO MENU", font = ("Helvetica", "14", 'bold'), foreground = 'white', bg = '#F07470', pady = 10, width = 15, highlightthickness = 2, highlightbackground = 'black',  activebackground = '#DC1C13', command = self.exit) #Attributes.
      self.exit_button.place(x = 20, y = 530) #Widget Placement.

      #Next button.
      self.next_button = Button(self.quiz_frame, text = "NEXT", font = ("Helvetica", "14", 'bold'), foreground = 'white', bg = '#D9EAD3', pady = 10, width = 10, highlightthickness = 2, highlightbackground = 'black',  activebackground = '#649568', command = self.score_bank) #Attributes.
      self.next_button.place(x = 500, y = 530) #Widget Placement.

      #Creating instances of score variable and question number variable to be used through the classes.
      self.score = 0
      self.question_number = 1

  #Method to exit the page and transfer back to menu page.
  def exit(self):
      self.score = 0
      self.question_number = 0
      self.quiz_frame.destroy()
      Start(window)

  #Question setup.
  def question_switch(self):
      ran() #Randomises questions.
      self.value.set(0) #Sets value to 0.
      self.question_label.config(text = "Q: " + question_bank[qnum][0]) #Configure question label to be the question in a key from dictionary.
      self.option1.config(text = question_bank[qnum][1]) #Radio button options become the answers from a key in dictionary.
      self.option2.config(text = question_bank[qnum][2])
      self.option3.config(text = question_bank[qnum][3])
      self.option4.config(text = question_bank[qnum][4])

  #Score calculations.
  def score_bank(self):
      #Instance labels of classes are equal to a variable name so I can configure the texts easily.
      total_score = self.numberscore_label
      option_choice = self.value.get()
      answer_text = self.answertext_label
      question_counter = self.qnumber_label
      if len(asked)>9: #If the last question (10th) is asked.
        if option_choice == question_bank[qnum][5]: #If last question is right answer.
          self.score += 1 #Add to score if answer right.
          self.question_number += 1 #Add to question number.
          total_score.configure(text = self.score) #Configures the score label to the new score.
          question_counter.configure(text = self.question_number, foreground = 'black') #Configures question number label to next question number.
          answer_text.configure(text = "Correct!", foreground = 'green') #Configures the answer label to say correct when user selects right answer.
          self.endResults() #Calls the method to set up the file for scoreboard.
        else: #If last question was wrong answer.
          self.score += 0 #No value added to score because answer was incorrect.
          self.question_number += 1
          total_score.configure(text = self.score)
          question_counter.configure(text = self.question_number, foreground = 'black')
          answer_text.configure(text = "Incorrect: \n" + question_bank[qnum][6], foreground = 'red') #Configure answer text to say user is incorrect and why.
          self.endResults()
      else:
        if option_choice == 0: #Check if user made a choice.
          answer_text.config(text = "Sorry you didn't select anything, please retry", foreground = 'red')
        else: #If they made choice that isn't last question.
          if option_choice == question_bank[qnum][5]: #If user is right.
            self.score += 1
            self.question_number += 1
            total_score.configure(text = self.score)
            question_counter.configure(text = self.question_number, foreground = 'black')
            answer_text.configure(text = "Correct!", foreground = 'green')
            self.question_switch() #Run method for next question to come up.
          else: #If the user chooses wrong answer.
            self.score += 0
            self.question_number += 1
            total_score.configure(text = self.score)
            question_counter.configure(text = self.question_number, foreground = 'black')
            answer_text.configure(text = "Incorrect: \n" + question_bank[qnum][6], foreground = 'red')
            self.question_switch()


  
if __name__== "__main__":
    window = Tk()
    window.title("IQ Quiz")
    window.geometry("700x600")
    bg_image = Image.open("startpage1.png")
    bg_image = bg_image.resize((700,600),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = Start(window)
    window.mainloop()





