# Press a buton in keyboard
class Control(tk.Frame):

    def __init__(self,master=None):
        tk.Frame.__init__(self,master=None)
    def PressAnyKey(self,label):
        value = label.char
        print(value, ' A button is pressed')

app_control = Control()
app_control.master.geometry('300x150')
app_control.master.bind('<Key>', lambda i : Control().PressAnyKey(i))
app_control.master.mainloop()