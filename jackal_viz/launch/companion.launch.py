from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    namespace = LaunchConfiguration('namespace')
    namespace_arg = DeclareLaunchArgument(
        name='namespace',
        default_value='misskal',
    )

    pkg_jackal_viz = FindPackageShare('jackal_viz')

    rviz_config = PathJoinSubstitution(
        [pkg_jackal_viz, 'rviz', 'misskal_navigation.rviz']
    )

    rviz_node = Node(
        namespace=namespace,
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', rviz_config],
        remappings=[('/tf', 'tf'), 
                    ('/tf_static', 'tf_static')],
    )

    swri_node = Node(
        namespace=namespace,
        package='swri_console',
        executable='swri_console',
        output='screen',
    )

    robot_monitor_node = Node(
        namespace=namespace,
        package='rqt_robot_monitor',
        executable='rqt_robot_monitor',
        output='screen',
    )

    runtime_monitor_node = Node(
        namespace=namespace,
        package='rqt_runtime_monitor',
        executable='rqt_runtime_monitor',
        output='screen',
    )

    ld = LaunchDescription()
    ld.add_action(namespace_arg)
    ld.add_action(rviz_node)
    ld.add_action(swri_node)
    ld.add_action(robot_monitor_node)
    ld.add_action(runtime_monitor_node)
    return ld
