import matplotlib.pyplot as plt

#This code finds the value of fibonacci numbers until the Nth digit
# and prints the numbers' projectory in a bar graph


limit = int(input("Enter the maximum number N\n"))
y = [0, 1]

for i in range(limit+1):
    y.append(y[i]+y[i+1])

N = len(y)
x = range(N)
width = 1/1.5
plt.plot(x, y, width, color="orange")
plt.xlabel('Nth number')
plt.ylabel('Fibonacci Value')
plt.title("Fibonacci numbers exponential growth")
plt.grid(True)#This makes sure the gridlines on the graph are drawn
plt.savefig("test.png")#Saves the resulting graph as a png file
plt.show()#Displays the graph
