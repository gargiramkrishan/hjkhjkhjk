import cv2
import os
path = "Images/"

images = []

for file in os.listdir(path):
    name, exe = os.path.splitext(file)
    if exe in [".png",".jpg",".gif"]:
        filename = path+"/"+file
        print(filename)
        images.append(filename)

print(len(images))
count = len(images)
frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)
print(size)
out = cv2.VideoWriter('pgffg.mp4',cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)

for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("done")