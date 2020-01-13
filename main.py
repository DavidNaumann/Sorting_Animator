'''
Sorting Animator by: David Naumann
Date: 01/12/2020

'''

import numpy as np
import matplotlib.pyplot as plt
from sorting_methods import timSort
from matplotlib import cm
from matplotlib.colors import ListedColormap
import imageio

def draw_plot(x,y):
    fig, ax = plt.subplots(figsize=(10,5))
    y_max = max(y)
    divider = int(y_max/6)
    colors = []
    for y_val in y:
        if y_val >= (divider * 5):
            y_max = max(y)
            curr_color = tuple([round(y_val/y_max,1),0,0])
        elif y_val >= (divider * 4):
            y_max = divider * 5
            curr_color = tuple([round(y_val / y_max, 1), round(y_val / y_max, 1), 0])
        elif y_val >= (divider * 3):
            y_max = divider * 4
            curr_color = tuple([0, round(y_val / y_max, 1), 0])
        elif y_val >= (divider * 2):
            y_max = divider * 3
            curr_color = tuple([0, 0, round(y_val / y_max, 1)])
        else:
            y_max = divider * 2
            curr_color = tuple([round(y_val / y_max, 1), 0, round(y_val / y_max, 1)])


        colors.append(curr_color)
    colors = tuple(colors)
    plt.bar(x,y,color=colors)

    ax.set(xlabel="X", ylabel="Y", title="Sorting Animation")
    ax.set_ylim(0,len(x))

    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close()
    return image


n = 50

test = list(range(1,n))
np.random.shuffle(test)
print("Beginning Sorting...")
sorts = timSort(test, 32)
print("Sorting done!")
x = range(1,n)

length = 5

frames = int(len(sorts) / length)

images = []

print("Beginning Image Creation...")
image_counter = 0
image_count = len(sorts)
print("0% done with Image Creation")
for sort in sorts:
	images.append(draw_plot(x, sort))
	image_counter += 1
	percent = round((image_counter/image_count * 100),1)
	
	print(str(percent) + "% done with Image Creation")

print("Image Creation done!")
	
print("Beginning Animation...")
kwargs_write = {'fps':2.0,'quantizer':'nq'}
imageio.mimsave('./sort.gif', images, fps=frames)
print("Animation done!")