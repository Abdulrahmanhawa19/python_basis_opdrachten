# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...
def celsius_to_fahrenheit(c):
    f = c * 9/5 + 32
    return f

def fahrenheit_to_celsius(f):
    c = (f - 32) * 5/9
    return c

# Gegeven waarden
c_values = [-12, 62.2]
f_values = [144, 96]

# Loop over gegeven waarden
for i in range(len(c_values)):
    c = c_values[i]
    f = f_values[i]
    
    calculated_f = celsius_to_fahrenheit(c)
    calculated_c = fahrenheit_to_celsius(f)
    
    print(f"{c} graden Celsius is gelijk aan {calculated_f:.1f} graden Fahrenheit")
    print(f"{f} graden Fahrenheit is gelijk aan {calculated_c:.1f} graden Celcius")
    print()
