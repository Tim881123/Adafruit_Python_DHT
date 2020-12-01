#!/usr/bin/env python3
while (1):
  h0, t0 = Adafruit_DHT.read_retry(sensor, pin)
  if h0 is not None and t0 is not None:
      print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(t0, h0))
  else:
      print('Failed to get reading. Try again!')
      sys.exit(1)

