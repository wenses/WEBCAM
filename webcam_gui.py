import tkinter, cv2
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

win=Tk()
win.title('WEBCAM VIEWER')
win.config(bg='dark blue')
win.resizable(FALSE,FALSE)
win.geometry('900x650')

lt=Label(win,text='BLIXEN WEBCAM VIEWER',fg='white',bg='dark blue',font=('sans-serif','25','bold'))
lt.place(x=10,y=50)


def show_camera():
	global camera
	global ret
	global frame
	camera=cv2.VideoCapture(0,cv2.CAP_DSHOW)

	while True:
		ret, frame=camera.read()
		cv2.imshow('Webcamera: Press x to cancel',frame)
		k=cv2.waitKey(10)
		if k & 0xFF==ord('x'):
			break
	camera.release()
	cv2.destroyAllWindows()

b1=Button(win,text='SHOW CAMERA',fg='white',bg='black',font=('sans-serif','20','bold'),
	command=show_camera)
b1.place(x=50,y=200)

def capture_frame():
	camera=cv2.VideoCapture(0,cv2.CAP_DSHOW)

	while True:
		ret, frame=camera.read()
		cv2.imshow('Webcam:press x to cancel, press c to take a picture',frame)
		
		if cv2.waitKey(10) & 0xFF==ord('x'):
			break
		elif cv2.waitKey(10) & 0xFF==ord('c'):
			cv2.imwrite('blixen_webcam_image.jpg',frame)
	
	camera.release()
	cv2.destroyAllWindows()


b2=Button(win,text='CAPTURE FRAMES',fg='white',bg='black',font=('sans-serif','20','bold'),
	command=capture_frame)
b2.place(x=50,y=300)

with open('about.txt','r') as f:
	howtouse_info=f.read()


messagebox.showinfo('ABOUT THIS SOFTWARE',howtouse_info)




win.mainloop()