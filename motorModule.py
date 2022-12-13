import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
print(0)

# SetUp the GPIO out put from the Rasspi 
GPIO.setup(29, GPIO.OUT)  # Yellow wire
GPIO.setup(31, GPIO.OUT)  # White Wire
GPIO.setup(32, GPIO.OUT)  # ORANGE WIRE
GPIO.setup(33, GPIO.OUT)  # BROWN wire

#creating a class to control the motors 
class Motor():
    def __init__(self, name, lwheel, rwheel):
        self.name = name
        # Tuple for GIPO controling the wheels
        # (29,31) , (32 ,33)
        self.lwheel = tuple(lwheel)
        self.rwheel = tuple(rwheel)
        # Specifiy for left wheel forward Backward
        self.lwheelF = int(lwheel[0])
        self.lwheelB = int(lwheel[1])
        # Specifiy for right wheel forward Backward
        self.rwheelF = int(rwheel[0])
        self.rwheelB = int(rwheel[1])

    def forward(self):
        GPIO.output(self.rwheelF, True)
        GPIO.output(self.lwheelF, True)

    def backward(self):
        GPIO.output(self.rwheelB, True)
        GPIO.output(self.lwheelB, True)

    def turnleft(self):
        GPIO.output(self.rwheelF ,True)

    def turnRight(self):
        GPIO.output(self.lwheelF ,True)

    def breaking(self):
        GPIO.output(self.rwheelF, False)
        GPIO.output(self.lwheelF, False)
        GPIO.output(self.rwheelB, False)
        GPIO.output(self.lwheelB, False)


def main():
    myMotor = Motor ("kalia" , (29,31) , (32,33))
    myMotor.forward()
    time.sleep(3)
    myMotor.breaking()
    time.sleep(3)
    myMotor.backward()
    time.sleep(3)
    myMotor.breaking()
    time.sleep(3)
    myMotor.turnRight()
    time.sleep(3)
    myMotor.breaking()
    time.sleep(3)
    myMotor.turnleft()
    time.sleep(3)
    myMotor.breaking()

if __name__ == "__main__":
    main()
