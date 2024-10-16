import cv2
import time
import numpy
# Set up video capture
vid = input("please enter the path of video: ")
cap = cv2.VideoCapture(vid)

times = []
frames = []
flag = 0



print("calculating the speed needs too much time around 1,5 hours")
print("you can test task4.py file that uses built in find_contour function and is faster")
print("or wait until this code finishes, Thank you for your patience")
print("In Total there are around 2300 frames")

ret, image2 = cap.read()
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

def find_obj(image1):

    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    subtracted_image = cv2.absdiff(gray1, gray2)
    threshold_value = 50
    max_value = 255  # Value assigned to pixels above the threshold
    _, thresholded_image = cv2.threshold(subtracted_image, threshold_value, max_value, cv2.THRESH_BINARY)
    arr = numpy.array(thresholded_image)
    n = len(arr)
    m = len(arr[0])
    vis = []
    for i in range(n):
        lst = []
        for j in range(m):
            lst.append(False)
        vis.append(lst)
    obj = []
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [1, 1, 1, 0, -1, -1, -1, 0]
    for i in range(n):
        for j in range(m):
            area = 0
            lst = []
            if vis[i][j] == False and arr[i][j] == 255:
                vis[i][j] = True
                area += 1
                lst.append([i, j])
                while len(lst) > 0:
                    p = lst[0]
                    px = p[0]
                    py = p[1]
                    lst.pop(0)
                    for t in range(len(dx)):
                        x = dx[t] + px
                        y = dy[t] + py
                        if 0 <= x < n and 0 <= y < m and vis[x][y] == False and arr[x][y] == 255:
                            vis[x][y] = True
                            lst.append([x, y])
                            area += 1
                obj.append(area)
    mx = 0
    for a in obj:
        if a > mx:
            mx = a

    return mx

while True:
    # Read the current frame
    flag += 1
    ret, frame = cap.read()

    if not ret:
        break

    # print('car has entered')
    cur = find_obj(frame)

    if cur > 150:
        times.append(time.time())

    print(f"current frame: {flag}")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(times)
total_Time = (times[len(times) - 1] - times[0]) / 25
total_Distance = 50

average_speed = total_Distance * 36 / total_Time

print(f"average speed of the car on this distance is: {average_speed}")
