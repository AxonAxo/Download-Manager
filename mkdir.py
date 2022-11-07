import os
from time import sleep


Direc = input("Choose a directory")

x = Direc + "/Text"
os.mkdir(x)
print("Made Directory" + x)
sleep(1)
x = Direc + "/3D_Models"
os.mkdir(x)
print("Made Directory" + x)
sleep(1)
x = Direc + "/Archives"
os.mkdir(x)
print("Made Directory" + x)
sleep(1)
x = Direc + "/Images"
os.mkdir(x)
print("Made Directory" + x)
sleep(1)
x = Direc + "/Music"
os.mkdir(x)
print("Made Directory" + x)
sleep(1)
x = Direc + "/Programs"
os.mkdir(x)
print("Made Directory" + x)

