some_string = "This is some string with double   space."

double_spaces = some_string.find("  ")

if double_spaces == -1:
    print("No Double Spaces Found!")
else :
    print("Double Spaces Found!")