import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class SquareClient(Node):
    def __init__(self):
        super().__init__('square_client')
        self.cli = self.create_client(AddTwoInts, 'calculate_square')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando servicio...')
        self.req = AddTwoInts.Request()

    def send_request(self, number):
        self.req.a = number
        future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, future)
        return future.result().sum 

def main():
    rclpy.init()
    node = SquareClient()
    number = 5  
    result = node.send_request(number)
    node.get_logger().info(f'El cuadrado de {number} es {result}')
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()