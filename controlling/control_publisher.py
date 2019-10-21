import rospy
from std_msgs.msg import Float64
import Tkinter as tk
from Counter import Counter

steering_min_value =  9 #right
steering_max_value =  16 #left
current_steering_value = 12
steering_delta = 0.1

throttle_min_value = 13.6
throttle_max_value = 15
current_throttle_value = 13.6
throttle_delta = 0.01

steering = rospy.Publisher('steering', Float64, queue_size=10)
throttle = rospy.Publisher('throttle', Float64, queue_size=10)
rospy.init_node('control', anonymous=True)
rate = rospy.Rate(100) # 10hz


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=400,  height=400)

        self.label = tk.Label(self, text="last key pressed:  ", width=20)
        self.label.pack(fill="both", padx=100, pady=100)

        self.label.bind("<w>", self.on_wasd)
        self.label.bind("<a>", self.on_wasd)
        self.label.bind("<s>", self.on_wasd)
        self.label.bind("<d>", self.on_wasd)
        self.label.bind("<q>", self.on_wasd)
    
	self.steering_controller = Counter(12, 14, 10, 0.5)
	self.throttle_controller = Counter(13, 15, 13, 0.025)

        self.label.focus_set()
        self.label.bind("<1>", lambda event: self.label.focus_set())

    def on_wasd(self, event):
        #self.label.configure(text="last key pressed: " + event.keysym);
        if event.keysym == "q":
                self.throttle_controller.reset()
                self.steering_controller.reset()

        if event.keysym == "w":  # increase velocity 
		self.throttle_controller.increase()

        if event.keysym == "s":
		self.throttle_controller.decrease()

        if event.keysym == "a":
	    	self.steering_controller.increase()

        if event.keysym == "d":
	    	self.steering_controller.decrease()

	steering.publish(float(self.steering_controller.initial_value))
	throttle.publish(float(self.throttle_controller.initial_value))

	rate.sleep()

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()

#if __name__ == '__main__':
#    try:
#        control()
#    except rospy.ROSInterruptException:
#        pass

