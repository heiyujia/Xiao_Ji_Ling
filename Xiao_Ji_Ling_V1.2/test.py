
import tkinter as tk
#创建listbox    
#
root = tk.Tk()    
user_listbox=tk.Listbox(root,font=('',14))
value = ['1','2','as','12','123','asd','1','2','as','12','123','asd','1','2','as','12','123','asd','1','2','as','12','123','asd']
for item in value:
    user_listbox.insert(tk.END, item)        
 
user_listbox.place(x=5,y=10,relwidth=0.9,relheight=0.9)
 
#创建Scrollbar
yscrollbar = tk.Scrollbar(user_listbox,command=user_listbox.yview)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

user_listbox.config(yscrollcommand=yscrollbar.set)

root.mainloop()
