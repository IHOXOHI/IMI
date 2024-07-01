from time import ticks_us
import uasyncio

t1 = ticks_us()###Time reference start there. (or Now?)

class TIMING:
    """New very simple'Timer Rescape' to manipulate unit's time with easy when classicals functions (time.localtime and/or RTC.datetime) doesn't works correctly"""

    def timing_us(self):
        t2 = ticks_us()
        us = t2 - t1
        return us

    def timing_ms(self):
        t2 = self.timing_us()
        ms = t2 // 1000
        return ms

    def timing_s(self):
        t2 = self.timing_ms()
        s = t2  // 1000
        return s

    def timing_m(self):
        t2 = self.timing_s()
        m = t2 // 60
        return m

    def timing_h(self):
        t2 = self.timing_m()
        h = t2 // 60
        return h

    def timing_d(self):
        t2 = self.timing_h()
        d = t2 // 24
        return d

    def timing_reset(self):
        global t1
        t1 = ticks_us()
