import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,30,40]
plt.plot(x,y)
plt.title("Simple Line Plot")
plt.plot(x,y,linestyle='--',color='r',marker='o',label="Data Line")
plt.xlabel("X axis")
plt.ylabel("Y label")
plt.legend()
plt.legend()
plt.show()