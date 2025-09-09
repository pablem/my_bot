import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    package_name='my_bot'

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'false'}.items()
    )

    # ekf_config = os.path.join(get_package_share_directory(package_name),'config','ekf.yaml')
    # # Run the ekf_node from the robot_localization package
    # ekf_node = Node(
    #     package='robot_localization',
    #     executable='ekf_node',
    #     name='ekf_filter_node',
    #     output='screen',
    #     parameters=[ekf_config]
    # )

    return LaunchDescription([
        rsp,
        # ekf_node,
    ])