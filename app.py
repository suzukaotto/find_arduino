import serial
import serial.tools.list_ports

def find_arduino_port():
    ports = serial.tools.list_ports.comports()
    
    arduino_port = None
    
    for port in ports:
        port_name = port.device
        description = port.description.lower()
        
        if "arduino" in description:
            arduino_port = port_name
            break
    
    return arduino_port

port = find_arduino_port()

if port:
    print(f"Arduino is connected on port: {port}")
else:
    print("No Arduino found.")
