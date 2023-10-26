import cv2
path = "Images/"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', 'png', 'jpg', 'jfif']:
        file_name = path+"/"+file
print(file_name)
images.append['111.jpg','112.jpg','113.jpg','114.jpg','115.jpg','116.jpg','117.jpg','118.jpg','119.jpg','120.jpg']
count = len(images)

frame = cv2.imread(images[0])
height,width,layers = frame.shape
size = (width,height)

print(size)
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVC'),0.8,size)

for i in range(0, count-1):
    cv2.imread()
    out.write()

print("Done")


