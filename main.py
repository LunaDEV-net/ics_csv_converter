import icalendar
import csv
from pathlib import Path

ics_path = Path("data/ics.ics")
csv_path = Path("data/output.csv")

with ics_path.open() as f:
    calendar = icalendar.Calendar.from_ical(f.read())

required_fields = ["SUMMARY", "description".upper(), "location".upper(), "DTSTART", "DTEND"]
other_fields = set()

for component in calendar.walk():
    if component.name == "VEVENT":
        other_fields.update(component.keys())

other_fields.difference_update(required_fields)
sorted_fields = required_fields + sorted(other_fields)


def clean_value(value):
    if isinstance(value, icalendar.prop.vDDDTypes):
        return value.dt if hasattr(value, 'dt') else str(value)
    return str(value)


with csv_path.open(mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(sorted_fields)

    for component in calendar.walk():
        if component.name == "VEVENT":
            row = [clean_value(component.get(field, "")) for field in sorted_fields]
            writer.writerow(row)