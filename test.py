''' Create a GUI with 2 text fields and a button. By klicking on the Button the text in the text field will be displayed in a message box. '''

import tkinter as tk
import json

def get_data():
    a = name.get()
    b = age.get()
    c = plz.get()
    d = MitarbeiterID.get()


    return a, b, c, d

def data_to_json():

    
    a,b,c,d, = get_data()

    data = {'a':a, 
            'b':b,
            'c':c, 
            'd':d,

            }

    with open('data.json', 'w') as f:
        json.dump(data, f)

root = tk.Tk()
root.title("GUI")
root.geometry("600x600")

label = tk.Label(root, text="Werkstattname")
label.pack()

name = tk.Entry(root)
name.pack()

label = tk.Label(root, text="PLZ")
label.pack()

age = tk.Entry(root)
age.pack()

label = tk.Label(root, text="PLZ")
label.pack()

plz = tk.Entry(root)
plz.pack()

label = tk.Label(root, text="Mitarbeiter ID")
label.pack()

MitarbeiterID = tk.Entry(root)
MitarbeiterID.pack()


label = tk.Label(root, text="Symptome")
label.pack()

''' Create new window'''
def new_window():
    window = tk.Toplevel(root)
    window.title("Symptome")
    window.geometry("600x600")

    'create 12 checkbuttons'
    for i in range(50):
        checkbutton = tk.Checkbutton(window, text="Checkbox " + str(i))
        checkbutton.pack()

    
    button = tk.Button(window, text="Close", command=window.destroy)
    button.pack()



button = tk.Button(root, text="Symptome", command=lambda: new_window())
button.pack()

root.mainloop()




