from datetime import datetime, timedelta

# Example date string with offset
date_string = "Tue Apr 03 18:00:09 +0000 2012"

# Parse the date string into a datetime object
date_object = datetime.strptime(date_string, "%a %b %d %H:%M:%S %z %Y")

timestamp = date_object.timestamp()
print(f"Unix Timestamp: {int(timestamp)}")
