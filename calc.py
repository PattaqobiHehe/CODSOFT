from tkinter import Tk, Entry, Button, StringVar
import tkinter.messagebox

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('380x465+0+0')
        master.config(bg='#1e1e1e')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
       
        entry = Entry(master, width=20, bg='#2b2b2b', fg='white', font=('Arial', 24), textvariable=self.equation, bd=0, justify='right')
        entry.place(x=10, y=10, width=360, height=50)


        button_color = '#4d4d4d'
        button_fg = 'white'
        special_button_color = '#ff8c00'
        special_button_fg = 'black'
        hover_color = '#666666'
       
        buttons = [
            ('(', 10, 70), (')', 100, 70), ('C', 190, 70), ('⌫', 280, 70),
            ('7', 10, 130), ('8', 100, 130), ('9', 190, 130), ('÷', 280, 130),
            ('4', 10, 190), ('5', 100, 190), ('6', 190, 190), ('x', 280, 190),
            ('1', 10, 250), ('2', 100, 250), ('3', 190, 250), ('-', 280, 250),
            ('0', 10, 310), ('.', 100, 310), ('=', 190, 310, 2), ('+', 280, 310),
        ]

        for (text, x, y, *args) in buttons:
            width = args[0] if args else 1
            height = 4
            bg = special_button_color if text in ('=', 'C', '⌫') else button_color
            fg = special_button_fg if text in ('=', 'C', '⌫') else button_fg
            button = Button(master, text=text, width=10 * width, height=height, bg=bg, fg=fg, font=('Arial', 14),
                            command=lambda t=text: self.on_button_click(t))
            button.place(x=x, y=y, width=80 * width, height=50)
            button.bind("<Enter>", lambda e, b=button, c=hover_color: b.config(bg=c))
            button.bind("<Leave>", lambda e, b=button, c=bg: b.config(bg=c))
        


            #keybinding for "Enter" for solve method
        master.bind('<Return>', lambda event: self.solve())
        
            #Keybinding for "Backspace" for backspace method
        master.bind('<BackSpace>', lambda event: self.backspace())

        for key in '1234567890+-*/()':
            master.bind(key, lambda event, char=key: self.show(char))
        master.bind('.', lambda event: self.show('.'))

       
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    #Defining the Clear screen button

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set('Invalid') #Shows an Error if the function is invalid
            
    #Defining the backspace button
    def backspace(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value) 


    def on_button_click(self, char):
        if char == 'C':
            self.clear()
        elif char == '⌫':
            self.backspace()
        elif char == '=':
            self.solve()
        else:
            self.show(char)


root = Tk()
calculator = Calculator(root)
root.mainloop()
