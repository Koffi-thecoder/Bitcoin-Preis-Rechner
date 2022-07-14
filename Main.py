import tkinter as tk
from tkinter import ttk
import requests

BITCOIN_PRICE_API = "https://api.coindesk.com/v1/bpi/currentprice.json"


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("390x200")
        self.title("Bitcoin-Preis-Rechner")
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        self.style = ttk.Style()
        self.style.configure("TLabel", font = ("Arial",13),foreground = "blue")

        self.style.configure("TButton", font =("Arial",13), foreground = "BLACK")


        window = Frame1(self)
        window.grid(column = 0, row =0)


class Frame1(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.euro_value = tk.StringVar(value="Hier wird dann den Preis in Euro angezeigt")

        user_label1 = ttk.Label(self, text = "Anzahl Bitcoin: ")
        user_label1.grid(column = 0, row= 0)

        self.user_enty = ttk.Entry(self, width  = 60)
        self.user_enty.grid(column = 0, row = 1, sticky = "w", columnspan = 3, padx = 5, pady = 5)

        user_label2 = ttk.Label(self, text = "Preis in Euro: ")
        user_label2.grid(column = 0, row = 2, sticky = "w", padx = 5, pady = 5)

        user_label3 = ttk.Label(self, textvariable = self.euro_value )
        user_label3.grid(column = 0, row = 3, sticky = "w", padx = 5, pady = 5)

        action_button = ttk.Button(self, text ="Berechnung durchführen", command = self.calculate_bitcoin_in_euro)
        action_button.grid(column = 0, row = 4, sticky = "ew", columnspan = 3, padx = 5, pady = 5)

    def calculate_bitcoin_in_euro(self):
        try:
            response = requests.get(BITCOIN_PRICE_API)
            response_dictionary = response.json()
            current_bitcoin_preis = response_dictionary["bpi"]["EUR"]["rate_float"]
            bitcoin_in_euro = (float(self.user_enty.get())* current_bitcoin_preis)
            self.euro_value.set("{:.2f}".format(bitcoin_in_euro))
            print(bitcoin_in_euro)

        except ValueError:
            print("Gebe einen gültigen Wert")




root = MainWindow()
root.mainloop()