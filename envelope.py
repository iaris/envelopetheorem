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

    ax.set_xticks([]) #x���̖ڐ��������
    ax.set_yticks([]) #y���̖ڐ��������
    
    return (fig, ax)

fig, ax = subplots() 

x = np.linspace(-10, 10, 200) #x�͈̔͂����߂�


#envelope0(�ׂ���)
for s in range(-20,20): #t�Ń��[�v������l�����߂�
    t = s*0.3
    y = f(x,t) 
    ax.plot(x,y,'k-',linewidth=1)

#envelope1(�e��)
for s in range(-10,10): #t�Ń��[�v������l�����߂�
    t = s*0.5
    y = f(x,t) 
    ax.plot(x,y,'k-',linewidth=1)
 
plt.ylim(-20,30) #y�̕\���͈͂����߂�

plt.savefig() #�t�@�C���ɏo��
plt.show()
