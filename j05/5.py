number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))
number3 = int(input("enter number3: "))
number4 = int(input("enter number4: "))

sum_number = number1 + number2 + number3

avg = sum_number / 3

if 0 <= number1 <= 20:
    if 0 <= number2 <= 20:
        if 0 <= number3 <= 20:
            if 0 <= number4 <= 20:
                if avg >= 18:
                    print(f"your average: {avg} Grade A")
                elif avg >= 16:
                    print(f"your average: {avg} Grade B")
                elif avg >= 14:
                    print(f"your average { avg} Grade C")
                elif avg >= 10:
                    print(f"your average { avg} Grade D")
                else:
                    print(f"your average: {avg,} you Failed")
            else:
                print("number4 is not valid (0 to 20)")
        else:
            print("number3 is not valid (0 to 20)")
    else:
        print("number2 is not valid (0 to 20)")
else:
    print("number1 is not valid (0 to 20)")
