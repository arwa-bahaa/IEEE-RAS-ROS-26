import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable

from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    task_pkg = get_package_share_directory('task_14')

    turtlebot_pkg = get_package_share_directory(
        'turtlebot3_description'
    )

    set_gazebo_path = SetEnvironmentVariable(
    name='GZ_SIM_RESOURCE_PATH',
    value='/opt/ros/jazzy/share:' + turtlebot_pkg

    )

    world = os.path.join(
        task_pkg,
        'worlds',
        'my_world.world'
    )    urdf_file = os.path.join(
        turtlebot_pkg,
        'urdf',
        'turtlebot3_burger.urdf'
    )


    with open(urdf_file, 'r') as file:
        robot_description = file.read()


    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={
            'gz_args': world
        }.items()
    )


    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[
            {
                'robot_description': robot_description
            }
        ],
        output='screen'
    )


    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name',
            'turtlebot3_burger',
            '-topic',
            'robot_description',
            '-x',
            '0',
            '-y',
            '0',
            '-z',
            '0.2'
        ],
        output='screen'
    )


    autonomous_mover = Node(
        package='task_14',
        executable='autonomous_mover',
        name='autonomous_mover',
        output='screen'
    )


    return LaunchDescription([
        set_gazebo_path,
        gazebo,
        robot_state_publisher,
        spawn_robot,
        autonomous_mover
    ])


