 #Importing necessary libraries
import turtle
import tkinter as tk
from PIL import Image, ImageTk

#Class for turtle movement
class Tmovement:

    def __init__(self,pen):
        self.pen=pen

    @staticmethod
    def show_warning_speed(speed):
        if speed==5:
            temp_speed ="Max Speed(5)"
        elif speed==1:
            temp_speed ="Min Speed(1)"
        warning_label = tk.Label(
            root,
            text=temp_speed,
            foreground="red",
            background="black",
            font=("Arial", 12, "bold")
        )
        warning_label.place(relx=0.5, y=10, anchor="n")
        root.after(3000, warning_label.destroy)
    
    def speedup(self):
        global speed
        speed+=1
        if speed>5:
            speed=5
            Tmovement.show_warning_speed(speed)
        self.pen.speed(speed)
    
    def slowdown(self):
        global speed
        speed-=1
        if speed<1:
            speed=1
            Tmovement.show_warning_speed(speed)
        self.pen.speed(speed)

    def lefty(self):
        self.pen.left(30)

    def righty(self):
        self.pen.right(30)

    def forward(self):
        global minx, maxx, miny, maxy
        x=self.pen.xcor()
        y=self.pen.ycor()
        self.pen.forward(10)
        if self.pen.xcor() < minx or self.pen.xcor() > maxx or self.pen.ycor() < miny or self.pen.ycor() > maxy:
            self.pen.backward(10)
        
    def backward(self):
        self.pen.backward(10)

    def penmode(self):
        global updown
        if not updown:
            self.pen.penup()
            updown=True
        else:
            self.pen.pendown()
            updown=False
    
    def continous_mode(self):
        global minx, maxx, miny, maxy, continous
        try:
            if not continous:
                while True:
                    if not (minx < self.pen.xcor() < maxx and miny < self.pen.ycor() < maxy):
                        self.pen.backward(10)
                        break
                    self.pen.forward(speed)
                    continous=True
            else:
                while True:
                    self.pen.forward(0)
                    continous=False
        except:
            pass

#Class for drawing mode
class drawing_mode:

    def __init__(self,pen):
        self.pen=pen

    @staticmethod
    def show_warning_width(width):
        if width==5:
            temp_width ="Max Width(5)"
        elif width==1:
            temp_width ="Min Width(1)"
        warning_label = tk.Label(
            root,
            text=temp_width,
            font=("Arial", 12, "bold"),
            foreground="red",
            background="black",
        )
        warning_label.place(relx=0.5, y=10, anchor="n")
        root.after(3000, warning_label.destroy)

    @staticmethod
    def mode_alert(eraser_mode):
        if eraser_mode:
            mode_info= "Eraser mode activated"
        else:
            mode_info= "Eraser mode deactivated"
        mode_label=tk.Label(root, text=mode_info,font=("Arial",12,"bold") ,foreground="yellow",background="black") 
        mode_label.place(relx=0.5, y=10, anchor="n")
        root.after(3000, mode_label.destroy)

    @staticmethod
    def fill_mode_alert(fill_mode):
        fill_label=tk.Label(root,text="Fill mode activated\nPress F to fill",font=("Arial",12,"bold"),foreground="yellow",background="black")
        if fill_mode:
            fill_label.place(relx=0.5, y=10, anchor="n")
            root.after(3000, fill_label.destroy)

    def pen_widthup(self):
        global width
        width+=1
        if width>5:
            width=5
            drawing_mode.show_warning_width(width)
        self.pen.pensize(width)

    def pen_widthdown(self):
        global width
        width-=1
        if width<1:
            width=1
            drawing_mode.show_warning_width(width)
        self.pen.pensize(width)

    def pen_visibility(self):
        if self.pen.isvisible():
            self.pen.hideturtle()
        else:
            self.pen.showturtle()

    def erase(self):
        global eraser_mode
        global bg_default
        if not eraser_mode:
            eraser_mode=True
            self.pen.pendown()
            if bg_default:
                self.pen.color('white',root.entry_pen.get())
            else:
                self.pen.color(root.entry_BG.get().lower(),root.entry_penfill.get().lower())
        else:
            eraser_mode=False
            if pen_default:
                self.pen.color('black','black')
            else:
                self.pen.color(root.entry_pen.get().lower(),root.entry_penfill.get().lower())
        drawing_mode.mode_alert(eraser_mode)

    def fill(self):
        global fill_mode
        if not fill_mode:
            fill_mode=True
            self.pen.begin_fill()
        else:
            fill_mode=False
            self.pen.end_fill()
        drawing_mode.fill_mode_alert(fill_mode)

    def clear(self):
        self.pen.clear()

#Method to start the game with canvas
def startgame():
    global bg_default
    global pen_default
    root.label_pen.pack_forget()
    root.button_penS.pack_forget()
    root.button_penB.pack_forget()
    root.entry_pen.pack_forget()
    root.label_pen2.pack_forget()
    root.label_penfill.pack_forget()
    root.entry_penfill.pack_forget()
    root.Label_warning.pack_forget()

    label_instructions=tk.Label(root,
                                text="Instructions:\nW: Forward\nS: Backward\nA: Left\nD: Right\nQ: Pen Mode\nC: Clear\nUp Arrow: Increase Speed\nDown Arrow: Decrease Speed\nE: Continous\nZ: Eraser Mode\nU: Increase Pen Width\nJ: Decrease Pen Width\nV: Show/Hide Turtle\nF: Fill Mode\nM: Exit Game",
                                font=("Arial", 20),
                                foreground='yellow',
                                background='black',
                                justify='left')
    label_instructions.pack(side="right",fill='y',padx=0,pady=0)

    canvas = tk.Canvas(root, width=1000, height=700)
    canvas.pack(anchor='w',padx=0,pady=0)
    screen = turtle.TurtleScreen(canvas)

    try:
        screen.bgcolor(root.entry_BG.get().lower())
    except:
        screen.bgcolor('white')
        bg_default=True

    #Object for turtle pen
    pen = turtle.RawTurtle(screen)
    pen.shape("turtle")
    pen.pensize(size)
    pen.speed(speed)
    
    try:
        pen.color(root.entry_pen.get().lower(),root.entry_penfill.get().lower())
    except:
        pen_default=True
        pen.color('black','black')
    

    #Objects for movement and drawing classes
    controller = Tmovement(pen)
    drawing = drawing_mode(pen)

    #Key bindings for turtle control and drawing
    screen.listen()
    screen.onkey(controller.lefty,"a")
    screen.onkey(controller.righty,"d")
    screen.onkey(controller.forward,"w")
    screen.onkey(controller.backward,"s")
    screen.onkey(controller.penmode,"q")
    screen.onkey(drawing.clear,"c")
    screen.onkey(controller.speedup,"Up")
    screen.onkey(controller.slowdown,"Down")
    screen.onkey(controller.continous_mode,'e')
    screen.onkey(drawing.erase,'z')
    screen.onkey(drawing.pen_widthup,'u')
    screen.onkey(drawing.pen_widthdown,"j")
    screen.onkey(drawing.pen_visibility,"v")
    screen.onkey(drawing.fill,"f")
    screen.onkey(root.destroy,"m")

#Method for pen color input screen
def pencolor():
    global blend_color

    root.button_BG.pack_forget()
    root.entry_BG.pack_forget()
    root.label_BG2.pack_forget()
    root.label_BG.pack_forget()
    root.Label_warning.pack_forget()

    root.label_pen=tk.Label(root,
                            text="Choose Pen Color",
                            font=("Arial", 35),
                            foreground='yellow',
                            background=blend_color)
    root.label_pen2=tk.Label(root,
                             text="(without spaces)",
                             font=("Arial", 23),
                             foreground='yellow',
                             background=blend_color)
    root.label_pen.pack(padx=100,pady=20)
    root.label_pen2.pack(padx=100,pady=5)
    root.entry_pen=tk.Entry(root, font=("Arial", 23))
    root.entry_pen.pack(padx=25,pady=25)
    root.label_penfill=tk.Label(root,
                                text="Enter fill color",
                                font=("Arial", 35),
                                foreground='yellow',
                                background=blend_color)
    root.label_penfill.pack(padx=25,pady=20)
    root.entry_penfill=tk.Entry(root, font=("Arial", 23))
    root.entry_penfill.pack(padx=25,pady=25)
    root.button_penS=tk.Button(root,
                               text="Submit",
                               font=("Arial", 18),
                               foreground='yellow',
                               background=blend_color,
                               command=startgame)
    root.button_penS.pack(padx=25,pady=25)
    root.button_penB=tk.Button(root,
                               text="Back",
                               font=("Arial", 18),
                               foreground='yellow',
                               background=blend_color,
                               command=bgcolour)
    root.button_penB.pack(padx=25,pady=5)
    root.Label_warning=tk.Label(root,
                               text="*If invalid color is entered, default color will be used",
                               font=("Arial", 15),
                               foreground='red',
                               background='black')
    root.Label_warning.pack(padx=10,pady=5)

#Method for background color input screen
def bgcolour():
    global blend_color

    label_start.pack_forget()
    button_start.pack_forget()
    try:
        bg_label.pack_forget()
        root.label_pen.pack_forget()
        root.button_penS.pack_forget()
        root.button_penB.pack_forget()
        root.entry_pen.pack_forget()
        root.label_pen2.pack_forget()
        root.label_penfill.pack_forget()
        root.entry_penfill.pack_forget()
        root.Label_warning.pack_forget()
    except:
        pass

    root.label_BG=tk.Label(root,
                           text="Choose Background Color",
                           font=("Arial", 35),
                           foreground='yellow',
                           background=blend_color)
    root.label_BG2=tk.Label(root,
                            text="(without spaces)",
                            font=("Arial", 23),
                            foreground='yellow',
                            background=blend_color)
    root.label_BG.pack(padx=10,pady=20)
    root.label_BG2.pack(padx=10,pady=5)
    root.entry_BG=tk.Entry(root, font=("Arial", 23))
    root.entry_BG.pack(padx=10,pady=100)
    root.button_BG=tk.Button(root,
                             text="Submit",
                             font=("Arial", 18),
                             foreground='yellow',
                             background=blend_color,
                             command=pencolor)
    root.button_BG.pack(padx=0,pady=5)
    root.Label_warning=tk.Label(root,
                               text="*If invalid color is entered, default color will be used",
                               font=("Arial", 15),
                               foreground='red',
                               background='black')
    root.Label_warning.pack(padx=10,pady=5)

#Main window setup
root=tk.Tk()
root.title("Turtle game")
root.geometry("1360x768")

bg_image = Image.open("TurtleBG.png")
bg_image = bg_image.resize((1368, 768)) 
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
blend_color = "#3e6c73"

label_start=tk.Label(root,
                     text="Turtle Game",
                     font=("Fixedsys",60),
                     foreground='yellow',
                     background=blend_color)
label_start.pack(padx=30,pady=30)
button_start=tk.Button(root, text="Start",
                       font=("Arial", 40),
                       foreground='yellow',
                       background=blend_color,
                       command=bgcolour)
button_start.pack(padx=200,pady=200)

#Initial global variables
size=1
speed=1
eraser_mode=False
updown=False
continous=False
width=1
bg_default=False
pen_default=False
fill_mode=False

#Boundary variables
minx = -500
maxx = 500
miny = -350
maxy = 350

#Method to keep the window open
root.mainloop()
