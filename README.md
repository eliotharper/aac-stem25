# AAC NSW Easter STEM Camp 2025

## Configure GPS

1. [Install Thonny](https://thonny.org)
2. Plug in your Pico
3. Select its COM port
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

Install [gps_parser.py](gps_parser.py) file.

This library not only hides a lot of the complexities of extracting the relevant information from the GPS string but also deals with the UART interactions for us as well. The code below is a demo of how to use the library:

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
    
    # Print the GPS data
    print(gps_data.has_fix, gps_data.latitude, gps_data.longitude)
    
    # Small delay
    time.sleep(0.5)

```