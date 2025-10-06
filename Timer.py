#cd /home/source/srcCode/Cska001/
#python3 Timer.py

from tkinter import messagebox
import tkinter as tk
import time

def timer():
   root = tk.Tk()
   root.withdraw()
   messagebox.showinfo("Вопрос", "Есть ли биллеты на 21-12-2025 ?")
   root.destroy()

while True:
   timer()
   time.sleep(5)
       
#Звуковой сигнал проигровать



