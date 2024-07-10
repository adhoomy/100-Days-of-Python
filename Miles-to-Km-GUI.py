# note: the converted numbers are rounded

from tkinter import *


def miles_to_km():
    miles = miles_entry.get()
    km = str(round(int(miles) * 1.609344))
    converted.config(text=km)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=30, height=30)
window.config(padx=30, pady=30)

miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)
miles_entered = int(miles_entry.get())

miles_text = Label(text="Miles", font=("Arial", 10))
miles_text.grid(column=2, row=0)

equal_to_text = Label(text="is equal to", font=("Arial", 10))
equal_to_text.grid(column=0, row=1)

converted = Label(text="0", font=("Arial", 10))
converted.grid(column=1, row=1)

miles_text = Label(text="is equal to", font=("Arial", 10))
miles_text.grid(column=0, row=1)

miles_text = Label(text="Km", font=("Arial", 10))
miles_text.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
