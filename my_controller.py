"""drive_my_drive controller."""
# You may need to import some classes of the controller module. Ex:
from controller import Robot, Motor, DistanceSensor, Keyboard, Camera
#from controller import Robot
# create the Robot instance.
robot = Robot()
print("hello")
k = robot.getKeyboard()
cam = robot.getCamera('camera')

# get the time step of the current world.
timestep = 64

k.enable(timestep)
cam.enable(timestep)
max_speed=6.28
#create motor instances
left_motor1 =robot.getMotor("motor_1")
left_motor2 =robot.getMotor("motor_4")
right_motor1=robot.getMotor("motor_2")
right_motor2=robot.getMotor("motor_3")
left_motor1.setPosition(float('inf'))
left_motor1.setVelocity(0.0)
left_motor2.setPosition(float('inf'))
left_motor2.setVelocity(0.0)
right_motor1.setPosition(float('inf'))
right_motor1.setVelocity(0.0)
right_motor2.setPosition(float('inf'))
right_motor2.setVelocity(0.0)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    key = k.getKey()
    if key == 315:
        left_speed = 1.0 * max_speed
        right_speed= 1.0 * max_speed
        left_motor1.setVelocity(left_speed)
        left_motor2.setVelocity(left_speed)
        right_motor1.setVelocity(right_speed)
        right_motor2.setVelocity(right_speed)
    if key == 32:
        left_speed = 0 * max_speed
        right_speed= 0 * max_speed
        left_motor1.setVelocity(left_speed)
        left_motor2.setVelocity(left_speed)
        right_motor1.setVelocity(right_speed)
        right_motor2.setVelocity(right_speed)
    if key == 317:
        left_speed = -1 * max_speed
        right_speed= -1 * max_speed
        left_motor1.setVelocity(left_speed)
        left_motor2.setVelocity(left_speed)
        right_motor1.setVelocity(right_speed)
        right_motor2.setVelocity(right_speed)
    if key == 314:
        left_speed = -1 * max_speed
        right_speed= 1 * max_speed
        left_motor1.setVelocity(left_speed)
        left_motor2.setVelocity(left_speed)
        right_motor1.setVelocity(right_speed)
        right_motor2.setVelocity(right_speed)
    if key == 316:
        left_speed = 1 * max_speed
        right_speed= -1 * max_speed
        left_motor1.setVelocity(left_speed)
        left_motor2.setVelocity(left_speed)
        right_motor1.setVelocity(right_speed)
        right_motor2.setVelocity(right_speed)
    
    
    # Enter here exit cleanup code.


