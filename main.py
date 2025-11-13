# I cannot believe I was flipping out about a "str int" error.
# Regardless, here's the code. 

# Inputs
temperature = int(input("What is the current temperature outside today?"))
status = input("Will you go outside today? (y/n)")
weather = input("Will it rain/snow today? (y/n)")

# Temp outputs
print("Outside temperature = ",temperature," degrees celsius.")
if status == "n":
    print("Ensure your indoor location has proper heating.")
    print("Wear a longsleeve and pants (such as cargos or sweats).")
elif status == "y":
    if temperature > 20:
        print("Wear a simple shirt with some rugged pants (jeans, cargos)")
    elif temperature <= 20 and temperature > 10:
        print("Wear a sweater over a shirt with some rugged pants")
    elif temperature <= 10 and temperature > 5:
        print("Wear a thick sweater or hoodie and a shirt (optimally longsleeve) with rugged pants.")
        print("If no thick sweater, use thin sweater and jacket.")
    elif temperature <= 5:
        print("Severe cold imminent. Wear a jacket, sweater, shirt, and pants.")
        print("Accessorize with gloves, hat, and scarf.")
    else:
        print("error")
else:
    print("ERROR: must provide with y (yes) or n (no) as response!")
print()

# Weather check
if weather == "y":
    print("Rain/snow to be expected.")
    print("Regardless of temperature, consider wearing something for that weather.")
    print("Suggestions: jacket, windbreaker, thermals, raincoat, boots, poncho...")
    print("Consider taking an umbrella with you!")
elif weather == "n":
    print("No rain or snow today.")
else:
    print("ERROR: must provide with y (yes) or n (no) as response!")
