import tkinter as tk
from tkinter import ttk, messagebox
from forex_python.converter import CurrencyRates, RatesNotAvailableError

CURRENCY_NAMES = {
    "USD": "United States Dollar",
    "EUR": "Euro",
    "INR": "Indian Rupee",
    "JPY": "Japanese Yen",
    "GBP": "British Pound Sterling",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "SGD": "Singapore Dollar",
    "BGN": "Bulgarian Lev",
    "BRL": "Brazilian Real",
    "CZK": "Czech Koruna",
    "DKK": "Danish Krone",
    "HKD": "Hong Kong Dollar",
    "HUF": "Hungarian Forint",
    "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Shekel",
    "ISK": "Icelandic Krona",
    "KRW": "South Korean Won",
    "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit",
    "NOK": "Norwegian Krone",
    "NZD": "New Zealand Dollar",
    "PHP": "Philippine Peso",
    "PLN": "Polish Zloty",
    "RON": "Romanian Leu",
    "SEK": "Swedish Krona",
    "THB": "Thai Baht",
    "TRY": "Turkish Lira",
    "ZAR": "South African Rand"
}


c = CurrencyRates()

try:
    available_codes = sorted(c.get_rates("USD").keys())
    available_codes.insert(0,"USD")

    available_currencies = [f"{code} - {CURRENCY_NAMES.get(code, 'Unknown')}" for code in available_codes]

except Exception as e:
    messagebox.showerror("Error", f"unable to fetch currency list : \n{e}")
    available_currencies = [f"{code} - {name}" for code, name in CURRENCY_NAMES.items()]

def convert_currencies():
    try:
        amount = float(amount_entry.get())
        from_cur = from_currency_cb.get().split("-")[0].strip().upper()
        to_currencies = [cur.split("-")[0].strip().upper() for cur in to_currency_cb.get().split(",") if cur.strip()]

        if not from_cur or not to_currencies:
            raise ValueError("Please select the both source and target currencies")
        results=[]

        for to_cur in to_currencies:
            try:
                converted = c.convert(from_cur, to_cur, amount)
                results.append(f"{amount :.2f} {from_cur} = {converted :.2f} {to_cur}")

            except RatesNotAvailableError:
                results.append(f"Rate not avilable for {from_cur} -> {to_cur}")

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "\n".join(results))

    except ValueError as ve:
        messagebox.showerror("Invalid string",str(ve))

    except Exception as e :
        messagebox.showerror("Error",f"Something went wrong:\n{e}")


root = tk.Tk()
root.title("Live Currency Converter")
root.geometry("400x400")
root.resizable(False,False)

tk.Label(root, text ="Live Currency Converter", font = ("Arial",14, "bold")).pack(pady=5)


tk.Label(root, text = "From Currency: ").pack()
from_currency_cb = ttk.Combobox(root, value = available_currencies, state = "readonly", font=("Arial",11))
from_currency_cb.set("USD - United States Dollar")
from_currency_cb.pack(pady = 5)

tk.Label(root, text="TO Currency: ").pack()
to_currency_cb = ttk.Combobox(root, value= available_currencies, font=("Arial",11))
to_currency_cb.set("INR - Indian Rupee")
to_currency_cb.pack(pady=5)

tk.Label(root, text ="Amount: ",font=("Arial", 12)).pack(pady=5)
amount_entry = tk.Entry(root,font=("Arial", 12))
amount_entry.pack(pady=5)

tk.Button(root, text = "CONVERT", command = convert_currencies, bg="#4CAF50",  fg="white",  font=("Arial", 12, "bold"), width=15).pack(pady=15)

output_text = tk.Text(root, height = 10, width = 50,font=("Arial", 11))
output_text.pack(pady = 5)

root.mainloop()
            
                
