from tkinter import *
# Ereignisverarbeitung

def verarbeiten(event):
    listeAusgewaehlt = listboxNamen.curselection()
    itemAusgewaehlt = listeAusgewaehlt[0]
    nameAusgewaehlt = listboxNamen.get(itemAusgewaehlt) 
    textBegruessung = 'Hallo ' + nameAusgewaehlt +'!'
    labelText.config(text=textBegruessung)
    
# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Test')
tkFenster.geometry('120x125')
# Rahmen Listbox
frameListbox = Frame(master=tkFenster, bg='#FFCFC9')
frameListbox.place(x=5, y=5, width=110, height=80)
# Rahmen Ausgabe
frameAusgabe = Frame(master=tkFenster, bg='#D5E88F')
frameAusgabe.place(x=5, y=90, width=110, height=30)
# Listbox
listboxNamen = Listbox(master=frameListbox, selectmode='browse')
listboxNamen.insert('end', 'Anna')
listboxNamen.insert('end', 'Bernd')
listboxNamen.insert('end', 'Clara')
listboxNamen.insert('end', 'Dominik')
listboxNamen.place(x=5, y=5, width=100, height=70)
listboxNamen.bind('<<ListboxSelect>>', verarbeiten)
# Label Text
labelText = Label(master=frameAusgabe, bg='white')
labelText.place(x=5, y=5, width=100, height=20)
# Aktivierung des Fensters
tkFenster.mainloop()








