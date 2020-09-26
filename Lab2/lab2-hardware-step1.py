from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def letter_A():
    B = blue
    O = nothing
    logo = [
    O, O, O, O, B, O, O, O,
    O, O, O, B, O, B, O, O,
    O, O, B, O, O, O, B, O,
    O, O, B, B, B, B, B, O,
    O, O, B, O, O, O, B, O,
    O, O, B, O, O, O, B, O,
    O, O, B, O, O, O, B, O,
    O, O, B, O, O, O, B, O,
    ]
    return logo

def letter_B():
    B = blue
    O = nothing
    logo = [
    O, O, B, B, B, B, O, O, 
    O, O, B, O, O, B, O, O,
    O, O, B, O, O, B, O, O, 
    O, O, B, B, B, B, B, O,
    O, O, B, O, O, O, B, O,
    O, O, B, O, O, O, B, O,
    O, O, B, O, O, O, B, O,
    O, O, B, B, B, B, B, O,
    ]
    return logo


images = [letter_A, letter_B]
count = 0

while True: 
    events = s.stick.get_events()
    if events:
      for event in events:
        if event.action != 'pressed':
          continue
        if event.direction == 'left':
          s.set_pixels(images[count % len(images)]())
          count += 1
        if event.direction == 'right':
          s.set_pixels(images[count % len(images)]())
          count += 1
        if event.direction == 'up':
          s.set_pixels(images[count % len(images)]())
          count += 1
        if event.direction == 'down':
          s.set_pixels(images[count % len(images)]())
          count += 1  