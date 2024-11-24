from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used?
@serial_command(BoardAddress.Picker, "O3")
class FraudSensorDisableTransistorCommand(SerialCommand):
    def run(self):
        self.logger.debug("FraudSensorDisableTransistor")
        self.ser.write(b"OK\r\n")
