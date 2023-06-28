# 2.1.1
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()

# 2.1.2
plt.plot([1,2,3,4],[1,4,9,16])
plt.show()

# 2.1.3
plt.plot([1,2,3,4],[1,4,9,16])
plt.xlabel('X-label')
plt.ylabel('Y-label')
plt.show()

# 2.1.4
plt.plot([1,2,3,4],[2,3,5,10], label='Price ($)')
plt.xlabel('X-label')
plt.ylabel('Y-label')
plt.legend()
plt.show()

# 2.1.5
plt.plot([1,2,3,4],[2,3,5,10],label='Price ($)')
plt.plot([1,2,3,4],[3,5,9,7],label='Demand (#)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend(loc='best', ncol=2)
plt.show()

# 2.1.6
plt.plot([1,2,3,4],[2,3,5,10])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.axis([0,5,0,20])

plt.show()

# 2.1.7
import numpy as np
x = np.linspace(-10,10,100)
y = x**3
plt.plot(x,y)
plt.xscale('symlog')
plt.show()

# 2.1.8
x = np.linspace(0,5,100)
y = np.exp(x)
plt.plot(x,y)
#plt.yscale('linear')
plt.yscale('log')
plt.show()

# 2.1.9
plt.plot([1,2,3,4],[2.0,3.0,5.0,10.0],'r')
plt.plot([1,2,3,4],[2.0,2.8,4.3,6.5],'g')
plt.plot([1,2,3,4],[2.0,2.5,3.3,4.5],'b')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

# 2.1.10
plt.plot([1,2,3,4],[2,3,5,10],'bo')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

# 2.1.11
#plt.plot([1,2,3,4],[2,3,5,10],'bo-')
plt.plot([1,2,3,4],[2,3,5,10],'bo--')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()

# 2.1.12
x = np.arange(0,2,0.2)
plt.plot(x,x,'r--',x,x**2,'bo',x,x**3,'g-.')
plt.show()

