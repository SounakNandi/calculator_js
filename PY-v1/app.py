from tkinter import *

def num_function(num_input):
    if display_entry.get() == 'ERROR' or display_entry.get() == 'SYNTAX ERROR' or display_entry.get() == 'CANNOT DIVIDE BY 0':
        display_entry.delete(0,END)
    display_entry.insert(END,num_input)

sum = None
def equal_to(event):
    try:
        global sum
        sum = eval(display_entry.get())
        display_entry.delete(0,END)
        display_entry.insert(0,sum)
    except SyntaxError:
        display_entry.delete(0,END)
        display_entry.insert(0,'SYNTAX ERROR')
    except ZeroDivisionError:
        display_entry.delete(0,END)
        display_entry.insert(0,'CANNOT DIVIDE BY 0')
    except Exception as e:
        print(e)
        display_entry.delete(0,END)
        display_entry.insert(0,'ERROR')


def clear(input):
    if input=='AC':
        display_entry.delete(0,END)
    elif input=='BC':
        display_entry.delete(len(display_entry.get())-1,END)

window=Tk()
window.title('Calculator')

display_entry = Entry(window,font=('consolas',19))
display_entry.pack()

keys_frame = Frame(window)
keys_frame.pack()

number=9
for ROW in range (3):
    for COLUMN in range(3):
        Button(keys_frame,text=number, height=4,width=9,command=lambda x=number:num_function(x)).grid(row=ROW,column=COLUMN)
        number-=1
Button(keys_frame,text='/', height=4,width=9,command=lambda:num_function('/')).grid(row=0,column=3)
Button(keys_frame,text='*', height=4,width=9,command=lambda:num_function('*')).grid(row=1,column=3)
Button(keys_frame,text='AC', height=4,width=9,command=lambda:clear('AC')).grid(row=2,column=3)
Button(keys_frame,text='0', height=4,width=9,command=lambda:num_function(0)).grid(row=3,column=0)
Button(keys_frame,text='(', height=4,width=9,command=lambda:num_function('(')).grid(row=3,column=1)
Button(keys_frame,text=')', height=4,width=9,command=lambda:num_function(')')).grid(row=3,column=2)
Button(keys_frame,text='backspace', height=4,width=9,command=lambda:clear('BC')).grid(row=3,column=3)

Button(keys_frame,text='+', height=4,width=9,command=lambda:num_function('+')).grid(row=4,column=0)
Button(keys_frame,text='-', height=4,width=9,command=lambda:num_function('-')).grid(row=4,column=1)
Button(keys_frame,text='.', height=4,width=9,command=lambda:num_function('.')).grid(row=4,column=2)
Button(keys_frame,text='=', height=4,width=9,command=lambda :equal_to(None)).grid(row=4,column=3)

window.mainloop()
