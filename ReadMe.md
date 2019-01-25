This script uses keras to determine the hand you raise (left, right or no) based on your webcam stream.
To generate training data, set right or left in the snapshot path in generate_dataset.py. Then run the script while handing your corresponding hand in multiple positions.
Run twice one for each hand.
Run model.py to learn.
Run guessing.py to see the prediction in realtime.
Change /dev/video1 to your default camera (usually /dev/video0).

With 100 training pictures I get 100% accuaracy on the training set, good results in live prediction but doesn't generalize enough (i.e when your hands is too at left or too at right).

To get better results:
  - More training data
  - More various training data: try at different distances from your webcam, with different angles, with different light settings
  - Bigger neural network

Fun ideas to try:
  - Control mouse with webcam
  - Control racing game
  - Spotify next/previous/pause
  - Control scroll
  - Switch tabs
  - Try to distinguish more precise hands positions
