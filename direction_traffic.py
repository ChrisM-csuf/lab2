"""
get the street number
if the street number is even display eastbound
if odd, display westbound
finish
"""

def calculate_street(street):
    print("divide: ", street / 2)
    print("Modulus: ", street % 2 == 0)
    if (street % 2) == 0:
        print("Eastbound")
    else:
        print("westbound")

calculate_street(11)
