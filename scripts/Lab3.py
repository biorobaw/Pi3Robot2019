#!/usr/bin/env python

import rospy
import Lab3Tasks
import SetSpeeds
from Tkinter import *
from robot_client.srv import RunFunction
from robot_client.srv import RunFunctionRequest
from robot_client.srv import RunFunctionResponse

rospy.wait_for_service('pi3_robot_2019/r1/run_function')
run_function = rospy.ServiceProxy('pi3_robot_2019/r1/run_function', RunFunction)

def on_shutdown():
    rospy.loginfo("Shutting down")
    SetSpeeds.setspeeds(0,0)
    result = run_function("init_camera",["kill"])
    print(result)
    rate.sleep()

#==========================GUI STUFF================
class Resolution_GUI(Frame):
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Enter width x height and quality    \n"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(row=0, column=0,ipadx=150, ipady=150, sticky="ew")

        self.w = IntVar()
        self.w.set(320)
        self.entry1 = Entry(self)
        self.entry1["textvariable"] = self.w
        self.entry1.grid(row=1,ipadx=100, ipady=25, sticky="ew")
        
        self.h = IntVar()
        self.h.set(240)
        self.entry2 = Entry(self)
        self.entry2["textvariable"] = self.h
        self.entry2.grid(row=2,ipadx=100, ipady=25, sticky="ew")
        
        self.q = IntVar()
        self.q.set(100)
        self.entry3 = Entry(self)
        self.entry3["textvariable"] = self.q
        self.entry3.grid(row=3,ipadx=100, ipady=25, sticky="ew")
           

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
class Application(Frame):
    function = ""
    def Task1(self):
        self.function = "Task1"
        self.quit()
    def Task2(self):
        self.function = "Task2"
        self.quit()
    def Task3(self):
        self.function = "Task3"
        self.quit()
    def Task4(self):
        self.function = "Task4"
        self.quit()
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT    \n"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(row=0, column=0,ipadx=150, ipady=150, sticky="ew")

        
        self.T1 = Button(self)
        self.T1["text"] = "Task1\n(Goal Facing)"
        self.T1.grid(row=0, column=1,ipadx=150, ipady=150, sticky="ew")
        self.T1["command"] =  self.Task1
        
        self.T2 = Button(self)
        self.T2["text"] = "Task2\n(Motion to Goal)"
        self.T2.grid(row=0, column=2,ipadx=150, ipady=150, sticky="ew")

        self.T2["command"] =  self.Task2
        
        self.T3 = Button(self)
        self.T3["text"] = "Task3\n(Triangulation)"
        self.T3.grid(row=1, column=0,ipadx=150, ipady=150, sticky="ew")

        self.T3["command"] =  self.Task3
         
         
        self.T4 = Button(self)
        self.T4["text"] = "Task4\n(Bug Algorithm)"
        self.T4.grid(row=1, column=1,ipadx=150, ipady=150, sticky="ew")

        self.T4["command"] =  self.Task4
           

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        

if __name__ == '__main__':
    
    try:
        rospy.init_node('lab_3', anonymous=True)
        rospy.on_shutdown(on_shutdown)
        rate = rospy.Rate(10) # 10hz
        root = Tk()
        res = Resolution_GUI(master=root)
        res.mainloop()
        res.destroy()
        if(res.w.get()==0 or res.w.get()==0 or res.q.get()==0):
            root.destroy()
            raise Exception('Not valid resolution')
        else:
            result = run_function("init_camera",[str(res.w.get()),str(res.h.get()),str(res.q.get())])
            print(result)
        
        app = Application(master=root)
        app.mainloop()
        root.destroy()
        if(app.function ==""):
            print("pass")
            pass

        elif(app.function =="Task1"):
            Lab3Tasks.Task1()
        elif(app.function =="Task2"):
            Lab3Tasks.Task2()
        elif(app.function =="Task3"):
            Lab3Tasks.Task3Main()
        elif(app.function =="Task4"):
            Lab3Tasks.Task4()
    except Exception as e:
        print(e)

    
