import matplotlib.pyplot as plt
import numpy as np

def f(x,t):
	return t*x-t**2 #�֐���ݒ�

def subplots():
    fig, ax = plt.subplots()

    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero') #���Ɖ��̎��͒����Ɉʒu������ 
        
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none') #�E�Ə�̎��͐F������
    
    return (fig, ax)

fig, ax = subplots() 

x = np.linspace(-10, 10, 200) #x�͈̔͂����߂�

for s in range(-20,20): #t�Ń��[�v������l�����߂�
 t = s*0.3+0.1
 y = f(x,t) 
 ax.plot(x,y,'k-',linewidth=1)
 
plt.tick_params(labelbottom='off') #x���̖ڐ��������
plt.tick_params(labelleft='off') #y���̖ڐ��������

plt.ylim(-20,30) #y�̕\���͈͂����߂�

plt.show()
