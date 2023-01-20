# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time

import adafruit_bmp280
import board
import busio

scl_pin = board.GP3
sda_pin = board.GP2

i2c_bus = busio.I2C( scl_pin, sda_pin )
bmp280_sensor = adafruit_bmp280.Adafruit_BMP280_I2C( i2c_bus, address = 0x76 )
# Get SLP or Altimeter pressure from https://e6bx.com/weather/KPVU/ or https://e6bx.com/weather/KU42/
bmp280_sensor.sea_level_pressure = 1023.2

print()
print( f"BMP280 demo for the Pico W using CircuitPython" )
print()


def c_to_f( value ):
  return value * 1.8 + 32


def m_to_f( meters ):
  return meters * 3.28084


def hpa_to_inhg( hpa ):
  return hpa * 0.029529983071445


loop_count = 0

while True:
  loop_count += 1
  print( f"Temperature: {bmp280_sensor.temperature:.2f} degrees C, {c_to_f( bmp280_sensor.temperature ):.2f} degrees F" )
  print( f"Pressure: {bmp280_sensor.pressure:.1f} hPa, {hpa_to_inhg( bmp280_sensor.pressure ):.2f} inHg" )
  print( f"Altitude = {bmp280_sensor.altitude:.2f} meters, {m_to_f( bmp280_sensor.altitude ):.2f} feet" )
  print( f"Loop count: {loop_count}" )
  print( "" )
  time.sleep( 15 )
