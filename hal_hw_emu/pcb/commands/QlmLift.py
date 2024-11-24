from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used
@serial_command(BoardAddress.Aux, "M1")
class QlmLiftCommand(SerialCommand):
    def run(self):
        self.logger.debug("QlmLift")
        self.ser.write(b"M OK\r\n")
