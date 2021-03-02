import re

dates = input()
pattern = r"\b(?P<day>\d{2})(?P<sep>\.|-|/)(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})\b"

match_dates = re.finditer(pattern, dates)
for date in match_dates:
    d = date.groupdict()
    print(f"Day: {d['day']}, Month: {d['month']}, Year: {d['year']}")
