
# Дано расстояние L в сантиметрах. Используя операцию деления
# нацело, найти количество полных метров в нем (1 метр =100 см).


import tkinter as tk

def to_meters():
    l = float(entry_l.get())
    meters = l / 100
    whole_meters = int(meters)
    meters_result.config(text=f"Количество полных метров: {whole_meters}.")

root = tk.Tk()
root.title("Сантиметры в метры")

label_l = tk.Label(root, text="Длина в сантиметрах:")
label_l.pack()
entry_l = tk.Entry(root)
entry_l.pack()

button_calculate = tk.Button(root, text="Посчитать", command=to_meters)
button_calculate.pack()

meters_result = tk.Label(root, text="")
meters_result.pack()

root.mainloop()