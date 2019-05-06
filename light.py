#!/usr/bin/env python

### reset BH1745 LEDs
from bh1745 import BH1745

bh = BH1745()

bh.setup()
bh.set_leds(1)
bh.set_leds(0)

print('turning off LED')