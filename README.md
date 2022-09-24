## ComputerVision_SnookerBallsDetection

Final project on the course "Computer Vision Multiple View Geometry", HIT Holon

This project presents a syntetic over view on a Snooker game table generated from a video of a game.

The view follows each ball during the game, displaying it moving on the table.

### Project Summary
We used a homography matrix to map each dot on the actual table from the video to our syntetic table.

We found the initial location of each ball on the table, and used the homography matrix to find the corresponding location of the balls on our syntetic table.

We updated the balls location on each frame to capture the movement of the balls in the game.

### Basic Requirements
Before running this notebook, please make sure to download the following packages to your environment:
```
- opencv-python
- matplotlib
- jupyterlab
```
