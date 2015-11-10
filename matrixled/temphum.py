import pigpio
import DHT22


def pi():
    pigpio.pi()


def sensor(pi, gpionum):
    DHT22.sensor(pi, gpionum)