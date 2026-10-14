# incident_report.py - T7A starter
# Calculates downtime totals for warehouse incidents (Operations Problem Navigator).
# Heads up: this code is repetitive AND has bugs. That's on purpose.
 
north_dc = [45, 30, 120, 15]   # downtime minutes per incident
west_dc = [90, 20, 45]          # downtime minutes per incident
south_dc = [60, 10, 25]
east_dc = [60, 10, 25]
 
def calculate_total(numbers):
    """Return the sum of downtime minutes."""
    total = 0
    for n in numbers:
        total = total + n
    return total   # deliberate bug: NameError
print ("North DC total downtime:", calculate_total(north_dc))
print ("West DC total downtime:", calculate_total(west_dc))

 

 
print("Most recent North DC incident:", north_dc[4])
 
new_minutes = int(input("Log a new North DC incident (minutes): "))
north_dc.append(new_minutes)
print("New North DC total:", sum(north_dc))