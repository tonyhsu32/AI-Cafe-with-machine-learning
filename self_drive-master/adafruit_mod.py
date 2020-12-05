from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import Robot


# Create an instance of the robot with the specified trim values.
# Not shown are other optional parameters:
#  - addr: The I2C address of the motor HAT, default is 0x60.
#  - left_id: The ID of the left motor, default is 1.
#  - right_id: The ID of the right motor, default is 2.
LEFT_TRIM   = 0
RIGHT_TRIM  = 0
robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)


GPIO.setmode(GPIO.BCM)
PWM_PINr = 18
PWM_PINl = 12
GPIO.setup(PWM_PINr, GPIO.OUT)
GPIO.setup(PWM_PINl, GPIO.OUT)

pwmrb = GPIO.PWM(PWM_PINr, 500)
pwmlb = GPIO.PWM(PWM_PINl, 500)

pwmrb.start(0)
pwmlb.start(0)


PWM_PINrb = 17
PWM_PINlb = 6
GPIO.setup(PWM_PINrb, GPIO.OUT)
GPIO.setup(PWM_PINlb, GPIO.OUT)

pwmr = GPIO.PWM(PWM_PINrb, 500)
pwml = GPIO.PWM(PWM_PINlb, 500)

pwmr.start(0)
pwml.start(0)

#GPIO_TRIGGER = 23
#GPIO_ECHO = 24

#GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
#GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

#GPIO.output(GPIO_TRIGGER, False)
camera = PiCamera()
camera.start_preview()
def init():
        robot.stop()
#60
def go_60():
        init()
        robot.forward(90)
#30
def go_30():
        init()
        robot.forward(80)

def left():
        init()
        robot.left(70)

def right():
        init()
        robot.right(70)
def left1():
        init()
        robot.left(100)

def right1():
        init()
        robot.right(100)

def stop():
        init()
        robot.stop()
#traffic sign use (Peter

def SP_60():
        init()
        pwmr.ChangeDutyCycle(95)
        pwml.ChangeDutyCycle(95)

def SP_30():
        init()
        pwmr.ChangeDutyCycle(40)
        pwml.ChangeDutyCycle(40)

def SP_60R():
        init()
        pwmrb.ChangeDutyCycle(30)
        pwml.ChangeDutyCycle(100)
def SP_30R():
        init()
        pwmrb.ChangeDutyCycle(30)
        pwml.ChangeDutyCycle(50)
def SP_60L():
        init()
        pwmr.ChangeDutyCycle(100)
        pwmlb.ChangeDutyCycle(30)
def SP_30L():
        init()
        pwmr.ChangeDutyCycle(50)
        pwmlb.ChangeDutyCycle(30)
#traffic sign use (Peter
def foo():
        print('good')

#def sendSonic():
# Allow module to settle
#        time.sleep(0.5)

# Send 10us pulse to trigger
#        GPIO.output(GPIO_TRIGGER, True)
#        time.sleep(0.00001)
#       GPIO.output(GPIO_TRIGGER, False)
#        start = time.time()
#        while GPIO.input(GPIO_ECHO)==0:
#                start = time.time()

#        while GPIO.input(GPIO_ECHO)==1:
#                stop = time.time()

# Calculate pulse length
#        elapsed = stop-start

# Distance pulse travelled in that time is time
# multiplied by the speed of sound (cm/s)
#        distance = elapsed * 34000

# That was the distance there and back so halve the value
#        distance = distance / 2

#        return distance

if __name__=='__main__':
    try:
        while True:
            key = raw_input('in:')   
            print(key)
            if key == 'w':
                init()
                go_60()
            print(key)

            if key == 's':
                init()
                robot.backward(90)
            print(key)

            if key == 'a':
                init()
                left()
                print(key)

            if key == 'd':
                init()
                right()
                print(key)

            if key == 'p':
                init()
                stop()
                print(key)

            if key == 'l':
                camera.rotation = 180
                camera.start_preview(alpha=200)
                camera.start_preview()
                time.sleep(3)
                camera.stop_preview()

            if key =='k':
                camera.stop_preview()


    except KeyboardInterrupt:
        print ("Exception: KeyboardInterrupt")

    finally:
        pwmr.stop()
        pwml.stop()
        pwmrb.stop()
        pwmlb.stop()


        GPIO.cleanup()

