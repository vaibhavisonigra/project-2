print("Welcome to the pattern generator and number Analyzer!")

while True:
    print(" select an option:")
    print("1. Generate a pattern")
    print("2. Analyze a range of numbers")
    print("3. Exit")
    choice = input("enter your choice:")

    match choice:
        case "1":
            print(" Generate a pattern")
            pattern_size = int(input("Enter the size of the pattern: "))
            for i in range(1, pattern_size + 1):
             print("*" * i)
    
        case "2": 
            print(" Analyze a range of numbers")
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            for num in range(start, end + 1):
             if num % 2 == 0:
                print(f"{num} is even")
            else:
                print(f"{num} is odd")

        case "3":
            print("Exiting the program. Goodbye!")
            break