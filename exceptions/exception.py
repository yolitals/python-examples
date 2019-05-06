
import sys

keep_asking = True
 
while keep_asking:
    try:
        x = int(input("Please enter a number: "))
        y = 2 + x
    except:
        print("Something Unexpected has happened.",sys.exc_info()[0])
    else:
        print("El resultado es:", y)
    finally:
        print("Esto siempre se va a ejecutar")