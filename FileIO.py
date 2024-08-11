from tkinter import *
import requests
from tkinter import ttk
from tkinter import filedialog as fd


def upload():
    filepath = fd.askopenfilename()
    if filepath:
        files = {'file': open(filepath,'rb')}
        response = requests.post('https://file.io',files=files)
        if response.status_code == 200:
            link = response.json()['link']
            entry.insert(0,link)


window = Tk()
window.title("Сохранение файлов в облаке")
window.geometry("400x200")

button = ttk.Button(text="Загрузить файл", command=upload)
button.pack()

entry = ttk.Entry()
entry.pack()

window.mainloop(())