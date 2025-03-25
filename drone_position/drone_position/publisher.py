import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import random

class DronePublisher(Node):
    def __init__(self):
        super().__init__('drone_publisher')
        self.publisher_ = self.create_publisher(NavSatFix, 'drone_position', 10)
        self.timer = self.create_timer(1.0, self.publish_position)

    def publish_position(self):
        msg = NavSatFix()
        msg.latitude = random.uniform(-90.0, 90.0)   
        msg.longitude = random.uniform(-180.0, 180.0)
        msg.altitude = random.uniform(0.0, 1000.0)
    
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: lat={msg.latitude}, lon={msg.longitude}, alt={msg.altitude}')

def main(args=None):
    rclpy.init(args=args)
    node = DronePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
