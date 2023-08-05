import random

def randomChoices(start, end):
    if start > end:
        start, end = end, start

    numbers = {}
    for i in range(start, end + 1):
        numbers[i] = random.choice(["Going to work", "Calling out"])

    return numbers

if __name__ == "__main__":
    try:
        range_start = int(input("Enter range starting number: "))
        range_end = int(input("Enter range ending numbe: "))

        choices = randomChoices(range_start, range_end)

        while True:
            try:
                selected_num = int(input("Enter a number to get your choice (0 to exit): "))
                if selected_num == 0:
                    break

                if range_start <= selected_num <= range_end:
                    print(f"Your choice for {selected_num}: {choices[selected_num]}")
                else:
                    print("Dumb fuck this isn't in the range you told me")
            except ValueError:
                print("This isn't a number???")

    except ValueError:
        print("This isn't a number???")
