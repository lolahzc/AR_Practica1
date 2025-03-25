# Práctica 1 

Para comprobar el paquete de drone position: 
1. Se clona el repositorio en el src de nuestro workspace
2. Hacemos colcon build
3. A continuación se hace source install/setup.bash
4. ros2 run drone_position publisher
5. ros2 run drone_position suscriber

Para comprobar el paquete de numero cuadrado:
1. ros2 run numero_cuadrado service_node
2. ros2 run numero_cuadrado client_node
