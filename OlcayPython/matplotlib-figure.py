import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20) #-10 ile 20 arasını 9 eşit parçaya böl
y = x ** 3 
z = x**2

"""
figure = plt.figure()

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8]) #bir figüre eksen eklemek için kullanılır.
axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("x axis")
axes_cube.set_ylabel("y axis")
axes_cube.set_title("Cube")

axes_square = figure.add_axes([0.15,0.6,0.25,0.25])
axes_square.plot(x,z,"r")
axes_square.set_xlabel("x axis")
axes_square.set_ylabel("y axis")
axes_square.set_title("square")
"""
"""
figure = plt.figure()
axes = figure.add_axes([0,0,1,1])
axes.plot(x,z,label = "Square")
axes.plot(x,y,label = "Cube")
axes.legend(loc=4) #lov 4 ise sağ alt köşe

"""
gif,axes = plt.subplots(nrows=2,ncols=1,figsize = (8,8))
axes[0].plot(x,y)
axes[0].set_title("Square")
axes[1].plot(x,z)
axes[1].set_title("Cube")

plt.tight_layout()
# fig.savefig("Figure1.png") # fig kaydetme .pdf dersek pdf şeklinde
plt.show()