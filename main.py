largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        num = int(num)
        if largest is None:
            largest = num
        elif num >= largest:
            largest = num
        elif smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num
        print(f"mayor es {largest}, menos es {smallest}")
    except:
        print("Invalid input")
    if num == "done":
        break
print("Maximum is", largest)
print("Minimun is", smallest)