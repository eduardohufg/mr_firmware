#Declare libraries
import rclpy
 # from lx16a import *
from math import *
from std_msgs.msg import *
from geometry_msgs.msg import Twist
from numpy import*
from rclpy.node import Node
'''
class Servos():
    def __init__(self,id):
        self.id =id
        self.value = 0
        self.status = "Static"
        self.mode ="Servo"
    def printing(self):
        if(self.mode=="Servo"):
            print(f"El servo {self.id} modo {self.status} tiene un angulo de {self.value}")
        else:
            print(f"El servo {self.id} modo {self.status} tiene una velocidad de {self.value}")
   '''  
class DTeleopListener(Node):
    
    def __init__(self):
        # Init the node
        super().__init__('listener_drive_teleop')
        # Subscribe to a topic named "Received Angle" and call the function "callback"
        self.subscriber = self.create_subscription(Twist,"cmd_vel",self.swerve_mover,10)
        self.subscriber

    def my_map(self,x,in_min,in_max,out_min,out_max):
        x = int(x)
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def angulos(self,servo,data,min,max):
        grados=degrees(data.data)
        angulo=int(self.my_map(grados,-90,90,min,max))
        if angulo<240:
            angulo=240
        elif angulo>0:
            angulo=0
        print(f"Servo {servo} : {0}º")

    def swerve_mover(self,data):
        if(data.linear.x>0.5 and data.linear.y<0.6):
            # Print the received data
            print(f"Servo 1 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 3 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 5 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 7 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 2 {0}º")
            print(f"Servo 4 {0}º")
            print(f"Servo 6 {0}º")
            print(f"Servo 8 {0}º")
        if(data.linear.x<0.5 and data.linear.x>0):
            self.angulos(2,data.angular.z,30,210)
            self.angulos(4,data.angular.z,55,235)
            self.angulos(6,data.angular.z,72,252)
            self.angulos(8,data.angular.z,-40,180)
            print(f"Servo 1 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 3 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 5 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 7 {int((data.linear.x+data.angular.z)*1000)}")
        if(data.linear.x>0.5 and data.linear.y>.6):
            # Print the received data
            print(f"Servo 1 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 3 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 5 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 7 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 2 {90}º")
            print(f"Servo 4 {90}º")
            print(f"Servo 6 {90}º")
            print(f"Servo 8 {90}º")
        if(data.linear.x == 0 and data.angular.z==0):
            print(f"Servo 1 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 3 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 5 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 7 {int((data.linear.x+data.angular.z)*1000)}")
            print(f"Servo 2 {0}º")
            print(f"Servo 4 {0}º")
            print(f"Servo 6 {0}º")
            print(f"Servo 8 {0}º")
       
def main(args=None):
    rclpy.init(args=args)
    listener=DTeleopListener()
    rclpy.spin(listener)
    listener.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    print("Escuchando")
    main()
