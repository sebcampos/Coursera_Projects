from matplotlib import pyplot as plt

#linear function
def h(ø_0, ø_1):
    y_values = []
    x_values = []
    for i in range(0,4):
        x_values.append(i)
        y_values.append( ø_0 + ø_1 * i)
    plt.plot(x_values, y_values)
    print("x\ty")
    for x,y in list(zip(x_values,y_values)):
        print(f"{x}\t{y}")
    return plt.show()


