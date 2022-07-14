capture=cv2.VideoCapture("/content/25.mp4")
frameNr=0
while(True):
  success,frame=capture.read()
  if success:
    cv2.imwrite(f'/content/my frames/frames_{frameNr}.jpg',frame)
    gray_image = cv2.cvtColor(/content/25.mp4, cv2.COLOR_BGR2GRAY)
    imshow("Converted to Grayscale", gray_)
  else:
      break 
  frameNr=frameNr+1
capture.release()
print(frameNr)
