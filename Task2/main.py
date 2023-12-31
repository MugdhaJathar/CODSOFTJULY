import tkinter as tk

calc = ""

def add_calc(symbol):
    global calc
    calc += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calc)
    
def evaluate_calc():
    global calc
    try:
        result = str(eval(calc))
        calc = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calc
    calc = ""
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calc)
    
root = tk.Tk() 
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Palantino", 24),bg='#DDE6ED',fg='#404258')
text_result.grid(columnspan=5)

btn1 = tk.Button(root, text="1", command=lambda: add_calc(1), width=5, font=("Palantino", 14),bg='#6B728E',fg='#F1F6F9')
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command=lambda: add_calc(2), width=5, font=("Palantino", 14),bg='#6B728E',fg='#F1F6F9')
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command=lambda: add_calc(3), width=5, font=("Palantino", 14),bg='#6B728E',fg='#F1F6F9')
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text="4", command=lambda: add_calc(4), width=5, font=("Palantino", 14),bg='#6B728E',fg='#F1F6F9')
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda: add_calc(5), width=5, font=("Palantino", 14),bg='#6B728E',fg='#F1F6F9')
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda: add_calc(6), width=5, font=("Palantino", 14),bg='#6B728E',fg='#F1F6F9')
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda: add_calc(7), width=5, font=("Palantino", 14),bg='#6B728E',fg='#F1F6F9')
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command=lambda: add_calc(8), width=5, font=("Palantino", 14),bg='#6B728E',fg='#F1F6F9')
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command=lambda: add_calc(9), width=5, font=("Palantino", 14),bg='#6B728E',fg='#F1F6F9')
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text="0", command=lambda: add_calc(0), width=5, font=("Palantino", 14),bg='#6B728E',fg='#F1F6F9')
btn0.grid(row=5, column=2)

btn_add = tk.Button(root, text="+", command=lambda: add_calc("+"), width=5, font=("Palantino", 14),bg='#404258',fg='#F1F6F9')
btn_add.grid(row=2, column=4)
btn_sub = tk.Button(root, text="-", command=lambda: add_calc("-"), width=5, font=("Palantino", 14),bg='#404258',fg='#F1F6F9')
btn_sub.grid(row=3, column=4)
btn_mul = tk.Button(root, text="*", command=lambda: add_calc("*"), width=5, font=("Palantino", 14),bg='#404258',fg='#F1F6F9')
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_calc("/"), width=5, font=("Palantino", 14),bg='#404258',fg='#F1F6F9')
btn_div.grid(row=5, column=4)
btn_open = tk.Button(root, text="(", command=lambda: add_calc("("), width=5, font=("Palantino", 14),bg='#6B728E',fg='#F1F6F9')
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_calc(")"), width=5, font=("Palantino", 14),bg='#6B728E',fg='#F1F6F9')
btn_close.grid(row=5, column=3)
btn_clear = tk.Button(root, text="C", command= clear_field, width=11, font=("Palantino", 14),bg='#404258',fg='#F1F6F9')
btn_clear.grid(row=6, column=1, columnspan=2)
btn_equals = tk.Button(root, text="=", command=evaluate_calc, width=11, font=("Palantino", 14),bg='#404258',fg='#F1F6F9')
btn_equals.grid(row=6, column=3, columnspan=2)

root.mainloop()  