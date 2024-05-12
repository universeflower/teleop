from setuptools import setup

package_name = 'turtlebot3_teleop'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yangjunseok',
    maintainer_email='yangjunseok@todo.todo',
    description='Teleoperation for TurtleBot3 using keyboard',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtlebot3_teleop_key = turtlebot3_teleop.turtlebot3_teleop_key:main',
        ],
    },
)

