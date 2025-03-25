import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts  

class SquareService(Node):
    def __init__(self):
        super().__init__('square_service')
        self.srv = self.create_service(AddTwoInts, 'calculate_square', self.calculate_square_callback)
        self.get_logger().info('Servicio de cuadrado listo')

    def calculate_square_callback(self, request, response):
        response.sum = request.a * request.a 
        self.get_logger().info(f'Recibido: {request.a}, Respuesta: {response.sum}')
        return response

def main():
    rclpy.init()
    node = SquareService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
