import serial
import os
import sys
class Ser(object):
    def __init__(self, port = 'COM9'):
        # 打开端口
        self.port = port
        #self.port = serial.Serial(port='COM9', baudrate=115200, bytesize=8, parity=serial.PARITY_ODD, stopbits=1, timeout=2)
        
    def open_port(self, port = 'COM9', baudrate=115200, bytesize=8, parity=serial.PARITY_ODD, stopbits=1, timeout=2):
        self.port = serial.Serial(port=port, baudrate=115200, bytesize=8, parity=serial.PARITY_ODD, stopbits=1, timeout=2)

    def find_ports(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i+1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/ttyUSB*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.usbserial*')
        else:
            raise EnvironmentError('Error finding ports on your operating system')
        openbci_port = []
        for port in ports:
            try:
                s = serial.Serial(port= port, baudrate = 115200)
                s.write(b'v')
                #openbci_serial = openbci_id(s)
                s.close()
                #if openbci_serial:
                openbci_port.append(port)
            except (OSError, serial.SerialException):
                pass
        if openbci_port == '':
            raise OSError('Cannot find serial port')
        else:
            return openbci_port 

    # 发送指令的完整流程
    def send_cmd(self, cmd):
        self.port.write(cmd)
        response = self.port.readall()
        response = self.convert_hex(response)
        return response

    def read_word(self, slave_addr, reg_addr):
        self.port.write([slave_addr, reg_addr*2])
        data = self.port.read(2)
        res = []
        for item in data:
            res.append(item)
        if res == []:
            res = [0x00,0x00]
        return res[1]*256+res[0]

    def write_word(self, slave_addr, reg_addr, data_H, data_L):
        self.port.write([slave_addr, reg_addr*2+1, data_L, data_H])

    def battery_write_command(self, slave_addr, data_H, data_L):
        self.port.write([slave_addr, data_L, data_H])

    def battery_read_voltage(self, slave_addr):
        self.port.write([slave_addr])
        voltage = self.port.read(2)
        res = []
        for item in voltage:
            res.append(item)
        if res == []:
            res = [0x00, 0x00]
        return res[1] * 256 + res[0]

    # 转成16进制的函数
    def convert_hex(self, string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))
        return result


