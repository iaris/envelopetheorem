import matplotlib.pyplot as plt
import numpy as np

def f(x,t):
	return t*x-t**2 #関数を設定

def subplots():
    fig, ax = plt.subplots()

    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero') #左と下の軸は中央に位置させる 
        
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none') #右と上の軸は色を消す
    
    return (fig, ax)

fig, ax = subplots() 

x = np.linspace(-10, 10, 200) #xの範囲を決める

for s in range(-20,20): #tでループさせる値を決める
 t = s*0.3+0.1
 y = f(x,t) 
 ax.plot(x,y,'k-',linewidth=1)
 
plt.tick_params(labelbottom='off') #x軸の目盛りを消す
plt.tick_params(labelleft='off') #y軸の目盛りを消す

plt.ylim(-20,30) #yの表示範囲を決める

plt.show()
