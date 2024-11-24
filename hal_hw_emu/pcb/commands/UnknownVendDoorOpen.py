from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used?
@serial_command(BoardAddress.Aux, "I2")
class UnknownVendDoorOpenCommand(SerialCommand):
    def run(self):
        self.logger.debug("UnknownVendDoorOpen")
        self.ser.write(b"I OK\r\n")