import time, board, busio
import adafruit_vl53l0x

i2c = busio.I2C(board.SCL, board.SDA)
tof = adafruit_vl53l0x.VL53L0X(i2c)     


while True:
    dist = tof.range
    print(f"{dist} mm")
    time.sleep(0.1)
