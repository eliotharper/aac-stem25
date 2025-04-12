# AAC NSW Easter STEM Camp 2025

## GPS Exercise

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