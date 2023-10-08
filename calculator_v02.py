import tkinter as tk 
calculation =""

def add_to_calculation(symbol):
    global calculation 
    calculation += str(symbol)
    text_result.delete(1.0, "end") 
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")

root=tk.Tk()
root.geometry("309x326")
text_result=tk.Text(root, height=2, width=16, font=("Times 28 italic"))
text_result.grid(columnspan=5)
text_result.config(bg="#014d14")
root.title("Calculator")

btn_1=tk.Button(root, text="1", command=lambda:add_to_calculation(1), width=5, font=("Times",18))
btn_1.grid(row=2, column=1)
btn_1.config(activebackground="#191a19",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#000301")
btn_2=tk.Button(root, text="2", command=lambda:add_to_calculation(2), width=5, font=("Times",18))
btn_2.grid(row=2, column=2)
btn_2.config(activebackground="#191a19",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#000301")
btn_3=tk.Button(root, text="3", command=lambda:add_to_calculation(3), width=5, font=("Times",18))
btn_3.grid(row=2, column=3)
btn_3.config(activebackground="#191a19",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#000301")
btn_4=tk.Button(root, text="4", command=lambda:add_to_calculation(4), width=5, font=("Times",18))
btn_4.grid(row=3, column=1)
btn_4.config(activebackground="#191a19",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#000301")
btn_5=tk.Button(root, text="5", command=lambda:add_to_calculation(5), width=5, font=("Times",18))
btn_5.grid(row=3, column=2)
btn_5.config(activebackground="#191a19",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#000301")
btn_6=tk.Button(root, text="6", command=lambda:add_to_calculation(6), width=5, font=("Times",18))
btn_6.grid(row=3, column=3)
btn_6.config(activebackground="#191a19",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#000301")
btn_7=tk.Button(root, text="7", command=lambda:add_to_calculation(7), width=5, font=("Times",18))
btn_7.grid(row=4, column=1)
btn_7.config(activebackground="#191a19",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#000301")
btn_8=tk.Button(root, text="8", command=lambda:add_to_calculation(8), width=5, font=("Times",18))
btn_8.grid(row=4, column=2)
btn_8.config(activebackground="#191a19",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#000301")
btn_9=tk.Button(root, text="9", command=lambda:add_to_calculation(9), width=5, font=("Times",18))
btn_9.grid(row=4, column=3)
btn_9.config(activebackground="#191a19",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#000301")
btn_0=tk.Button(root, text="0", command=lambda:add_to_calculation(0), width=5, font=("Times",18))
btn_0.grid(row=5, column=2)
btn_0.config(activebackground="#191a19",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#000301")
btn_plus=tk.Button(root, text="+", command=lambda:add_to_calculation("+"), width=5, font=("Times",18))
btn_plus.grid(row=2, column=4)
btn_plus.config(activebackground="#333333",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#191a19")
btn_minus=tk.Button(root, text="-", command=lambda:add_to_calculation("-"), width=5, font=("Times",18))
btn_minus.grid(row=3, column=4)
btn_minus.config(activebackground="#333333",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#191a19")
btn_mul=tk.Button(root, text="*", command=lambda:add_to_calculation("*"), width=5, font=("Times",18))
btn_mul.grid(row=4, column=4)
btn_mul.config(activebackground="#333333",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#191a19")
btn_div=tk.Button(root, text="/", command=lambda:add_to_calculation("/"), width=5, font=("Times",18))
btn_div.grid(row=5, column=4)
btn_div.config(activebackground="#333333",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#191a19")
btn_open=tk.Button(root, text="(", command=lambda:add_to_calculation("("), width=5, font=("Times",18))
btn_open.grid(row=5, column=1)
btn_open.config(activebackground="#333333",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#191a19")
btn_close=tk.Button(root, text=")", command=lambda:add_to_calculation(")"), width=5, font=("Times",18))
btn_close.grid(row=5, column=3)
btn_close.config(activebackground="#333333",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#191a19")
btn_equals=tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Times",18))
btn_equals.grid(row=6, column=3, columnspan=2)
btn_equals.config(activebackground="#333333",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#191a19")
btn_clear=tk.Button(root, text="C", command=clear_field, width=11, font=("Times",18))
btn_clear.grid(row=6, column=1, columnspan=2)
btn_clear.config(activebackground="#cf8104",activeforeground="#f7f8fa",fg="#f7f8fa",bg="#191a19")

root.mainloop()