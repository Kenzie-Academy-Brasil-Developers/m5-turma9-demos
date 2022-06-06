from datetime import datetime as dt

now = dt.now()
now
now.day
now.month
now.year
now.minute
now.hour
now.timestamp()
now.strftime("%a %d %b %Y")
date_str = "03/03/1993"
dt.strptime(date_str, "%d/%m/%Y")
date_obj = dt.strptime(date_str, "%d/%m/%Y")
date_obj
date_obj.year
date_obj.day
now
date_obj
now - date_obj
