"""
GUI Animation
"""
import numpy as np
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import math
import pandas as pd

# Load the CSV files "marathon_results_2015 ~ 2017.csv" under "data" folder
marathon_2015_2017 = pd.read_csv("./data/marathon_2015_2017.csv")

# Merge 2015, 2016 and 2017 files into marathon_2015_2017 file index by Official Time
record = pd.DataFrame(marathon_2015_2017,columns=['5K',  '10K',  '15K',  '20K', 'Half',  '25K',  '30K',  '35K',  '40K',  'Official Time']).sort_values(by=['Official Time'])

# Dataframe to List
record_list = record.values.tolist()

xData = [5, 10, 15, 20, 21.098, 25, 30, 35, 40, 42.195 ]

fig = Figure(figsize=(5,4), dpi=100)
ax = fig.add_subplot(111)
t_xdata, t_ydata = [], []
ax.set_xlim(0, 45) # 영역 제한
ax.set_ylim(0, 10000)
dn, = ax.plot([], [], 'ro')
t_a = 0

def seconds_to_hhmmss(seconds): # 초단위 -> 시간 형태
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)

def init():
    ax.set_xlim(0, 45)
    ax.set_ylim(0, 10000)
    return dn, 

def animateFrame(frame):
    t_a = int(t_aSpbox.get()) -1
    t_x = xData[int(frame)]
    t_y = record_list[t_a][int(frame)]
    t_xdata.append(t_x)
    t_ydata.append(t_y)
    dn.set_data(t_xdata, t_ydata) 
    return dn,

def update():
    t_a = int(t_aSpbox.get()) -1 # list에서 찾을거기 때문에 입력값 - 1
    ani = FuncAnimation(fig, animateFrame, frames=np.linspace(0, len(xData)-1, len(xData)),
                        init_func=init, blit=True) # 에니메이션 설정, animateFrame, init 함수 호출
    ax.set_xlabel('Distance(km)')
    ax.set_ylabel('Time(Second)')
    ax.set_title('Records of runner #'+str(t_a + 1)) 
    
    record_list_format = [seconds_to_hhmmss(s) for s in record_list[t_a]] # 시간형태로 변환
    for i, txt in enumerate(record_list_format):
        ax.annotate(txt, (xData[i], record_list[t_a][i]), fontsize=8)

    fig.canvas.draw()

#main
main = Tk()
main.title("Marathon Records")
main.geometry()

label=Label(main, text='Marathon Records')
label.config(font=("Courier", 18))
label.grid(row=0,column=0,columnspan=4)

t_aVal  = DoubleVar(value=1.0)

t_aSpbox = Spinbox(main, textvariable=t_aVal ,from_=0, to=len(record_list), increment=1, justify=RIGHT)
t_aSpbox.config(state='readonly')
t_aSpbox.grid(row=1,column=1)
t_aLabel=Label(main, text='Rank of runner : ')                
t_aLabel.grid(row=1,column=0)

Button(main,text="Run",width=20,height=3,command=lambda:update()).grid(row=1, column=2, columnspan=2, rowspan=1)

canvas = FigureCanvasTkAgg(fig, main)
canvas.get_tk_widget().grid(row=2,column=0,columnspan=3)

main.mainloop()
