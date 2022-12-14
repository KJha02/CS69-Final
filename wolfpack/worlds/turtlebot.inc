define kinect ranger
(
  sensor
  (
    range_max 6.5
    fov 58.0
    samples 640
  )
  # generic model properties
  color "black"
  size [ 0.06 0.15 0.03 ]
)

define turtlebot position
(
  pose [ 0.0 0.0 0.0 0.0 ]

  odom_error [0.0 0.0 0 0 0 0.0]

  localization "odom"
  size [ 0.125 0.125 0.40 ]
  origin [ 0.0 0.0 0.0 0.0 ]
  gui_nose 1
  drive "diff"
  color "gray"

  kinect(pose [ 0.0 0.0 0.0 0.0 ])
)
