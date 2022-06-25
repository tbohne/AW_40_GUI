''' Create a GUI with 2 text fields and a button. By klicking on the Button the text in the text field will be displayed in a message box. '''

import tkinter as tk
import json

from regex import W

def get_data():
    a = name.get()
    b = age.get()
    c = plz.get()
    d = MitarbeiterID.get()


    return a, b, c, d

def data_to_json():

    
    a,b,c,d, = get_data()

    data = {'Werkstattname':a, 
            'PLZ':b,
            'WerkstattID':c, 
            'MitarbeiterID':d,

            }

    with open('data.json', 'a') as f:
        json.dump(data, f)


def check(i,di):
    if di[i] == "No":
        di [i] = "Yes"

    return di

def save_di_to_json(di):
    with open('data.json', 'a') as f:
        json.dump(di, f)


def symptome():
    window = tk.Toplevel(root)
    window.title("Symptome")
    window.geometry("600x600")

    symptome = ["Motorkonrollleuchte an", "Motor ruckelt", "Motor lässt sich nicht starten", "keine Gasannahme","Motorkonrollleuchte an", "Motor ruckelt", "Motor lässt sich nicht starten", "keine Gasannahme","Motorkonrollleuchte an", "Motor ruckelt", "Motor lässt sich nicht starten", "keine Gasannahme"]
    
    di = {}
    for i in symptome:
        di[i] = "No"
    
    '''Create 12 checkboxes in 3 columns'''
    for i in range(0, 12):
        if i % 3 == 0:
            checkbox = tk.Checkbutton(window, text=symptome[i], variable=i, command=lambda i=symptome[i]: check(i,di))
            checkbox.grid(row=i // 3, column=0)
        elif i % 3 == 1:
            checkbox = tk.Checkbutton(window, text=symptome[i], variable=i, command=lambda i=symptome[i]: check(i,di))
            checkbox.grid(row=i // 3, column=1)
        else:
            checkbox = tk.Checkbutton(window, text=symptome[i], variable=i, command=lambda i=symptome[i]: check(i,di))
            checkbox.grid(row=i // 3, column=2)
    

    button = tk.Button(window, text="Save", command= save_di_to_json(di))
    button.grid(row = 5, column = 0)
    
    button = tk.Button(window, text="Close", command=window.destroy)
    button.grid(row = 6, column = 0)


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

label = tk.Label(root, text="WerksstattID")
label.pack()

plz = tk.Entry(root)
plz.pack()

label = tk.Label(root, text="Mitarbeiter ID")
label.pack()

MitarbeiterID = tk.Entry(root)
MitarbeiterID.pack()


label = tk.Label(root, text="Symptome")
label.pack()




button = tk.Button(root, text="Symptome", command=lambda: symptome())
button.pack()

button = tk.Button(root, text="Speichern und beenden", command=lambda: data_to_json())
button.pack()

root.mainloop()




