from tkinter import Tk, Entry, Button, StringVar, Toplevel, Label
from fractions import Fraction

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('385x544+0+0')
        master.config(bg='#141414')
        master.resizable(False, False)
        self.master = master

        self.equation = StringVar()
        self.entry_value = ''
       
        text = Label(master, text="Calculator\nUsing Python Tkinter", font=('Tahoma', 20), fg='white', bg='#141414')
        text.place(x=0, y=0)    

        Entry(width=10, borderwidth=4,bg='#1a1a1a',fg='#ffffff', font=('Tahoma', 50), textvariable=self.equation).place(x=3, y=80)


#keybinding for "Enter" for solve method
        master.bind('<Return>', lambda event: self.solve())
#Keybinding for "Backspace" for backspace method
        master.bind('<BackSpace>', lambda event: self.backspace())
#Keybinding for "Escape" for clear method
        master.bind('<Escape>', lambda event: self.clear())


#Button Definitions

    #Bracket buttons
        Button(width=11, height=4, text='(', relief='flat', bg='#2b2b2b', fg='white',command=lambda:self.show('(')).place(x=3, y=183)
        Button(width=11, height=4, text=')', relief='flat', bg='#2b2b2b', fg='white',command=lambda:self.show(')')).place(x=91, y=183)

    #Numbers 0~9
        button_data = [
            {'text': '1', 'x': 3, 'y': 399},
            {'text': '2', 'x': 91, 'y': 399},
            {'text': '3', 'x': 179, 'y': 399},
            {'text': '4', 'x': 3, 'y': 327},
            {'text': '5', 'x': 91, 'y': 327},
            {'text': '6', 'x': 179, 'y': 327},
            {'text': '7', 'x': 3, 'y': 255},
            {'text': '8', 'x': 91, 'y': 255},
            {'text': '9', 'x': 179, 'y': 255},
            {'text': '0', 'x': 91, 'y': 471},
            ]

        for button_info in button_data:
            button = Button(
                width=11,
                height=4,
                text=button_info['text'],
                relief='flat',
                bg='#2b2b2b',
                fg='white',
                command=lambda text=button_info['text']: self.show(text)
            )
            button.place(x=button_info['x'], y=button_info['y'])


    #Arithmetic functions
        operator_data = [
            {'text': '+', 'y': 399},
            {'text': '-', 'y': 327},
            {'text': '÷', 'y': 183},
            {'text': 'x', 'y': 255},
        ]

        for operator in operator_data:
            button = Button(
                width=15,
                height=4,
                text=operator['text'],
                relief='flat',
                bg='#2b2b2b',
                fg='white',
                command=lambda operator=operator['text']: self.show(operator)
            )
            button.place(x=267, y=operator['y'])


    #Other Function buttons 
        special_button_data = [
            {'text': '.', 'x': 179, 'y': 471},
            {'text': '⌫', 'x': 179, 'y': 183},
            {'text': '=', 'x': 267, 'y': 470, 'width': 15, 'bg': 'red'},  # Specify width and color
            {'text': 'C', 'x': 3, 'y': 470, 'bg': '#ff8c00', 'fg': 'black'},  # Specify background and foreground color
        ]

        for button_info in special_button_data:
            button = Button(
                width=button_info.get('width', 11),  # Use default width if not provided
                height=4,
                text=button_info['text'],
                relief='flat',
                fg=button_info.get('fg', 'white'),  # Use default foreground color if not provided
                bg=button_info['bg'],
                command=lambda action=button_info['text']: getattr(self, action)()  # Call method based on button text
            )
            button.place(x=button_info['x'], y=button_info['y'])

    #History Button
        Button(width=2, text='↺', bg='#333333', fg='#ffffff', font=('Tahoma', 8), command=self.show_history).place(x=357, y=5)

    #Conversion button
        Button(width=10, text='Convert', bg='#333333', fg='#ffffff', font=('Tahoma', 8), command=self.convert_to_fraction).place(x=300, y=70)
        
        
    #Theme switcher button
        self.theme_mode = StringVar()
        self.theme_mode.set("🌚")  # Default theme mode
        Button(width=2, textvariable=self.theme_mode, bg='#333333', fg='#ffffff', font=('Tahoma', 8), command=self.toggle_theme).place(x=330, y=5)

#Binding Keys from 0~9
        for key in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '(', ')', '.', 'C']:
            master.bind(key, lambda event, key=key: self.show(key))
     
    def convert_to_fraction(self):
        try:
# Check if the entry value is a fraction
            if '/' in self.entry_value:
                fraction_value = Fraction(self.entry_value)
                decimal_value = fraction_value.numerator / fraction_value.denominator
            else:
                decimal_value = float(self.entry_value)
                fraction_value = Fraction(decimal_value).limit_denominator()
        
        # Toggle between fraction and decimal
            if isinstance(decimal_value, float):
                self.entry_value = str(fraction_value)
            else:
                self.entry_value = str(decimal_value)
        
            self.equation.set(self.entry_value)
        except ValueError:
           self.equation.set("Invalid")   


    def toggle_theme(self):
        current_mode = self.theme_mode.get()
        if current_mode == "🌚":  # Check if it's currently in dark mode
        # Change to light mode
            self.master.config(bg='#f0f0f0')  
            self.theme_mode.set("🌞")
            self.update_theme('#ffffff', 'black', '#cccccc', 'black', '#f0f0f0')
        else:
        # Change to dark mode
            self.master.config(bg='#141414')  
            self.theme_mode.set("🌚")
            self.update_theme('#1a1a1a', 'white', '#2b2b2b', 'white', '#141414')    


    def update_theme(self, entry_bg, entry_fg, button_bg, button_fg, calculator_bg):
    # Update colors for entry, top text, and buttons
        for child in self.master.winfo_children():
            if isinstance(child, Entry):
                child.config(bg=entry_bg, fg=entry_fg)
            elif isinstance(child, Label):
                child.config(bg=calculator_bg, fg=entry_fg)  # Adjust text and background color for the top text
            elif isinstance(child, Button) and child.cget("text") not in ['C', '=']:
                child.config(bg=button_bg, fg=button_fg, activebackground=button_bg)  # Set button background color and text color
                if button_fg == 'black':
                    child.config(fg='white')  # Ensure button text color is white for dark theme
    
    # Set background color for the calculator
        self.master.config(bg=calculator_bg)

    def show_history(self):
        history_window = Toplevel(self.master)
        history_window.title("History")
        history_window.geometry('300x200+100+100')

        history_label = Label(history_window, text="History of calculations", font=('Tahoma', 14), x=10,y=0)
        history_label.pack()

        # Here you can populate the history label with previous calculations
        # For example:
        # history = ["Calculation 1", "Calculation 2", "Calculation 3"]
        # for item in history:
        #     Label(history_window, text=item).pack()
        
        # Close button
        close_button = Button(history_window, text="Close", command=history_window.destroy)
        close_button.pack()
    
#Defining Show value 
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

#Defining the Clear screen fn i.e 'C'
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

#Defining the Solve value for '=' fn
    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set('Invalid') #Shows an Error if the function is invalid
            
#Defining the backspace for '⌫' fn 
    def backspace(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value) 

root = Tk()
calculator = Calculator(root)
root.mainloop()
