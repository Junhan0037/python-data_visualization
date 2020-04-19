"""
GUI Tkinter
"""
import numpy as np
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import pandas as pd

MAXVAL = 0
INTERVAL = 1000

fig = Figure(figsize=(5,4), dpi=100)
ax = fig.add_subplot(111) # 1x1그리드에 첫 번째 subplot

# Load the CSV files "marathon_results_2015 ~ 2017.csv" under "data" folder
marathon_2015_2017 = pd.read_csv("./data/marathon_2015_2017.csv")

# Merge 2015, 2016 and 2017 files into marathon_2015_2017 file index by Official Time
record = pd.DataFrame(marathon_2015_2017,columns=['5K',  '10K',  '15K',  '20K', 'Half',  '25K',  '30K',  '35K',  '40K',  'Official Time']).sort_values(by=['Official Time'])

# Dataframe to List
record_list = record.values.tolist()

xData = [5, 10, 15, 20, 21.098, 25, 30, 35, 40, 42.195 ]

def update():
    t_a = int(t_aSpbox.get()) # 입력창에 입력된 값 가져오기
    MAXVAL = t_a * INTERVAL # 천명 단위로 간격
    ax.set_xlabel('Distance(km)')
    ax.set_ylabel('Time(Second)')
    ax.set_title(str(t_a) + ' records of runners')
    
    for t in range(0, MAXVAL, INTERVAL):
        ax.plot(xData, record_list[int(t)], 'o', label=str(t+1))

    ax.legend()
    fig.canvas.draw()

#main
main = Tk() # tkinter 인스턴스화 (위젯 제작)
main.title("Marathon Records")
main.geometry() #  너비x높이 (기본값)

label=Label(main, text='Marathon Records')
label.config(font=("Courier", 18))
label.grid(row=0,column=0,columnspan=4) # row와 column을 이용하여 배치 및 span을 이용하여 크기조정

t_aVal  = DoubleVar(value=1.0) # 입력창

t_aSpbox = Spinbox(main, textvariable=t_aVal ,from_=0, to=100, increment=1, justify=RIGHT) # 증가, 감소 버튼
t_aSpbox.config(state='readonly')
t_aSpbox.grid(row=1,column=1)
t_aLabel=Label(main, text='Number of runner : ')
t_aLabel.grid(row=1,column=0)

Button(main,text="Run",width=20,height=5,command=lambda:update()).grid(row=1, column=2, columnspan=2, rowspan=1) # 버튼 (클릭시 update() 실행)

canvas = FigureCanvasTkAgg(fig, main)
canvas.get_tk_widget().grid(row=4,column=0,columnspan=3)

main.mainloop()
