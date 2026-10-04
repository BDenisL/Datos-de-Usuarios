import tkinter as tk
from tkinter import ttk


def save():
    name = box_name.get()
    lastname = box_lastname.get()
    age = box_age.get()
    dni = box_dni.get()
    phonenum = box_phonenum.get()
    email = box_email.get()
    address = box_address.get()
    city = box_city.get()
    prov = box_provin.get()
    postalcode = box_code.get()

    tabla.insert("", "end", values=(
        name,
        lastname,
        age,
        dni,
        phonenum,
        email,
        address,
        city,
        prov,
        postalcode
    ))


vna = tk.Tk()
vna.title("Tablas de Clientes")
vna.geometry("1200x600")

tk.Label(vna, text="").grid(row=0, column=0)
tk.Label(vna, text="").grid(row=1, column=0)

tk.Label(vna, text="Nombre").grid(row=2, column=0)
box_name = tk.Entry(vna)
box_name.grid(row=2, column=1)

tk.Label(vna, text="Apellido").grid(row=3,column=0)
box_lastname = tk.Entry(vna)
box_lastname.grid(row=3, column=1)

tk.Label(vna, text="Edad").grid(row=4, column=0)
box_age = tk.Entry(vna)
box_age.grid(row=4, column=1)

tk.Label(vna, text="DNI").grid(row=5, column=0)
box_dni = tk.Entry(vna)
box_dni.grid(row=5,column=1)

tk.Label(vna, text="Telefono").grid(row=6, column=0)
box_phonenum = tk.Entry(vna)
box_phonenum.grid(row=6, column=1)

tk.Label(vna, text="EMAIL").grid(row=7, column=0)
box_email = tk.Entry(vna)
box_email.grid(row=7, column=1)

tk.Label(vna, text="Direccion").grid(row=8, column=0)
box_address = tk.Entry(vna)
box_address.grid(row=8, column=1)

tk.Label(vna, text="Ciudad").grid(row=9,column=0)
box_city = tk.Entry(vna)
box_city.grid(row=9, column=1)

tk.Label(vna, text="Provincia").grid(row=10, column=0)
box_provin = tk.Entry(vna)
box_provin.grid(row=10,column=1)

tk.Label(vna,text="Codigo Postal").grid(row=11, column=0)
box_code = tk.Entry(vna)
box_code.grid(row=11, column=1)

buttonSave = tk.Button(vna, text="Guardar", command=save)
buttonSave.grid(row=12, column=0, columnspan=3, pady=12)

c = (
    "Nombre",
    "Apellido",
    "Edad",
    "DNI",
    "Telefono",
    "EMAIL",
    "Direccion",
    "Ciudad",
    "Provincia",
    "Codigo Postal"
)

tabla = ttk.Treeview(vna, columns=c, show="headings", height=10)

for col in c:
    tabla.heading(col, text=col)
    tabla.column(col, width=100)
    tabla.grid(row=13, column=0, columnspan=4, padx=10, pady=20)


vna.mainloop()