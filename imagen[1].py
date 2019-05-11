from tkinter import *
tk =Tk()
canvas=Canvas (tk,width=1024, height=768)
canvas.pack()

my_image=PhotoImage (file="Koala.gif")
canvas.create_image(0,0, anchor=NW, image=my_image)
tk.mainloop()