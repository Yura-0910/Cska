#cd /home/source/srcCode/Cska001/
#python3 Date.py

from datetime import datetime, date, timedelta
def raznica1():
   datetime1 = datetime(2025, 12, 24, 15, 50, 0) #24 декабря 2025 15:50
   datetime2 = datetime(2026, 1, 11, 18, 0, 0)  
   diff = (datetime2 - datetime1)
   days = diff.days
   #где 86400 = 24 часа × 60 минут × 60 секунд
   #где /3600 - для перевода в часы (60 сек * 60 минут)
   hours = int((diff.total_seconds() - days*86400)/3600)
   minutes = int((diff.total_seconds() - days*86400 - hours*3600)/60)  
   print(f"Разница между {datetime1} и {datetime2}")
   print(f"будет {days} дня(ей) {hours} часов {minutes} минут") 

def raznica2():
   original_date = date(2025, 12, 21)
   print(f"Дата начала матча: {original_date}")
   new_date = original_date - timedelta(days=41)
   print(f"За 41 день до начала матча это дата:: {new_date}")

raznica1()
raznica2()
