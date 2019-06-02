from matplotlib import pyplot as py
from matplotlib.widgets import Button,RadioButtons
from PIL import Image
import PIL.ExifTags
import piexif

path = "./test.jpg"
emotion = 0

def on_release(event):
    if event.inaxes == None:
        # print ("none")
        return 0
    fig = event.inaxes.figure
    print (emotion)
    print(emo_to_filter(emotion))
    print (usercomment)
    print ('---')

def draw_sad2():
    global sad2 # must global
    point_1 = py.axes([0.2,0.2,0.1,0.08])
    sad2 = Button(point_1, "\U0001F62D")
    sad2.label.set_fontsize(20)
    sad2.on_clicked(sad2_press)

def draw_sad1():
    global sad1 # must global
    point_2 = py.axes([0.3,0.2,0.1,0.08])
    sad1 = Button(point_2, "\U0001F616")
    sad1.label.set_fontsize(20)
    sad1.on_clicked(sad1_press)

def draw_neutral():
    global neutral # must global
    point_3 = py.axes([0.4,0.2,0.1,0.08])
    neutral = Button(point_3, "\U0001F636")
    neutral.label.set_fontsize(20)
    neutral.on_clicked(neutral_press)

def draw_smile1():
    global smile1 # must global
    point_4 = py.axes([0.5,0.2,0.1,0.08])
    smile1 = Button(point_4, "\U0001F600")
    smile1.label.set_fontsize(20)
    smile1.on_clicked(smile1_press)

def draw_smile2():
    global smile2 # must global
    point_5 = py.axes([0.6,0.2,0.1,0.08])
    smile2 = Button(point_5, "\U0001F604")
    smile2.label.set_fontsize(20)
    smile2.on_clicked(smile2_press)

def sad2_press(event):
    global emotion
    emotion = -2
    print ('The photo is too sad! ')

def sad1_press(event):
    global emotion
    emotion = -1
    print ('The photo is a little sad. ')

def neutral_press(event):
    global emotion
    emotion = 0
    print ('I feel nothing. ')

def smile1_press(event):
    global emotion
    emotion = 1
    print ('The photo is a little happy. ')

def smile2_press(event):
    global emotion
    emotion = 2
    print ('The photo is very happy. ')

def draw_ok():
    global ok_button # must global
    point_ok = py.axes([0.3,0.1,0.2,0.08])
    ok_button = Button(point_ok, "Okay")
    ok_button.label.set_fontsize(20)
    ok_button.on_clicked(ok_press)

def ok_press(event):
    insertComment()
    print ('Emotion information Saved!')
    quit()

def button_press(event):
    print ('button is pressed!')

def insertComment():
    exif_dict = piexif.load(path)
    usercomment = 'Emotion[' + str(emotion) + ']'
    exif_dict['Exif'][piexif.ExifIFD.UserComment] = usercomment.encode()
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes,path)
    
if __name__ == "__main__":
    img = Image.open(path)
    fig = py.figure(figsize=(4,6))
    print ('Initialing...')
    draw_sad2()
    draw_sad1()
    draw_neutral()
    draw_smile1()
    draw_smile2()
    draw_ok()
    # fig.canvas.mpl_connect("button_release_event", on_release)
    ax1 = fig.add_subplot(111)
    ax1.imshow(img)
    py.axis("off")
    fig = py.show()
