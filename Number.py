import tkinter as tk
root=tk.Tk()
root.title('Number Converter')
root.geometry('700x600+50+50')
opt=tk.IntVar()
opt1=tk.IntVar()
x=tk.StringVar()
def inp():
    
    global final
    global f
    
    if(opt.get()==1):
        f=int(x.get(),2)
        if(opt1.get()==1):
            final=x.get()
            ansa.config(text=final)
            exp='Input-->Output\nInput and output both will be same.'
            label.config(text=exp)
        if(opt1.get()==2):
            final=oct(f).replace('0o','')
            ansb.config(text=final)
            exp='Input-->Output\nWe have to split the binary numbers\ninto groups of three elements.\nEach grouped elements written as a single \nunit in octal number.'
            label.config(text=exp)
        if(opt1.get()==3):
            final=f
            ansc.config(text=final)
            exp='Input-->Output\nFrom right to left corresspondingly\nto binary number 2^n is taken\nwhere n=0,1,2,3...\nthe number is conrresspondingly added \nwhich having 1 value in binary.'
            label.config(text=exp)
        if(opt1.get()==4):
            final=hex(f).replace('0x','')
            ansd.config(text=final)
            exp='Input-->Output\nWe have to split the binary numbers\ninto groups of four elements.\nEach grouped elements written as a single \nunit in Hexadecimal number.'
            label.config(text=exp)
            
    if(opt.get()==2):
        f=int(x.get(),8)
        if(opt1.get()==1):
            final=bin(f).replace('0b','')
            ansa.config(text=final)
            exp='Step 1 − Convert each octal digit to a \n3-digit binary number (the octal digits \nmay be treated as decimal for this conversion). \nStep 2 − Combine all the resulting binary \ngroups (of 3 digits each) into a \nsingle binary number..'
            label.config(text=exp)
        if(opt1.get()==2):
            final=x.get()
            ansb.config(text=final)
            exp='Input-->Output\nInput and output both will be same.'
            label.config(text=exp)
        if(opt1.get()==3):
            final=f
            ansc.config(text=final)
            exp="Start the decimal result at 0.\nRemove the most significant octal \ndigit (leftmost) and add it to the result.\nIf all octal digits have been \nremoved, you're done. Stop.\nOtherwise, multiply the result by 8.\nGo to step 2."
            label.config(text=exp)
        if(opt1.get()==4):
            final=hex(f).replace('0x','')
            ansd.config(text=final)
            exp="Step 1: Let the number of digits\n in the number be n \nStep 2: Multiply the digits with 8n-1where n \nis position of digit from the right \nend of the number.If the number has decimal\npart the multiply digits after decimal \nby 1/8^m where m is position of the \nnumber from the decimal."
            label.config(text=exp)
    if(opt.get()==3):
        f=int(x.get())
        if(opt1.get()==1):
            final=bin(f).replace('0b','')
            ansa.config(text=final)
            exp="Set up the problem. For this example, \nlet's convert the decimal number \n15610 to binary. ...Divide. ...\nContinue to divide until you reach 0. ...\nWrite out the new, binary number."
            label.config(text=exp)
        if(opt1.get()==2):
            final=oct(f).replace('0o','')
            ansb.config(text=final)
            exp='Divide the decimal number by the \ndesired target radix (2, 8, or 16).\nAppend the remainder as \nthe next most significant digit.\nRepeat until the decimal number \nhas reached zero..'
            label.config(text=exp)
        if(opt1.get()==3):
            final=str(f)
            ansc.config(text=final)
            exp='Input-->Output\nInput and output both will be same.'
            label.config(text=exp)
        if(opt1.get()==4):
            final=hex(f).replace('0x','')
            ansd.config(text=final)
            exp='We have to write binary number in a group\n of four elements for each decimal digit.'
            label.config(text=exp)
    if(opt.get()==4):
        f=int(x.get(),16)
        if(opt1.get()==1):
            final=bin(f).replace('0b','')
            ansa.config(text=final)
            exp='We have to write binary number in a group\n of four elements for each hexadecimal digit.'
            label.config(text=exp)
        if(opt1.get()==2):
            final=oct(f).replace('0o','')
            ansb.config(text=final)
            exp='We have to first convert it into binary\nThen make groups of three elements from\nbinary.'
            label.config(text=exp)
        if(opt1.get()==3):
            final=f
            ansc.config(text=final)
            exp='We have to first convert it into binary\nThen binary will be converted into decimal.'
            label.config(text=exp)
        if(opt1.get()==4):
            final=hex(f).replace('0x','')
            ansd.config(text=final)
            exp='Input-->Output\nInput and output both will be same.'
            label.config(text=exp)
        
        
tk.Label(relief='groove').place(relx=0.01,rely=0.01,height=150,width=550)
l1=tk.Label(text='Enter a Number')
l1.grid(row=5,column=0,padx=20,pady=10)
tk.Entry(textvariable=x).grid(row=5,column=1,padx=0)
r1=tk.Radiobutton(text='Binary',value=1,variable=opt,command=inp)
r1.grid(row=6,column=0,padx=20,sticky='W')
r2=tk.Radiobutton(text='Octal',value=2,variable=opt,command=inp)
r2.grid(row=7,column=0,padx=20,sticky='W')
r3=tk.Radiobutton(text='Decimal',variable=opt,value=3,command=inp)
r3.grid(row=8,column=0,padx=20,sticky='W')
r4=tk.Radiobutton(text='Hexadecimal',variable=opt,value=4,command=inp)
r4.grid(row=9,column=0,padx=20,sticky='W')
l8=tk.Label(text='Number to be converted in:')
l8.grid(row=5,column=3,padx=40,sticky='w')
s1=tk.Radiobutton(text='Binary',variable=opt1,value=1,command=inp)
s1.grid(row=6,column=3,padx=45,sticky='w')
s2=tk.Radiobutton(text='Octal',variable=opt1,value=2,command=inp)
s2.grid(row=7,column=3,padx=45,sticky='w')
s3=tk.Radiobutton(text='Decimal',variable=opt1,value=3,command=inp)
s3.grid(row=8,column=3,padx=45,sticky='w')
s4=tk.Radiobutton(text='Hexadecimal',variable=opt1,value=4,command=inp)
s4.grid(row=9,column=3,padx=45,sticky='w')

tk.Label(relief='groove').place(relx=0.01,rely=0.3,height=150,width=270)
l2=tk.Label(text='Result:')
l2.place(y=170,x=20)
l3=tk.Label(text='Binary :').place(y=210,x=30)
ansa=tk.Label(relief='groove')
ansa.place(y=210,x=110,height=20,width=150)
l4=tk.Label(text='Octal : ').place(y=235,x=30)
ansb=tk.Label(relief='groove')
ansb.place(y=235,x=110,height=20,width=150)
l5=tk.Label(text='Decimal : ')
l5.place(y=260,x=30)
ansc=tk.Label(relief='groove')
ansc.place(y=260,x=110,height=20,width=150)
l6=tk.Label(text='Hexadecimal : ').place(y=285,x=30)
ansd=tk.Label(relief='groove')
ansd.place(y=285,x=110,height=20,width=150)

tk.Label(relief='groove').place(relx=0.4,rely=0.3,height=150,width=280)
l7=tk.Label(text='Explanation:')
l7.place(y=170,x=290)
label=tk.Label(fg='blue')
label.place(x=300,y=190)

root.mainloop()
