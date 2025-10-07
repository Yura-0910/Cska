#cd /home/source/srcCode/Cska001/
#python3 Timer.py

from tkinter import messagebox
import tkinter as tk
import time
from datetime import datetime

def timer():
   root = tk.Tk()
   root.withdraw()
   print("\a", end='', flush=True)
   messagebox.showinfo("Вопрос", "Есть ли биллеты на 21-12-2025 ?")
   root.destroy()
   current_datetime = datetime.now()
   print(f"Текущая дата и время: {current_datetime}")

while True:
   timer()
   time.sleep(3600)
       
#Звуковой сигнал проигровать:: три раза, с паузой в секунду. Затем выдать сообщение.
