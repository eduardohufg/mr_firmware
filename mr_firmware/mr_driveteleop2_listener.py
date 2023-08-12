#Declare libraries
import rclpy
from .submodules.lx16a import *
#from lx16a import *
from math import *
from std_msgs.msg import *
from geometry_msgs.msg import Twist
from numpy import*
from rclpy.node import Node

class DTeleopListener(Node):
    
    def __init__(self):
        # Init the node
        super().__init__('listener_drive_teleop')
        # Subscribe to a topic named "Received Angle" and call the function "callback"
        self.subscriber = self.create_subscription(Twist,"cmd_vel",self.swerve_mover,10)
        self.subscriber
        # Select the correct port, otherwise, the program wont continue
        LX16A.initialize("/dev/SERVO_CONTROLLER")
        # Define the servos, remember you had to set the ID before.
        self.servo1 = LX16A(1)
        self.servo3 = LX16A(3)
        self.servo5 = LX16A(5)
        self.servo7 = LX16A(7)
        self.servo2 = LX16A(2)
        self.servo4 = LX16A(4)
        self.servo6 = LX16A(6)
        self.servo8 = LX16A(8)
        # Define the mode, in this case, servoMode
        self.servo2.servoMode()
        self.servo4.servoMode()
        self.servo6.servoMode()
        self.servo8.servoMode()

    def my_map(self,x,in_min,in_max,out_min,out_max):
        x = int(x)
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def angulos(self,servo,data,min,max):
        grados=degrees(data)
        angulo=int(self.my_map(grados,-90,90,min,max))
        if angulo<240:
            angulo=240
        elif angulo>0:
            angulo=0
        servo.moveTimeWrite(angulo)

    def swerve_mover(self,data):
        if((data.linear.x>0.1 or data.linear.x<-0.1) and abs(data.linear.y)<0.8 and abs(data.angular.z <0.8)):
            print("Avanzando")
            # Print the received data
            
            self.servo2.moveTimeWrite(120)
            self.servo4.moveTimeWrite(145)
            self.servo6.moveTimeWrite(165)
            self.servo8.moveTimeWrite(180)
            self.servo1.motorMode(-int((data.linear.x)*1000))
            self.servo3.motorMode(-int((data.linear.x)*1000))
            self.servo5.motorMode(int((data.linear.x)*1000))
            self.servo7.motorMode(int((data.linear.x)*1000))
        elif(abs(data.angular.z)>=0.1) and abs(data.linear.x)<0.8:
            print("Rotando")
            #self.angulos(self.servo2,120,30,210)
            #self.angulos(self.servo4,145,55,235)
            #self.angulos(self.servo6,165,72,252)
            #self.angulos(self.servo8,50,-40,180)
            self.servo2.moveTimeWrite(165)
            self.servo4.moveTimeWrite(100)
            self.servo6.moveTimeWrite(120)
            self.servo8.moveTimeWrite(225)
            self.servo1.motorMode(int((data.angular.z)*1000))
            self.servo3.motorMode(int((data.angular.z)*1000))
            self.servo5.motorMode(int((data.angular.z)*1000))
            self.servo7.motorMode(int((data.angular.z)*1000))
        elif(abs(data.linear.x)<0.8 and abs(data.linear.y)>0.3 and abs(data.angular.z) <0.8):
            print("lado")
            # Print the received data
            #self.servo1.motorMode(-int((data.linear.x+data.angular.z)*1000))
            #self.servo3.motorMode(-int((data.linear.x+data.angular.z)*1000))
            #self.servo5.motorMode(int((data.linear.x-data.angular.z)*1000))
            #self.servo7.motorMode(int((data.linear.x-data.angular.z)*1000))
            self.servo2.moveTimeWrite(210)
            self.servo4.moveTimeWrite(55)
            self.servo6.moveTimeWrite(75)
            self.servo8.moveTimeWrite(90)

            self.servo1.motorMode(int((data.linear.y)*1000))
            self.servo3.motorMode(-int((data.linear.y)*1000))
            self.servo5.motorMode(-int((data.linear.y)*1000))
            self.servo5.motorMode(int((data.linear.y)*1000))
            #self.servo7.motorMode(int((data.linear.x-data.angular.z)*1000))

            #self.servo2.moveTimeWrite(90*(abs(data.linear.y)/(data.linear.y)))
            #self.servo4.moveTimeWrite(90*(abs(data.linear.y)/(data.linear.y)))
            #self.servo6.moveTimeWrite(90*(abs(data.linear.y)/(data.linear.y)))
            #self.servo8.moveTimeWrite(90*(abs(data.linear.y)/(data.linear.y)))
        elif(data.linear.x == 0 and data.angular.z==0 and data.linear.y==0):
            #self.servo1.motorMode(-int(0))
            #self.servo3.motorMode(-int(0))
            #self.servo5.motorMode(int((0)))
            #self.servo7.motorMode(int((0)))
            self.servo2.moveTimeWrite(120)
            self.servo4.moveTimeWrite(145)
            self.servo6.moveTimeWrite(165)
            self.servo8.moveTimeWrite(180)
            self.servo1.motorMode(0)
            self.servo3.motorMode(0)
            self.servo5.motorMode(0)
            self.servo7.motorMode(0)

def main(args=None):
    rclpy.init(args=args)
    listener=DTeleopListener()
    rclpy.spin(listener)
    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    print("Escuchando")
    main()
