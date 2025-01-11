import matplotlib.pyplot as plt, os

numbers = []
for filename in os.listdir('files'):
    with open(f"files/{filename}") as file:
        numbers.append(float(file.read()))



plt.figure(num=10)
plt.plot(numbers)
plt.grid(True)
plt.title("Plotting Data with matplotlib")
plt.xlabel("Number Index")
plt.ylabel("Number Value")
plt.show()