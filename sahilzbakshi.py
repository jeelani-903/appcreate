import pysimplegui as sg

layout = [ [sg.Text("Hello", font=("Arial", 16))]]

window = sg.Window("First app", layout)
events, values = window.Read()
window.Close()
