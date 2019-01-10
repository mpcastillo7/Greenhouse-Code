from gpiozero import AngularServo
from time import

s = AngularServo(17, min_angle=-80, max_angle=80)
s.angle = 15
sleep(1)
s.angle = 0
