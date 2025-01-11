numbers = input("Provide a list of numerical data separated by spaces:\n").split()
print()
print("Number Analysis Results:")
print("-"*20)

try:
    numbers = [int(x) for x in numbers]
except ValueError:
    print("Please only include numbers.")
    exit()

frequency = {number: numbers.count(number) for number in numbers}

print(f"""Total Numbers: {len(numbers)}
Sum of Numbers: {sum(numbers)}
Range of Numbers: {max(numbers)-min(numbers)}
Most Frequent Number: {max(frequency, key=lambda x: frequency[x])} (appears {max(frequency.values())} times)
Average Number: {sum(numbers) / len(numbers)}
""")