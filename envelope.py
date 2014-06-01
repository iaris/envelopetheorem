# -*- coding: utf-8 -*-
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

    ax.set_xticks([]) #x軸の目盛りを消す
    ax.set_yticks([]) #y軸の目盛りを消す

    return (fig, ax)

fig, ax = subplots()

x = np.linspace(-10, 10, 200) #xの範囲を決める


FILEFORMAT = 'png'  # 'png' or 'pdf'

FIGNUM = 0  # 0 (細かい) or 1 (粗い)


if FIGNUM == 0:  # envelope0(細かい)
    for s in range(-20, 20 + 1): #tでループさせる値を決める
        t = s * 0.3
        y = f(x, t)
        ax.plot(x, y, 'k-', linewidth=1)

if FIGNUM == 1:  # envelope1(粗い)
    for s in range(-10, 10 + 1): #tでループさせる値を決める
        t = s * 0.5
        y = f(x, t)
        ax.plot(x, y, 'k-', linewidth=1)


plt.ylim(-20, 30) #yの表示範囲を決める

plt.savefig('envelope' + str(FIGNUM) + '.' + FILEFORMAT)  # ファイルに出力
plt.show()
