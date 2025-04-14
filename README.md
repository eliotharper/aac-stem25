# AAC NSW Easter STEM Camp 2025

## Pinout
connect GND pin of GPS to any GND pin on Pico
connect VCC pin of GPS to  pin (1) of Pico
connect RX pin of GPS to TX pin (0) of Pico
connect TX pin of GPS to RX pin (1) of Pico

## Configure GPS

1. [Install Thonny](https://thonny.org)
2. Plug in your Pico in BOOTSEL mode
3. Flash Pico with [RPI_PICO_W-20241129-v1.24.1.uf2](RPI_PICO_W-20241129-v1.24.1.uf2)
3. Select COM port
4. Paste in the code below which will read and display the raw UART data coming from the GPS module

```
from machine import Pin, UART
import time

# Set up UART connection to GPS module
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Main loop
while True:
    # Check if data is available from GPS
    if uart.any():
        # Read the available data
        gps_reading = uart.read().decode('utf-8')
        
        print(gps_reading)
```

## Install Library

Install [gps_parser.py](https://github.com/inmcm/micropyGPS/tree/master) file.

1. Download [gps_parser.py](gps_parser.py) file.
2. Install library on Pico using Thonny
3. Run the following code

```
from machine import Pin, UART
import time
import gps_parser  # Import our GPS parser library

# Set up UART connection to GPS module
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Create a GPS reader object
gps = gps_parser.GPSReader(uart)

# Main loop
while True:
    # Get the GPS data, this will also try and read any new information form the GPS
    gps_data = gps.get_data()

    if gps_data.has_fix:
        # Print the GPS data
        print(gps_data.latitude, gps_data.longitude)
    
    # Small delay
    time.sleep(0.5)

```


## Integrate with Google Earth

1. [Install pip](https://bootstrap.pypa.io/pip/pip.pyz)

```
from machine import Pin, UART
import time
import gps_parser

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

gps = gps_parser.GPSReader(uart)

def send_kml_over_serial():
    try:
        with open('placemark.kml', 'r') as f:
            print("===BEGIN_KML===")
            for line in f:
                print(line.strip())  # Send each line over serial
            print("===END_KML===")
    except Exception as e:
        print("Failed to read file:", e)

while True:
    gps_data = gps.get_data()

    if gps_data.has_fix:
        print(gps_data.latitude, gps_data.longitude)

        with open('placemark.kml', 'w') as pos:
            kml = f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Placemark>
    <name>Cyber Course</name>
    <description>Attached to the ground. Intelligently places itself at the height of the underlying terrain.</description>
    <Point>
      <coordinates>{gps_data.longitude},{gps_data.latitude}</coordinates>
    </Point>
  </Placemark>
</kml>'''
            pos.write(kml)

        send_kml_over_serial()  # Transmit file over serial after writing

    time.sleep(5)  # Reduce frequency to avoid spamming output

```

