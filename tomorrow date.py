from datetime import datetime, timedelta

presentday = datetime.now()

tomorrow = presentday + timedelta(1)

print("Today = ", presentday.strftime('%d-%m-%Y'))
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y'))