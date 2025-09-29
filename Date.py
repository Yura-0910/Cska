#cd /home/source/srcCode/Cska001/
#python3 Date.py

from datetime import datetime, date, timedelta
def raznica1():
   datetime1 = datetime(2025, 9, 25)
   datetime2 = datetime(2025, 10, 26)
   difference = (datetime2 - datetime1).days
   print(f"Разница между {datetime1} и {datetime2} будет {difference} дня(ей)") 

def raznica2():
   original_date = date(2025, 12, 21)
   print(f"Дата начала матча: {original_date}")
   new_date = original_date - timedelta(days=31)
   print(f"За 31 день до начала матча это дата:: {new_date}")

raznica1()
raznica2()

