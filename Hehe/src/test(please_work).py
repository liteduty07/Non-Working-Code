import wpilib
from wpilib.buttons import JoystickButton
from robotpy_ext.autonomous import AutonomousModeSelector
from networktables import NetworkTables


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Set up NetworkTables
        NetworkTables.initialize(server='localhost')
        self.sd = NetworkTables.getTable('SmartDashboard')

        # Set up joystick
        self.stick = wpilib.Joystick(0)

        # Set up drivetrain motors
        self.left_motor = wpilib.Spark(0)
        self.right_motor = wpilib.Spark(1)

        # Set up autonomous mode selector
        self.auto_mode_selector = AutonomousModeSelector()

    def autonomousInit(self):
        self.auto_mode_selector.start()

    def autonomousPeriodic(self):
        self.auto_mode_selector.display_current_mode()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        # Use joystick to control the robot
        self.left_motor.set(-self.stick.getRawAxis(1))
        self.right_motor.set(-self.stick.getRawAxis(5))

        # Send data to the SmartDashboard
        self.sd.putNumber('left_speed', self.left_motor.get())
        self.sd.putNumber('right_speed', self.right_motor.get())

if __name__ == '__main__':
    wpilib.run(MyRobot)