'''
GUI Für das Autowerkstatt 4.0 Projekt

@author DanielNowak98

'''
import tkinter as tk
import json
from tkinter import filedialog as fd

def get_data():

    ''' Funktion zum Auslesen der Eingabefelder der GUI für:

        a = Werkstattname
        b = PLZ
        c = WerkstattID
        d = MitarbeiterID

    '''
    a = name.get()
    b = age.get()
    c = plz.get()
    d = MitarbeiterID.get()
    return a, b, c, d



def data_to_json():
    ''' Sammelt Daten aus Eingabefeldern. Diese Daten werden in ein JSON File gelegt (data)'''
    
    a,b,c,d, = get_data()

    data = {'Werkstattname':a, 
            'PLZ':b,
            'WerkstattID':c, 
            'MitarbeiterID':d,
            }

    with open('data.json', 'a') as f:
        json.dump(data, f)


def check(i,di):
    '''Checkfunktion. Diese Funktion stellt den Dictionary-Eintrag von "No" auf "Yes".'''

    if di[i] == "No":
        di [i] = "Yes"
    return di
    

def save_di_to_json(di):
    '''di - Dictionary wird im JSON Format gespeichert'''
    with open('da.json', 'a') as f:
        json.dump(di, f)


def symptome():
    '''Öffnet ein neues Fenster, in dem die Symptome zur Checkbox Auswahl liegen.'''

    window = tk.Toplevel(root)
    window.title("Symptome")
    window.geometry("600x600")

    symptome = ["Motorkonrollleuchte an", "Motor ruckelt", "Motor lässt sich nicht starten", "keine Gasannahme","Motorkonrollleuchte an", "Motor ruckelt", "Motor lässt sich nicht starten", "keine Gasannahme","Motorkonrollleuchte an", "Motor ruckelt", "Motor lässt sich nicht starten", "keine Gasannahme"]
    
    di = {}

    # Symtpome innerhalb des dictionarys werden auf "No" gesetzt.
    for i in symptome:
        di[i] = "No"
    
    # 12 Checkboxen werden in 3 Spalten gesetzt
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
    
    # Knopf um Dictionary in JSON zu speichern
    button = tk.Button(window, text="Save", command= lambda: save_di_to_json(di))
    button.grid(row = 5, column = 0)
    
    # Knopf zum schließen des Fensters
    button = tk.Button(window, text="Close", command=window.destroy)
    button.grid(row = 6, column = 0)


def select_obd_file():
    filename = fd.askopenfilename()
    print(filename)

def select_scope_file():
    filename = fd.askopenfilename()
    print(filename)

def Messungen():
    '''Öffnet ein neues Fenster, in dem die Messungen abgelegt werden.'''

    window = tk.Toplevel(root)
    window.title("Messungen")
    window.geometry("600x600")

    label = tk.Label(window, text="OBD-Protokoll")
    label.grid(row = 0, column = 0)

    button = tk.Button(window, text="OBD-Protokoll - auswählen", command=lambda: select_obd_file())
    button.grid(row = 1, column = 0)

    label = tk.Label(window, text="OBD-Protokoll")
    label.grid(row = 2, column = 0)

    label = tk.Label(window, text="Picoscope-Datei")
    button.grid(row = 3, column = 0)

    button = tk.Button(window, text="Messung auswählen", command=lambda: select_scope_file())
    button.grid(row = 1, column = 0)

    button = tk.Button(window, text="Close", command=window.destroy)
    button.grid(row = 4, column = 0)
    



''' Hauptfenster wird geöffnet und definiert'''

root = tk.Tk()
root.title("GUI")
root.geometry("600x600")

######################################## - Elemente werden innerhalb des Hauptfensters gesetzt - ########################################

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


label = tk.Label(root, text="Messungen")
label.pack()


button = tk.Button(root, text="Messungen", command=lambda: Messungen())
button.pack()


button = tk.Button(root, text="Speichern und beenden", command=lambda: data_to_json())
button.pack()


root.mainloop()