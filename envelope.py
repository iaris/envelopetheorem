import matplotlib.pyplot as plt
import numpy as np

def f(x,t):
	return t*x-t**2

def subplots():
    "Custom subplots with axes throught the origin"
    fig, ax = plt.subplots()

    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')
    
    ax.grid()
    return (fig, ax)

fig, ax = subplots()  # Call the local version, not plt.subplots()
x = np.linspace(-10, 10, 200)

for s in range(10):
 t = 5-s
 y = f(x,t) 
 ax.plot(x,y,'b-',linewidth=1)
 ax.legend() 

plt.tick_params(labelbottom='off')
plt.tick_params(labelleft='off')
plt.ylim(-20,30)
plt.show()
