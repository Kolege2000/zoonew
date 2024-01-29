import tkinter as tk

class Order:
    def __init__(self, root, anna):
        self.root           = root
        self.root.title('Restaurant')
        self.root.geometry('500x700')
        self.root.resizable(width=False, height=False)
        self.order_text     = ''
        self.total_price    = ['Gesamtbetrag', 0, '€']
        self.anna           = anna

        label_top           =   tk.Label(root, text='Was möchtest du bestellen?')
        label_top.pack()

        button_name = {'Döner' : 10, 'Currywurst' : 10, 'Churros' : 6, 'Cookie' : 6, 'Cola' : 5, 'Wasser' : 5}

        for name, price in button_name.items():
            button_pick_meal = tk.Button(root, text=f'{name} : {price} €', command=lambda n=name, p=price : self.button_pick_meal_click(n,p))
            button_pick_meal.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        self.label_order   =   tk.Label(root, text=self.order_text)
        self.label_order.pack(anchor=tk.NW)

        button_exit = tk.Button(root, text='raus hier', width=25, height=3, command= root.destroy)
        button_exit.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

        button_order = tk.Button(root, text='bestellen', width=25, height=3, command=lambda : self.button_order_click())
        button_order.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

        self.label_total_price  =   tk.Label(root, text=self.total_price, font=('Arial', 16))
        self.label_total_price.pack(side=tk.BOTTOM, anchor=tk.SE)

    def button_pick_meal_click(self, name, price):
        self.order_text += f'{name}\n'
        self.label_order.configure(text=self.order_text)

        self.total_price[1] += price
        self.label_total_price.configure(text=self.total_price)

    def button_order_click(self):
        if self.anna.money >= self.total_price[1]:
            self.anna.money -= self.total_price[1]
            print('Essen gekauft')
            print(f'du hast noch {self.anna.money} € übrig\n')
        else:
            print('du hast nicht genug Geld\n')
        self.root.destroy()

def run_order(anna):
    root = tk.Tk()
    Order(root, anna)
    root.mainloop()