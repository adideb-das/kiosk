import time, board, busio
import adafruit_vl53l0x

i2c = busio.I2C(board.SCL, board.SDA)
tof = adafruit_vl53l0x.VL53L0X(i2c)     # i2c address of lidar is  0x29


while True:
    # Distance is in centimeters
    dist_mm = tof.range
    dist_cm = dist_mm/10
    print(f"{dist_cm} cm")
    time.sleep(0.1)
