class FakePigpio:
    pass

class FakeDHT22:
    pass

import sys
sys.modules['pigpio'] = FakePigpio
sys.modules['DHT22'] = FakeDHT22