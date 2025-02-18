from tkinter import *
from tkinter import ttk

root = Tk()
# root.geometry("480x640")
# root.resizable(0, 0)

def btn_click(item):
    """This function updates the input field when a button is pressed."""
    global expression
    expression += str(item)
    input_text.set(expression)
    
def btn_clear():
    """This function clears the input field when the clear button is 
    pressed."""
    global expression
    expression = ""
    input_text.set("")
    
def btn_equal():
    """This function evaluates the expression in the input field when the 
    = button is pressed."""
    global expression
    intermediate = expression.replace("^", "**")
    result = str(eval(intermediate))
    input_text.set(result)
    expression = result
    
def btn_perc():
    """This function moves the decimal place 2 places to the left when the
    % key is pressed."""
    global expression
    intermediate = expression.replace("^", "**")
    result = str(eval(intermediate + "/100"))
    input_text.set(result)
    expression = result
    
def btn_inv():
    """This function moves the decimal place 2 places to the left when the
    % key is pressed."""
    global expression
    intermediate = expression.replace("^", "**")
    result = str(eval("1/" + intermediate))
    input_text.set(result)
    expression = result
    
expression = ""

#This variable holds the value to be displayed in the input field.
input_text = StringVar()

#This frame displays the input field.
input_frame = ttk.Frame(root)
input_frame.pack(side=TOP)

#This is the input field displayed in the input frame
input_field = ttk.Entry(input_frame, font=('arial', 18, 'bold'),
                        textvariable=input_text, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10)

#This frame contains the buttons on the calculator.
btn_frame = ttk.Frame(root)
btn_frame.pack()

#Styles for special buttons
s = ttk.Style()
s.configure("C.TButton", background="red", foreground="white")
s.configure("E.TButton", background="green", foreground="white")


#The first row of buttons
clear = ttk.Button(btn_frame, text = "C", cursor = "hand2", style="C.TButton", 
                   command = lambda: btn_clear())
               
clear.grid(row = 0, column = 0, padx = 1, pady = 1)


power = ttk.Button(btn_frame, text = "^", cursor = "hand2", 
                   command = lambda: btn_click("^"))

power.grid(row = 0, column = 1, padx = 1, pady = 1)


invert = ttk.Button(btn_frame, text = "1/x", cursor = "hand2",
                     command = lambda: btn_inv())

invert.grid(row = 0, column = 2, padx = 1, pady = 1)


divide = ttk.Button(btn_frame, text = "/", cursor = "hand2",
                    command = lambda: btn_click("/"))
                
divide.grid(row = 0, column = 3, padx = 1, pady = 1)

#The second row of buttons           
seven = ttk.Button(btn_frame, text = "7", cursor = "hand2",
                   command = lambda: btn_click(7))
               
seven.grid(row = 1, column = 0, padx = 1, pady = 1)

               
eight = ttk.Button(btn_frame, text = "8", cursor = "hand2",
                   command = lambda: btn_click(8))
               
eight.grid(row = 1, column = 1, padx = 1, pady = 1)


nine = ttk.Button(btn_frame, text = "9", cursor = "hand2",
                  command = lambda: btn_click(9))
              
nine.grid(row = 1, column = 2, padx = 1, pady = 1)

              
multiply = ttk.Button(btn_frame, text = "*", cursor = "hand2",
                      command = lambda: btn_click("*"))
                  
multiply.grid(row = 1, column = 3, padx = 1, pady = 1)

#The third row of buttons
four = ttk.Button(btn_frame, text = "4", cursor = "hand2",
                  command = lambda: btn_click(4))
              
four.grid(row = 2, column = 0, padx = 1, pady = 1)

 
five = ttk.Button(btn_frame, text = "5", cursor = "hand2",
                  command = lambda: btn_click(5))
              
five.grid(row = 2, column = 1, padx = 1, pady = 1)

 
six = ttk.Button(btn_frame, text = "6", cursor = "hand2",
                 command = lambda: btn_click(6))
                 
six.grid(row = 2, column = 2, padx = 1, pady = 1)

 
minus = ttk.Button(btn_frame, text = "-", cursor = "hand2",
                   command = lambda: btn_click("-"))
               
minus.grid(row = 2, column = 3, padx = 1, pady = 1)

#The fourth row of buttons
one = ttk.Button(btn_frame, text = "1", cursor = "hand2",
                 command = lambda: btn_click(1))
             
one.grid(row = 3, column = 0, padx = 1, pady = 1)

 
two = ttk.Button(btn_frame, text = "2", cursor = "hand2",
                 command = lambda: btn_click(2))
                 
two.grid(row = 3, column = 1, padx = 1, pady = 1)

 
three = ttk.Button(btn_frame, text = "3", cursor = "hand2", 
                   command = lambda: btn_click(3))
                   
three.grid(row = 3, column = 2, padx = 1, pady = 1)

 
plus = ttk.Button(btn_frame, text = "+", cursor = "hand2",
                  command = lambda: btn_click("+"))
                  
plus.grid(row = 3, column = 3, padx = 1, pady = 1)
                  
#The fifth row of buttons               
zero = ttk.Button(btn_frame, text = "0", cursor = "hand2",
                  command = lambda: btn_click(0))
                  
zero.grid(row = 4, column = 0, padx = 1, pady = 1)

 
point = ttk.Button(btn_frame, text = ".", cursor = "hand2",
                   command = lambda: btn_click("."))
               
point.grid(row = 4, column = 1, padx = 1, pady = 1)

 
equal = ttk.Button(btn_frame, text = "=", cursor = "hand2", style="E.TButton",
                   command = lambda: btn_equal())
                   
equal.grid(row = 4, column = 3, padx = 1, pady = 1)


percent = ttk.Button(btn_frame, text = "%", cursor = "hand2",
                     command = lambda: btn_perc())

percent.grid(row = 4, column = 2, padx = 1, pady = 1)


root.mainloop()