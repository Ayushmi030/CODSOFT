from tkinter import *

w=Tk()
w.title("Arithmetic Calculator")
w.geometry('800x200')

def calculate():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
    except:
        result_label.config(text="Please enter valid numbers.")
        return

    operation =operation_var.get()
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            result_label.config(text="Cannot divide by zero")
            return
        result = num1 / num2
    else:
        result_label.config(text="Please select an operation.")

    result_label.config(text=f"Result: {result}")

label1=Label(w,text="Number1 : ")
label1.grid(row=0,column=0,padx=10,pady=5)

entry1 = Entry(w)
entry1.grid(row=0,column=1,padx=10,pady=5)

label2=Label(w,text="Number2 : ")
label2.grid(row=1,column=0,padx=10,pady=5)

entry2 = Entry(w)
entry2.grid(row=1,column=1,padx=10,pady=5)

label3= Label(w,text="Operation: ")
label3.grid(row=2,column=0,padx=10,pady=5)

operation_var=StringVar()
operation_var.set("")

operations_frame=Frame(w)
operations_frame.grid(row=2,column=1,padx=10,pady=5)

radio_add = Radiobutton(operations_frame,text="+",variable=operation_var,value="+")
radio_add.pack(side=LEFT)

radio_subtract = Radiobutton(operations_frame,text="-",variable=operation_var,value="-")
radio_subtract.pack(side=LEFT)

radio_multiply = Radiobutton(operations_frame,text="*",variable=operation_var,value="*")
radio_multiply.pack(side=LEFT)

radio_divide = Radiobutton(operations_frame,text="/",variable=operation_var,value="/")
radio_divide.pack(side=LEFT)


submit_button=Button(w,text="Submit",command=calculate)
submit_button.grid(row=3,column=0,columnspan=2,pady=10)

result_label = Label(w,text="Result: ")
result_label.grid(row=4,column=0,columnspan=2,pady=5)

w.mainloop()
