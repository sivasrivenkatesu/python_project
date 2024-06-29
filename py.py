# import numpy as np
# a=np.array([1,2,3,4])
# b=np.array([1,2,3,4])
# c=a+b
# print(c)
# list=[1,2,3,4,5]
# e=np.array(list)
# print(e)
# f=e[1:5]
# print(f)
# g=a[1]
# print(g)
# #multidimensional array in numpy
# l2=[c,c,c,c,c]
# l3=[c,c,c,c,c]
# l4=[c,c,c,c,c]
# final=np.array([l2,l3,l4])
# print("ADD",np.add(a,b))
# print("sub",np.subtract(a,b))
# print("ADD",np.multiply(a,b))
# print("ADD",np.divide(a,b))
# print(final)

# 

import matplotlib.pyplot as p
import pandas as pd 
import numpy as np
# p.title("matplotlib practice")
# x1=np.array([1,2,6,8,5])
# x3=np.array([3,8,1,0,8])
# p.subplot(1,2,1)
# pl=p.plot(x1,x3,marker='*',linestyle="dotted")
# p.xlabel("siva sri")
# p.ylabel("venkatesu")
# p.grid(axis='y')
# p.show()
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()