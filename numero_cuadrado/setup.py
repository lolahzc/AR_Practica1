from setuptools import setup
import os
from glob import glob

package_name = 'numero_cuadrado'  

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),  
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lolahercan',
    maintainer_email='lolahercan@email.com',
    description='Paquete que implementa un servicio y cliente en ROS2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service_node = numero_cuadrado.service_node:main',  
            'client_node = numero_cuadrado.client_node:main',    
        ],
    },
)