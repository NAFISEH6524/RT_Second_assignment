# RT_Second_assignment

# Introduction
The employment of a robot simulator in ROS is the subject of the second assignment for the research track 1 course.
Moving the robot in the environment to the user-selected objective point is the task for this assignment.
We are employing operator ROS custom messages, services, and actions in this assignment. Additionally, graphical interfaces (Rviz and Gazebo) were used to view the simulation of the robot. In order to launch the simulation, a launch file must also be created.
Alongside assignment 2 2022, a new package was created. This assignment's goal was to add four new nodes to the robot simulation:

# Installation
 Creat the workspace()
 ```bash
    $ ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_STANDARD=20
```


# Setup the .basrhc script
Open .bashrc with a text editor and add the following line at the end of the file: 

source ~/ros_catkin_ws/install_isolated/setup.bash
```bash
    $ source .bashrc
```
You should have now a full desktop ROS installation in your Ubuntu22 OS!


# Install the package
Go to your workspace's src folder.
```bash
    $ cd ~/ros_catkin_ws/src
```
Clone the repository of prof in the src folder
```bash
    $ git clone https://github.com/CarmineD8/assignment_2_2022.git
```
Then Clone this repository in the src folder
```bash
    $ git clone https://github.com/NAFISEH6524/RT_Second_assignment.git
```
# Node description
In the first step, you have the option to either establish or remove a target point.
Then, you will display how many goals were achieved and how many were abandoned.
 Also, you will display the robot's distance from the target point and its average speed.



# Running Terminals
You have the option to set or remove a target point in this terminal. You can enter 1 if you want to set a target.
![Tux, the Linux mascot](/picture/run.jpeg)

# Nodes Graph
A GUI plugin for displaying the ROS computation graph is offered by the rqt graph command.
The resulting network in this instance is quite straightforward as there are only four nodes (shown as elliptical boxes) and two themes (represented as rectangular boxes). Simply execute the following command to see the graph:
```bash
    $ rqt_graph
```
![Tux, the Linux mascot](/picture/rqt.jpeg)

