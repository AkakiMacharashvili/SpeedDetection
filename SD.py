import cv2
import time
# Set up video capture
vid = input("please, enter the path of video: ")
cap = cv2.VideoCapture(vid)

# Read the first frame
ret, prev = cap.read()

# Convert the frame to grayscale
prev_converted_into_grey = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

# Set up the background subtractor
diff = cv2.createBackgroundSubtractorMOG2()
times = []
flag = 0

while True:
    # Read the current frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply background subtraction
    fgmask = diff.apply(frame_gray)

    # Find contours
    contours = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # print(f"current frame: {flag}")
    # flag += 1
    # Process each contour
    for contour in contours:
        # Calculate contour area
        area = cv2.contourArea(contour)

        # Ignore small contours
        if area < 43:
            continue
        # print('car has entered')
        times.append(time.time())


        x = cv2.boundingRect(contour)[0]
        y = cv2.boundingRect(contour)[1]
        w = cv2.boundingRect(contour)[2]
        h = cv2.boundingRect(contour)[3]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Visual Effect', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows

total_Time = times[len(times) - 1] - times[150]
total_Distance = 50
average_speed = total_Distance * 36 / total_Time
print(f"average speed of the car on this distance is: {average_speed}")

cap.release()
cv2.destroyAllWindows()
