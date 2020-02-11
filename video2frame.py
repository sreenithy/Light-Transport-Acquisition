import cv2
vidcap = cv2.VideoCapture('Hadamard_20fps_1024_32_pos.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("pos_new/frame%d.png" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1