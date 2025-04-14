port = '/dev/tty.usbmodem1101'  # Adjust this to your Pico's device
baud = 115200                   # REPL default baud rate

collecting = False

# Open the serial port like a regular file
with open(port, 'rb') as ser, open("placemark.kml", "w") as outfile:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line == "===BEGIN_KML===":
            collecting = True
            continue
        elif line == "===END_KML===":
            break
        if collecting:
            outfile.write(line + "\n")

print("KML file received and saved to placemark.kml")