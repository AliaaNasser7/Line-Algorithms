import tkinter as tk
import turtle
from tkinter import *
from tkinter import scrolledtext


INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000

x_max = 350
y_max = 300
x_min = 50
y_min = 100

# Variables to store mouse coordinates
start_x = None
start_y = None
end_x = None
end_y = None


def open_auto_window():
    auto_window = tk.Toplevel(pro)
    auto_window.title("automatic Algorithms")
    auto_window.geometry('300x500+500+100')
    
    dda = tk.Button(auto_window, text='DDA', fg='#FFF8E7', bg='#203A43', width=20,
                    height=2, borderwidth=5, font='Helvetica, 13', command=open_dda_auto)
    dda.place(x=47, y=20)
    bre = tk.Button(auto_window, text='BRESENHAM', fg='#FFF8E7', bg='#203A43', width=20,
                    height=2, borderwidth=5, font='Helvetica, 13', command=open_bresenham_auto)
    bre.place(x=47, y=100)
    mid = tk.Button(auto_window, text='MIDPOINT', fg='#FFF8E7', bg='#203A43', width=20,
                    height=2, borderwidth=5, font='Helvetica, 13', command=open_midpoint_auto)
    mid.place(x=47, y=180)
    clip = tk.Button(auto_window, text='COHEN-SUTHERLAND', fg='#FFF8E7', bg='#203A43',
                     width=20, height=2, borderwidth=5, font='Helvetica, 13', command=open_cohen_sutherland_clip_auto)
    clip.place(x=47, y=260)
    clip2 = tk.Button(auto_window, text='LIANG-BARSKY', fg='#FFF8E7',
                      bg='#203A43', width=20, height=2, borderwidth=5, font='Helvetica, 13',command=open_liang_auto)
    clip2.place(x=47, y=340)
    sqr = tk.Button(auto_window, text='SQUARE', fg='#FFF8E7', bg='#203A43',
                    width=20, height=2, borderwidth=5, font='Helvetica, 13', command=draw_it)
    sqr.place(x=47, y=420)


def open_manual_window():
    auto_window = tk.Toplevel(pro)
    auto_window.title("Manual Algorithms")
    auto_window.geometry('300x430+500+100')
    dda = tk.Button(auto_window, text='DDA', fg='#FFF8E7', bg='#203A43', width=20,
                    height=2, borderwidth=5, font='Helvetica, 13', command=open_dda_man)
    dda.place(x=47, y=20)
    bre = tk.Button(auto_window, text='BRESENHAM', fg='#FFF8E7', bg='#203A43', width=20,
                    height=2, borderwidth=5, font='Helvetica, 13', command=open_bresenham_man)
    bre.place(x=47, y=100)
    mid = tk.Button(auto_window, text='MIDPOINT', fg='#FFF8E7', bg='#203A43', width=20,
                    height=2, borderwidth=5, font='Helvetica, 13', command=open_midpoint_man)
    mid.place(x=47, y=180)
    clip = tk.Button(auto_window, text='COHEN-SUTHERLAND', fg='#FFF8E7', bg='#203A43', width=20,
                     height=2, borderwidth=5, font='Helvetica, 13', command=open_cohen_sutherland_clip_man)
    clip.place(x=47, y=260)
    clip2 = tk.Button(auto_window, text='LIANG-BARSKY', fg='#FFF8E7',
                      bg='#203A43', width=20, height=2, borderwidth=5, font='Helvetica, 13',command=open_liang_man)
    clip2.place(x=47, y=340)


def open_dda_man():
    dda_m = tk.Toplevel(pro)
    dda_m.title("manual DDA")
    dda_m.geometry('500x500+500+100')
    dda_m.configure(bg='#203A43')
    click_num = 0

    def draw_line(event):
        nonlocal click_num 
        global start_x, start_y, end_x, end_y

        if click_num == 0:
            start_x = event.x
            start_y = event.y
            click_num = 1
        else:
            end_x = event.x
            end_y = event.y

            line_coords = dda_line(start_x, start_y, end_x, end_y)

            for x, y in line_coords:
                canvas.create_rectangle(x, y, x + 1, y + 1, fill="black")
                print(f"({x}, {y})")
                output_text.insert(tk.END, f'({x}, {y})\n') 

            click_num = 0
    label1 = tk.Label(dda_m, text="DDA",fg="white", bg='#203A43')
    label1.pack()
    output_text =scrolledtext.ScrolledText(dda_m, height=5, width=40)
    output_text.pack()
    Dlabel = tk.Label(dda_m, text="Draw Manually:-",fg="white", bg='#203A43')
    Dlabel.pack()
    canvas = tk.Canvas(dda_m, width=400, height=300, bg='white')
    
    canvas.pack()
    

    canvas.bind("<Button-1>", draw_line)


def open_dda_auto():
    def draw_line():
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())

        line_coords = dda_line(x1, y1, x2, y2)

        for x, y in line_coords:
            canvas.create_rectangle(x, y, x + 1, y + 1, fill="black")
            print(f"({x}, {y})")
            output_text.insert(tk.END, f'({x}, {y})\n') 
            

    dda_w = tk.Toplevel(pro)
    dda_w.title("dda Algorithms")
    dda_w.geometry('400x600+500+100')
    dda_w.configure(bg='#203A43')

    label_x1 = tk.Label(dda_w, text="x1:",fg="white", bg='#203A43')
    label_x1.pack()
    entry_x1 = tk.Entry(dda_w,borderwidth=5)
    entry_x1.pack()

    label_y1 = tk.Label(dda_w, text="y1:", fg="white",bg='#203A43')
    label_y1.pack()
    entry_y1 = tk.Entry(dda_w,borderwidth=5)
    entry_y1.pack()

    label_x2 = tk.Label(dda_w, text="x2:",fg="white", bg='#203A43')
    label_x2.pack()
    entry_x2 = tk.Entry(dda_w,borderwidth=5)
    entry_x2.pack()

    label_y2 = tk.Label(dda_w, text="y2:",fg="white", bg='#203A43')
    label_y2.pack()
    entry_y2 = tk.Entry(dda_w,borderwidth=5)
    entry_y2.pack()

    draw_button = tk.Button(dda_w, text="Draw",fg="white",borderwidth=5,
                            command=draw_line, bg='#203A43')
    draw_button.pack()

    

    
    output_text =scrolledtext.ScrolledText(dda_w, height=5, width=40)
    output_text.pack()
    canvas = tk.Canvas(dda_w, width=400, height=300, bg='white')
    canvas.pack()
    



def open_bresenham_man():
    bresenham_m = tk.Toplevel(pro)
    bresenham_m.title("Manual BRESENHAM")
    bresenham_m.geometry('500x500+500+100')
    bresenham_m.configure(bg='#203A43')
    click_num = 0

    def draw_bresenham(event):
        nonlocal click_num  
        global start_x, start_y, end_x, end_y

        if click_num == 0:
            start_x = event.x
            start_y = event.y
            click_num = 1
        else:
            end_x = event.x
            end_y = event.y

            line_coords = bresenham_line(start_x, start_y, end_x, end_y)

            for x, y in line_coords:
                canvas.create_rectangle(x, y, x + 1, y + 1, fill="black")
                print(f"({x}, {y})")
                output_text.insert(tk.END, f'({x}, {y})\n') 
            click_num = 0

    label1 = tk.Label(bresenham_m, text="Bresenham", fg="white", bg='#203A43')
    label1.pack()
    output_text = scrolledtext.ScrolledText(bresenham_m, height=5, width=40)
    output_text.pack()
    Dlabel = tk.Label(bresenham_m, text="Draw Manually:-", fg="white", bg='#203A43')
    Dlabel.pack()
    canvas = tk.Canvas(bresenham_m, width=400, height=300, bg='white')
    canvas.pack()
    canvas.bind("<Button-1>", draw_bresenham)


def open_bresenham_auto():
    def draw_bresenham():
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())

        line_coords = bresenham_line(x1, y1, x2, y2)

        for x, y in line_coords:
            canvas.create_rectangle(x, y, x + 1, y + 1, fill="black")
            print(f"({x}, {y})")
            output_text.insert(tk.END, f'({x}, {y})\n') 
    bresenham_w = tk.Toplevel(pro)
    bresenham_w.title("Bresenham Algorithm")
    bresenham_w.geometry('400x600+500+100')
    bresenham_w.configure(bg='#203A43')
    label_x1 = tk.Label(bresenham_w, text="x1:",fg="white", bg='#203A43')
    label_x1.pack()
    entry_x1 = tk.Entry(bresenham_w,borderwidth=5)
    entry_x1.pack()

    label_y1 = tk.Label(bresenham_w, text="y1:",fg="white", bg='#203A43')
    label_y1.pack()
    entry_y1 = tk.Entry(bresenham_w,borderwidth=5)
    entry_y1.pack()

    label_x2 = tk.Label(bresenham_w, text="x2:",fg="white", bg='#203A43')
    label_x2.pack()
    entry_x2 = tk.Entry(bresenham_w,borderwidth=5)
    entry_x2.pack()

    label_y2 = tk.Label(bresenham_w, text="y2:",fg="white", bg='#203A43')
    label_y2.pack()
    entry_y2 = tk.Entry(bresenham_w,borderwidth=5)
    entry_y2.pack()
    draw_button = tk.Button(bresenham_w, text="Draw", borderwidth=5,command=draw_bresenham, bg='white')
    draw_button.pack()
    
    output_text =scrolledtext.ScrolledText(bresenham_w, height=5, width=40)
    output_text.pack()
    canvas = tk.Canvas(bresenham_w, width=400, height=400, bg='white')
    canvas.pack()
   


def open_midpoint_man():
    midpoint_m = tk.Toplevel(pro)
    midpoint_m.title("Manual Midpoint")
    midpoint_m.geometry('400x400+500+100')
    midpoint_m.configure(bg='#203A43')
    click_num = 0

    def draw_line(event):
        nonlocal click_num  
        global start_x, start_y, end_x, end_y

        if click_num == 0:
            start_x = event.x
            start_y = event.y
            click_num = 1
        else:
            end_x = event.x
            end_y = event.y

            line_coords = midpoint_line(start_x, start_y, end_x, end_y)

            for x, y in line_coords:
                canvas.create_rectangle(x, y, x + 1, y + 1, fill="black")
                print(f"({x}, {y})")
                output_text.insert(tk.END, f'({x}, {y})\n')   

            click_num = 0
    label1 = tk.Label(midpoint_m, text="DDA",fg="white", bg='#203A43')
    label1.pack()
    output_text =scrolledtext.ScrolledText(midpoint_m, height=5, width=40)
    output_text.pack()
    Dlabel = tk.Label(midpoint_m, text="Draw Manually:-",fg="white", bg='#203A43')
    Dlabel.pack()
    canvas = tk.Canvas(midpoint_m, width=400, height=300, bg='white')
    canvas.pack()

    canvas.bind("<Button-1>", draw_line)


def open_midpoint_auto():

    def draw_midpoint():
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())

        line_coords = midpoint_line(x1, y1, x2, y2)

        for x, y in line_coords:
            canvas.create_rectangle(x, y, x + 1, y + 1, fill="black")
            print(f"({x}, {y})")
            output_text.insert(tk.END, f'({x}, {y})\n') 
    midpoint_w = tk.Toplevel(pro)
    midpoint_w.title("Midpoint Algorithms")
    midpoint_w.geometry('400x600+500+100')
    midpoint_w.configure(bg='#203A43')

    label_x1 = tk.Label(midpoint_w, text="x1:",fg="white", bg='#203A43')
    label_x1.pack()
    entry_x1 = tk.Entry(midpoint_w,borderwidth=5)
    entry_x1.pack()

    label_y1 = tk.Label(midpoint_w, text="y1:",fg="white", bg='#203A43')
    label_y1.pack()
    entry_y1 = tk.Entry(midpoint_w,borderwidth=5)
    entry_y1.pack()

    label_x2 = tk.Label(midpoint_w, text="x2:",fg="white", bg='#203A43')
    label_x2.pack()
    entry_x2 = tk.Entry(midpoint_w,borderwidth=5)
    entry_x2.pack()

    label_y2 = tk.Label(midpoint_w, text="y2:",fg="white", bg='#203A43')
    label_y2.pack()
    entry_y2 = tk.Entry(midpoint_w,borderwidth=5)
    entry_y2.pack()
    draw_button = tk.Button(midpoint_w, text="Draw",borderwidth=5,
                            command=draw_midpoint, bg='white')
    draw_button.pack()
    output_text =scrolledtext.ScrolledText(midpoint_w, height=5, width=40)
    output_text.pack()
    canvas = tk.Canvas(midpoint_w, width=400, height=400, bg='white')
    canvas.pack()


def open_cohen_sutherland_clip_auto():
    def draw_cohen_sutherland():
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())

        my_canvas.create_line(x1, y1, x2, y2, fill='red', width=3)

        code1 = computeCode(x1, y1)
        code2 = computeCode(x2, y2)
        accept = False

        while True:
            if code1 == 0 and code2 == 0:
                accept = True
                break
            elif (code1 & code2) != 0:
                break
            else:
                x = 1.0
                y = 1.0
                if code1 != 0:
                    code_out = code1
                else:
                    code_out = code2
                if code_out & TOP:
                    x = x1 + ((x2 - x1) / (y2 - y1)) * (y_max - y1)
                    y = y_max
                elif code_out & BOTTOM:
                    x = x1 + ((x2 - x1) / (y2 - y1)) * (y_min - y1)
                    y = y_min
                elif code_out & RIGHT:
                    y = y1 + ((y2 - y1) / (x2 - x1)) * (x_max - x1)
                    x = x_max
                elif code_out & LEFT:
                    y = y1 + ((y2 - y1) / (x2 - x1)) * (x_min - x1)
                    x = x_min

                if code_out == code1:
                    x1 = x
                    y1 = y
                    code1 = computeCode(x1, y1)
                else:
                    x2 = x
                    y2 = y
                    code2 = computeCode(x2, y2)

        if accept:
            print("Line accepted from %.2f, %.2f to %.2f, %.2f" %(x1, y1, x2, y2))
            my_canvas.create_line(x1, y1, x2, y2, fill='blue',  width=3)
            output_text.insert(tk.END,"Line accepted from %.2f, %.2f to %.2f, %.2f\n" %(x1, y1, x2, y2))
        else:
            print("Line rejected\n")
            output_text.insert(tk.END,"Line rejected\n")

    my_window = tk.Toplevel(pro)
    my_window.title("Cohen-Sutherland Clip Auto")
    my_window.geometry('600x800+500+20')
    my_window.configure(bg='#203A43')
    label_x1 = tk.Label(my_window, text="x1:",fg="white", bg='#203A43')
    label_x1.pack()
    entry_x1 = tk.Entry(my_window,borderwidth=5)
    entry_x1.pack()

    label_y1 = tk.Label(my_window, text="y1:",fg="white", bg='#203A43')
    label_y1.pack()
    entry_y1 = tk.Entry(my_window,borderwidth=5)
    entry_y1.pack()

    label_x2 = tk.Label(my_window, text="x2:",fg="white", bg='#203A43')
    label_x2.pack()
    entry_x2 = tk.Entry(my_window,borderwidth=5)
    entry_x2.pack()

    label_y2 = tk.Label(my_window, text="y2:",fg="white", bg='#203A43')
    label_y2.pack()
    entry_y2 = tk.Entry(my_window,borderwidth=5)
    entry_y2.pack()

    draw_button = tk.Button(my_window, text="Draw Line",
                            command=draw_cohen_sutherland,borderwidth=5, bg='white')
    draw_button.pack()
    output_text =scrolledtext.ScrolledText(my_window, height=5, width=50)
    output_text.pack()
    my_canvas = tk.Canvas(my_window, width=400, height=400, bg='white')
    my_canvas.pack()

    # Rectangle
    my_canvas.create_line(x_min, y_min, x_max, y_min, fill='black')  # Top line
    my_canvas.create_line(x_max, y_min, x_max, y_max, fill='black')  # Right line
    my_canvas.create_line(x_max, y_max, x_min, y_max,fill='black')  # Bottom line
    my_canvas.create_line(x_min, y_max, x_min, y_min,fill='black')  # Left line

    my_window.mainloop()


def computeCode(x, y):
    code = INSIDE
    if x < x_min:  # to the left of rectangle
        code |= LEFT
    elif x > x_max:  # to the right of rectangle
        code |= RIGHT
    if y < y_min:  # below the rectangle
        code |= BOTTOM
    elif y > y_max:  # above the rectangle
        code |= TOP

    print(code)
    return code


def open_cohen_sutherland_clip_man():
    cohen_sutherland_clip_man = tk.Toplevel(pro)

    cohen_sutherland_clip_man.title("Cohen sutherland clip manual")
    cohen_sutherland_clip_man.geometry('600x700+500+20')
    cohen_sutherland_clip_man.configure(bg='#203A43')

    def draw_line(event):
        global start_x, start_y, end_x, end_y

        if start_x is None:
            start_x = event.x
            start_y = event.y
        else:
            end_x = event.x
            end_y = event.y

            my_canvas.create_line(start_x, start_y, end_x, end_y, fill='red', width=3)

            code1 = computeCode(start_x, start_y)
            code2 = computeCode(end_x, end_y)
            accept = False

            while True:
                # If both endpoints are in the rectangle
                if code1 == 0 and code2 == 0:
                    accept = True
                    break
                # If both endpoints are outside the rectangle
                elif (code1 & code2) != 0:
                    break
                # Some segment lies within the rectangle
                else:
                    x = 1.0
                    y = 1.0
                    if code1 != 0:
                        code_out = code1
                    else:
                        code_out = code2
                    # Find intersection point
                    if code_out & TOP:
                        # point is above the clip rectangle
                        x = start_x + ((end_x - start_x) /
                                       (end_y - start_y)) * (y_max - start_y)
                        y = y_max
                    elif code_out & BOTTOM:
                        # point is below the clip rectangle
                        x = start_x + ((end_x - start_x) /
                                       (end_y - start_y)) * (y_min - start_y)
                        y = y_min
                    elif code_out & RIGHT:
                        # point is to the right of the clip rectangle
                        y = start_y + ((end_y - start_y) /
                                       (end_x - start_x)) * (x_max - start_x)
                        x = x_max
                    elif code_out & LEFT:
                        # point is to the left of the clip rectangle
                        y = start_y + ((end_y - start_y) /
                                       (end_x - start_x)) * (x_min - start_x)
                        x = x_min

                    # We replace point outside clipping rectangle by intersection point
                    if code_out == code1:
                        start_x = x
                        start_y = y
                        code1 = computeCode(start_x, start_y)
                    else:
                        end_x = x
                        end_y = y
                        code2 = computeCode(end_x, end_y)

            if accept:
                print("Line accepted from %.2f, %.2f to %.2f, %.2f\n" %(start_x, start_y, end_x, end_y))
                my_canvas.create_line(
                    start_x, start_y, end_x, end_y, fill='blue', width=3)
                output_text.insert(tk.END,"Line accepted from %.2f, %.2f to %.2f, %.2f\n" % (start_x, start_y, end_x, end_y))
            else:
                print("Line rejected\n")
                output_text.insert(tk.END,"Line rejected\n")

            # Reset coordinates for the next line
            start_x, start_y, end_x, end_y = None, None, None, None
    label1 = tk.Label(cohen_sutherland_clip_man, text="Cohen-SutherLand:",fg="white", bg='#203A43')
    label1.pack()
    output_text =scrolledtext.ScrolledText(cohen_sutherland_clip_man, height=5, width=50)
    output_text.pack()
    label1 = tk.Label(cohen_sutherland_clip_man, text="Draw Manually:-",fg="white", bg='#203A43')
    label1.pack()
    my_canvas = Canvas(cohen_sutherland_clip_man, width=400, height=400,background="white")
    my_canvas.pack()
    
    my_canvas.bind("<Button-1>", draw_line)

    # Rectangle
    x1 = 50  # Top-left x coordinate
    y1 = 100  # Top-left y coordinate
    x2 = 350  # Bottom-right x coordinate
    y2 = 300  # Bottom-right y coordinate
    my_canvas.create_line(x1, y1, x2, y1, fill='black')  # Top line
    my_canvas.create_line(x2, y1, x2, y2, fill='black')  # Right line
    my_canvas.create_line(x2, y2, x1, y2, fill='black')  # Bottom line
    my_canvas.create_line(x1, y2, x1, y1, fill='black')  # Left line

    cohen_sutherland_clip_man.mainloop()

    midpoint_m = tk.Toplevel(pro)
    midpoint_m.title("Manual Midpoint")

    def draw_line(event):
        global start_x, start_y, end_x, end_y

        if start_x is None:
            start_x = event.x
            start_y = event.y
        else:
            end_x = event.x
            end_y = event.y
            my_canvas.create_line(start_x, start_y, end_x, end_y, fill='red', width=3)

            code1 = computeCode(start_x, start_y)
            code2 = computeCode(end_x, end_y)
            accept = False

            while True:
                # If both endpoints lie within rectangle
                if code1 == 0 and code2 == 0:
                    accept = True
                    break
                # If both endpoints are outside rectangle
                elif (code1 & code2) != 0:
                    break
                # Some segment lies within the rectangle
                else:
                    x = 1.0
                    y = 1.0
                    if code1 != 0:
                        code_out = code1
                    else:
                        code_out = code2
                    if code_out & TOP:

                        # point is above the clip rectangle
                        x = start_x + ((end_x - start_x) /
                                       (end_y - start_y)) * (y_max - start_y)
                        y = y_max
                    elif code_out & BOTTOM:

                        # point is below the clip rectangle
                        x = start_x + ((end_x - start_x) /
                                       (end_y - start_y)) * (y_min - start_y)
                        y = y_min

                    elif code_out & RIGHT:

                        # point is to the right of the clip rectangle
                        y = start_y + ((end_y - start_y) /
                                       (end_x - start_x)) * (x_max - start_x)
                        x = x_max

                    elif code_out & LEFT:

                        # point is to the left of the clip rectangle
                        y = start_y + ((end_y - start_y) /
                                       (end_x - start_x)) * (x_min - start_x)
                        x = x_min

                    # We replace point outside clipping rectangle by intersection point
                    if code_out == code1:
                        start_x = x
                        start_y = y
                        code1 = computeCode(start_x, start_y)

                    else:
                        end_x = x
                        end_y = y
                        code2 = computeCode(end_x, end_y)

            if accept:
                print("Line accepted from %.2f, %.2f to %.2f, %.2f\n" %(start_x, start_y, end_x, end_y))
                my_canvas.create_line(start_x, start_y, end_x, end_y, fill='blue', width=3)

            else:
                print("Line rejected\n")

            # Reset coordinates for the next line
            start_x, start_y, end_x, end_y = None, None, None, None
    my_canvas = Canvas(cohen_sutherland_clip_man, width=400, height=400)

    my_canvas.grid(row=6, column=0)

    my_canvas.bind("<Button-1>", draw_line)
    # Rectangle
    x1 = 50  # Top-left x coordinate
    y1 = 100  # Top-left y coordinate
    x2 = 350  # Bottom-right x coordinate
    y2 = 300  # Bottom-right y coordinate
    my_canvas.create_line(x1, y1, x2, y1, fill='black')  # Top line
    my_canvas.create_line(x2, y1, x2, y2, fill='black')  # Right line
    my_canvas.create_line(x2, y2, x1, y2, fill='black')  # Bottom line
    my_canvas.create_line(x1, y2, x1, y1, fill='black')  # Left line


def open_liang_auto():
    global full_line
    full_line=None
    
    def draw_clipping_rectangle():
    # Draw the clipping rectangle
        x1, y1, x2, y2 = x_min, y_min, x_max, y_max
        canvas.create_line(x1, y1, x2, y1, fill='black')
        canvas.create_line(x2, y1, x2, y2, fill='black')
        canvas.create_line(x2, y2, x1, y2, fill='black')
        canvas.create_line(x1, y2, x1, y1, fill='black')
    
    def clip_line():
        global full_line
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())

        # Clear previous drawings on the canvas
        canvas.delete("all")
        
        draw_clipping_rectangle()

        full_line = canvas.create_line(x1, y1, x2,y2, fill='red', width=2)

        clipped_line = liang_barsky_clip(x1,y1, x2,y2)

        if clipped_line:
            print(f"Line accepted from {clipped_line[0]:.2f}, {clipped_line[1]:.2f} to {clipped_line[2]:.2f}, {clipped_line[3]:.2f}\n")
            canvas.create_line(clipped_line[0], clipped_line[1], clipped_line[2], clipped_line[3], fill='blue', width=2)
            output_text.insert(tk.END,f"Line accepted from {clipped_line[0]:.2f}, {clipped_line[1]:.2f} to {clipped_line[2]:.2f}, {clipped_line[3]:.2f}\n")
        else:
            print("Line rejected\n")
            output_text.insert(tk.END,"Line rejected\n")
    def delete_line():
        canvas.delete(full_line)

    clip_liang_auto = tk.Toplevel(pro)
    clip_liang_auto.title("Liang Algorithm")
    clip_liang_auto.configure(bg='#203A43')
    clip_liang_auto.geometry('600x800+500+0')
    

    tk.Label(clip_liang_auto, text="Enter point x1:",fg='white',bg='#203A43').pack()
    entry_x1 = tk.Entry(clip_liang_auto, width=20,borderwidth=5)
    entry_x1.pack()

    tk.Label(clip_liang_auto, text="Enter point y1:",fg='white',bg='#203A43').pack()
    entry_y1 = tk.Entry(clip_liang_auto, width=20,borderwidth=5)
    entry_y1.pack()

    tk.Label(clip_liang_auto, text="Enter point x2:",fg='white',bg='#203A43').pack()
    entry_x2 = tk.Entry(clip_liang_auto, width=20,borderwidth=5)
    entry_x2.pack()

    tk.Label(clip_liang_auto, text="Enter point y2:",fg='white',bg='#203A43').pack()
    entry_y2 = tk.Entry(clip_liang_auto, width=20,borderwidth=5)
    entry_y2.pack()
    output_text =scrolledtext.ScrolledText(clip_liang_auto, height=5, width=50)
    output_text.pack()
    canvas = tk.Canvas(clip_liang_auto, width=400, height=350,bg='white')
    canvas.pack()
    draw_clipping_rectangle()

    tk.Button(clip_liang_auto, text="Submit points", width=25, borderwidth=5, command=clip_line).pack()
    tk.Button(clip_liang_auto, text="Clip", width=25, borderwidth=5, command=delete_line).pack()

    

def open_liang_man():
    liang_clip_man = tk.Toplevel(pro)
    liang_clip_man.title("liang clip manual")
    liang_clip_man.configure(bg='#203A43')
    label1 = tk.Label(liang_clip_man, text="liang Barsky:",fg="white", bg='#203A43')
    label1.pack()
    output_text =scrolledtext.ScrolledText(liang_clip_man, height=5, width=50)
    output_text.pack()
    label1 = tk.Label(liang_clip_man, text="Draw Manually:-",fg="white", bg='#203A43')
    label1.pack()
    my_canvas = Canvas(liang_clip_man, width=400, height=400,background="white")
    my_canvas.pack()
    def draw_line(event):
        global start_x, start_y, end_x, end_y

        if start_x is None:
            start_x = event.x
            start_y = event.y
        else:
            end_x = event.x
            end_y = event.y

        my_canvas.create_line(start_x, start_y, end_x, end_y, fill='red', width=3)

        clipped_line = liang_barsky_clip(start_x, start_y, end_x, end_y)

        if clipped_line:
            start_x, start_y, end_x, end_y = clipped_line
            my_canvas.create_line(start_x, start_y, end_x, end_y, fill='blue', width=3)
            print("Line accepted from %.2f, %.2f to %.2f, %.2f\n" % (start_x, start_y, end_x, end_y))
            output_text.insert(tk.END,"Line accepted from %.2f, %.2f to %.2f, %.2f\n" % (start_x, start_y, end_x, end_y))
        else:
            print("Line rejected\n")
            output_text.insert(tk.END,"Line rejected\n")

        # Reset coordinates for the next line
        start_x, start_y, end_x, end_y = None, None, None, None

    my_canvas.bind("<Button-1>", draw_line)

    # Rectangle
    x1 = 50  # Top-left x coordinate
    y1 = 100  # Top-left y coordinate
    x2 = 350  # Bottom-right x coordinate
    y2 = 300  # Bottom-right y coordinate
    my_canvas.create_line(x1, y1, x2, y1, fill='black')  # Top line
    my_canvas.create_line(x2, y1, x2, y2, fill='black')  # Right line
    my_canvas.create_line(x2, y2, x1, y2, fill='black')  # Bottom line
    my_canvas.create_line(x1, y2, x1, y1, fill='black')  # Left line

def draw_square(x, y):
    my_turtle = turtle.Turtle()
    my_turtle.speed(7)
    my_turtle.pensize(3)  
    my_turtle.pencolor("blue")
    my_turtle.penup()  
    my_turtle.goto(x, y)  
    my_turtle.pendown()  
    for _ in range(4):
        my_turtle.forward(100)  
        my_turtle.right(90)


def draw_it():
    turtle.onscreenclick(draw_square)  
    turtle.done()


def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps
    coords = []
    x, y = x1, y1
    for i in range(steps + 1):
        coords.append((round(x), round(y)))
        x += x_increment
        y += y_increment
    return coords


def bresenham_line(x0, y0, x1, y1):
    # Bresenham's line algorithm
    line_coords = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while x0 != x1 or y0 != y1:
        line_coords.append((x0, y0))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    line_coords.append((x1, y1))
    return line_coords

def midpoint_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy <= dx
    if not slope:
        dx, dy = dy, dx
    p = dy - dx
    coords = []
    x, y = x1, y1
    for i in range(dx + 1):
        coords.append((x, y))
        if p >= 0:
            if slope:
                y += 1 if y < y2 else -1
            else:
                x += 1 if x < x2 else -1
            p -= 2 * dx
        if slope:
            x += 1 if x < x2 else -1
        else:
            y += 1 if y < y2 else -1
        p += 2 * dy
    return coords

def liang_barsky_clip(x1, y1, x2, y2):
    u1, u2 = 0.0, 1.0
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - x_min, x_max - x1, y1 - y_min, y_max - y1]

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None
        else:
            r = q[i] / p[i]
            if p[i] < 0:
                if r > u2:
                    return None
                elif r > u1:
                    u1 = r
            elif p[i] > 0:
                if r < u1:
                    return None
                elif r < u2:
                    u2 = r

    if u1 < u2:
        clipped_x1 = x1 + u1 * dx
        clipped_y1 = y1 + u1 * dy
        clipped_x2 = x1 + u2 * dx
        clipped_y2 = y1 + u2 * dy

        return [clipped_x1, clipped_y1, clipped_x2, clipped_y2]
    else:
        return None
    
pro = tk.Tk()
pro.title('Line Algorithmes')
pro.geometry('250x230+483+234')
pro.resizable(False, False)

btn1 = tk.Button(pro, text='Automatic', fg='#FFF8E7', bg='#203A43', width=15, height=3, borderwidth=5, font='Helvetica, 13', command=open_auto_window)
btn1.place(x=47, y=20)
btn2 = tk.Button(pro, text='Manual', fg='#FFF8E7', bg='#203A43', width=15, height=3, borderwidth=5, font='Helvetica, 13', command=open_manual_window)
btn2.place(x=47, y=130)
pro.mainloop()
