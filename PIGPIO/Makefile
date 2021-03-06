#
CC       = gcc
AR       = ar
RANLIB   = ranlib
SIZE     = size
SHLIB    = gcc -shared
STRIPLIB = strip --strip-unneeded

CFLAGS	+= -O3 -Wall

LIB1     = libpigpio.so
OBJ1     = pigpio.o command.o

LIB2     = libpigpiod_if.so
OBJ2     = pigpiod_if.o command.o

LIB      = $(LIB1) $(LIB2)

ALL     = $(LIB) x_pigpio x_pigpiod_if pig2vcd pigpiod pigs

LL1      = -L. -lpigpio -lpthread -lrt

LL2      = -L. -lpigpiod_if -lpthread -lrt

all:	$(ALL)

pigpio.o: pigpio.c pigpio.h command.h custom.cext
	$(CC) $(CFLAGS) -fpic -c -o pigpio.o pigpio.c

pigpiod_if.o: pigpiod_if.c pigpio.h command.h pigpiod_if.h
	$(CC) $(CFLAGS) -fpic -c -o pigpiod_if.o pigpiod_if.c

command.o: command.c pigpio.h command.h
	$(CC) $(CFLAGS) -fpic -c -o command.o command.c

x_pigpio:	x_pigpio.o $(LIB1)
	$(CC) -o x_pigpio x_pigpio.o $(LL1)

x_pigpiod_if:	x_pigpiod_if.o $(LIB2)
	$(CC) -o x_pigpiod_if x_pigpiod_if.o $(LL2)

pigpiod:	pigpiod.o $(LIB1)
	$(CC) -o pigpiod pigpiod.o $(LL1)

pigs:		pigs.o command.o
	$(CC) -o pigs pigs.o command.o

pig2vcd:	pig2vcd.o
	$(CC) -o pig2vcd pig2vcd.o

clean:
	rm -f *.o *.i *.s *~ $(ALL)

install:	$(ALL)
	install -m 0755 -d               /opt/pigpio/cgi
	install -m 0755 -d               /usr/local/include
	install -m 0644 pigpio.h         /usr/local/include
	install -m 0644 pigpiod_if.h     /usr/local/include
	install -m 0755 -d               /usr/local/lib
	install -m 0755 libpigpio.so     /usr/local/lib
	install -m 0755 libpigpiod_if.so /usr/local/lib
	install -m 0755 -d               /usr/local/bin
	install -m 0755 -s pig2vcd       /usr/local/bin
	install -m 0755 -s pigpiod       /usr/local/bin
	install -m 0755 -s pigs          /usr/local/bin
	python2 setup.py install
	python3 setup.py install
	install -m 0755 -d               /usr/local/man/man1
	install -m 0644 *.1              /usr/local/man/man1
	install -m 0755 -d               /usr/local/man/man3
	install -m 0644 *.3              /usr/local/man/man3
	ldconfig

uninstall:
	rm -f /usr/local/include/pigpio.h
	rm -f /usr/local/include/pigpiod_if.h
	rm -f /usr/local/lib/libpigpio.so
	rm -f /usr/local/lib/libpigpiod_if.so
	rm -f /usr/local/bin/pig2vcd
	rm -f /usr/local/bin/pigpiod
	rm -f /usr/local/bin/pigs
	echo removing python2 files
	python2 setup.py install --record /tmp/pigpio >/dev/null
	xargs rm -f < /tmp/pigpio >/dev/null
	echo removing python3 files
	python3 setup.py install --record /tmp/pigpio >/dev/null
	xargs rm -f < /tmp/pigpio >/dev/null
	rm -f /usr/local/man/man1/pig*.1
	rm -f /usr/local/man/man3/pig*.3
	ldconfig

$(LIB1):	$(OBJ1)
	$(SHLIB) -o $(LIB1) $(OBJ1)
	$(STRIPLIB) $(LIB1)
	$(SIZE)     $(LIB1)

$(LIB2):	$(OBJ2)
	$(SHLIB) -o $(LIB2) $(OBJ2)
	$(STRIPLIB) $(LIB2)
	$(SIZE)     $(LIB2)

# generated using gcc -MM *.c

pig2vcd.o: pig2vcd.c pigpio.h
pigpiod.o: pigpiod.c pigpio.h
pigs.o: pigs.c pigpio.h command.h
x_pigpio.o: x_pigpio.c pigpio.h
x_pigpiod_if.o: x_pigpiod_if.c pigpiod_if.h pigpio.h
