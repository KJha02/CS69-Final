# Hunting patrolling party

After setting up the contents of this zipped file as a catkin package, we can run this program by doing the following:

Open your ros directory within 3 terminal windows, running the command ```docker-compose exec ros bash``` in each.

In one terminal window, launch the stage ros world by typing ```roslaunch wolfpack main.launch```.

In the two other windows
  - Type ```roscd wolfpack```, which should change your current working directory to the package's main folder.
  - In one of these windows, run the command ```bash run6.sh``` to initiate the patrolling and running away behavior.
  - To end these processes, run the command ```bash kill6.sh``` in the last window
