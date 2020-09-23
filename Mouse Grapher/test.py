import matplotlib.pyplot as plt
import pyautogui as gui

mouseCoords = []
index = -1
num = 100

while len(mouseCoords) < num:
    tup = gui.position()
    if len(mouseCoords) != 0 and tup == mouseCoords[index]:
        continue
    print(tup)
    mouseCoords.append(tup)
    index += 1
    if index % (num / 10) == 0:
        print('———————————————————————')
        print('P O S I T I O N', index)
        print('———————————————————————')

xValues = list()
yValues = list()

for x, y in mouseCoords:
    xValues.append(x)
    yValues.append(-y)

plt.plot(xValues, yValues)
plt.show()