from tkinter import *
from tkinter import messagebox  # extra import statement for messagebox is needed!!!

import json
from difflib import get_close_matches

def EngDict():
    data = json.load(open('data.json'))

    word = word_input.get().lower()
    t_output.delete(1.0, END)

    if word in data.keys():
        result = '\n\nOr:\n\n'.join(data[word])
        return t_output.insert(END, result)

    elif word.title() in data.keys():
            result = '\n\nOr:\n\n'.join(data[word.title()])
            return t_output.insert(END, result)

    elif word.upper() in data.keys():
            result = '\n\nOr:\n\n'.join(data[word.upper()])
            return t_output.insert(END, result)

    elif get_close_matches(word, data.keys(), cutoff=0.8) != []:
        matchlist = get_close_matches(word, data.keys(), n=5, cutoff=0.8)
        m = 0
        YorN_list = []
        while m < len(matchlist):
            match = matchlist[m]
            # messagebox function can only be used when defining a function   # messagebox.askyesno() function returns either 1 or 0
            YorN = messagebox.askyesno('Possible Matches Found', 'Did you mean {} instead? Enter Y if yes, or N if no: '.format(match))
            YorN_list.append(YorN)
            if YorN == 1:
                result = '\n\nOr:\n\n'.join(data[match])
                return t_output.insert(END, result)
                break
            else:
                m = m + 1
                continue

        if YorN_list[-1] == 0:
            return messagebox.showerror('Error', 'The word does not exist. Please double check it.')

    else:
        return messagebox.showerror('Error', 'The word does not exist. Please double check it.')


window = Tk()

lbl1 = Label(window, text = 'Enter word:', width = 20)
lbl1.grid(row=1, column=0)
lbl1.configure(font = ('roboto', 10, 'bold')) #use .configure() to change the font style and font size

word_input = StringVar()
e = Entry(window, textvariable = word_input, width = 35)
e.grid(row=1, column=1)
e.configure(font = ('roboto', 12))

b1 = Button(window, text = 'Search', command = EngDict)
b1.grid(row=1, column=2)
b1.configure(font = ('roboto', 10, 'bold'))

lbl2 = Label(window, text = 'Result:')
lbl2.grid(row=3, column=0)
lbl2.configure(font = ('roboto', 10, 'bold'))

t_output = Text(window, height = 30, width = 60)
t_output.grid(row=3, column=1, columnspan = 2)
t_output.configure(font = ('comic sans ms', 12))


lbl2_ws = Label(window, text = ' ')
lbl2_ws.grid(row=0, column=0, columnspan=3)

lbl1_ws = Label(window, text = ' ')
lbl1_ws.grid(row=2, column=0, columnspan=3)

lbl3_ws = Label(window, text = ' ', width = 2)
lbl3_ws.grid(row=0, column=3, rowspan=4)

lbl4_ws = Label(window, text = ' ')
lbl4_ws.grid(row=4, column=0, columnspan=3)

window.mainloop()
