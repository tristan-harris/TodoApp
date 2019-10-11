from datetime import datetime

def date_add_suffix(day_of_month):
    # https://stackoverflow.com/questions/3644417/python-format-datetime-with-st-nd-rd-th-english-ordinal-suffix-like
    return str(day_of_month)+("th" if 4<=day_of_month%100<=20 else {1:"st", 2:"nd", 3:"rd"}.get(day_of_month%10, "th"))

def friendly_datetime(the_datetime):
    # e.g 12th of November
    return date_add_suffix(the_datetime.day) + the_datetime.strftime(" of %B")
