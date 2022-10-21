import cv2
import random
import time
import dropbox

startTime = time.time()


def take_Snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret,frame= videoCaptureObject.read(
        )
        img_name = 'Img' + str(number) + '.png'
        cv2.imwrite(img_name , frame )
        result = False
    return img_name
    print("SnapShot Taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadPic(img_name):
    access_token = 'sl.BRnoMuAssS1FMCRVLfK1xppPnFF7pbNmijlNaQx9HvJ5I_5SlDJI3ykcmcSN_FApaoogMCt5V80XIvhRSGmzDMVBbOwE1i1OZT8rjqJuBETCGoohoPJUzJ7UrAQ3hvwnQ9ZMYyo'
    file = img_name
    file_from = file
    file_2 = '/PicHub/' + img_name
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb')as f:
        dbx.files_upload(f.read(), file_2, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")


def main():
    while(True):
        if((time.time() - startTime ) >= 10):
            name = take_Snapshot()
            uploadPic(name)


main()