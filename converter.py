import tkinter as tk
from tkinter import ttk

# Function to convert units
def convert():
    try:
        value = float(entry_value.get())
        unit_from = combo_from.get()
        unit_to = combo_to.get()
        
        if unit_from == "Meters" and unit_to == "Kilometers":
            result = value / 1000
        elif unit_from == "Meters" and unit_to == "Miles":
            result = value / 1609.34
        elif unit_from == "Kilometers" and unit_to == "Meters":
            result = value * 1000
        elif unit_from == "Kilometers" and unit_to == "Miles":
            result = value / 1.60934
        elif unit_from == "Miles" and unit_to == "Meters":
            result = value * 1609.34
        elif unit_from == "Miles" and unit_to == "Kilometers":
            result = value * 1.60934
        else:
            result = "Invalid Conversion"
        
        # Update the result label
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input! Please enter a number.")

# Setting up the main window
window = tk.Tk()
window.title("Unit Converter")

# Creating the labels and entry fields
label_title = tk.Label(window, text="Unit Converter", font=("Arial", 16))
label_title.pack(pady=10)

label_value = tk.Label(window, text="Enter Value:")
label_value.pack()

entry_value = tk.Entry(window)
entry_value.pack(pady=5)

# Creating combo boxes for unit selection
label_from = tk.Label(window, text="From Unit:")
label_from.pack()

combo_from = ttk.Combobox(window, values=["Meters", "Kilometers", "Miles"])
combo_from.set("Meters")
combo_from.pack(pady=5)

label_to = tk.Label(window, text="To Unit:")
label_to.pack()

combo_to = ttk.Combobox(window, values=["Meters", "Kilometers", "Miles"])
combo_to.set("Kilometers")
combo_to.pack(pady=5)

# Button to trigger conversion
button_convert = tk.Button(window, text="Convert", command=convert)
button_convert.pack(pady=10)

# Label to display the result
label_result = tk.Label(window, text="Result: ", font=("Arial", 12))
label_result.pack(pady=5)

# Run the GUI loop
window.mainloop()
