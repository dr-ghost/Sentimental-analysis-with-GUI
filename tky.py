from tkinter import *
z=Tk()
####FRAME 1
frame=LabelFrame(z)
frame.pack(side="top",expand=True,fill="both")
frame.configure(bg="lavender")
dest=Button(frame,text="EXIT",font=("impact"),fg="royal blue",bg="lavender",command=z.destroy)
dest.place(relx=0.5,rely=1.0,anchor="s")
frameser=LabelFrame(frame)
search=Entry(frameser,width=20,font=("century gothic",25),fg="grey")
search.insert(0,"Search")
senti=search.get()
def btsent():
    return
e=Entry(frame,width=20,font=("century gothic",25),fg="grey")
searchb=Button(frameser,text="SEARCH",fg="royal blue",bg="lavender",font="impact")
frameser.pack()
e.pack()
search.grid(row=1,column=2)
searchb.grid(row=1,column=3)
z.mainloop()
