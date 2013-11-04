TEMPLATE = app
TARGET = atrace
CONFIG -= qt
SOURCES += atrace.c
CONFIG += link_pkgconfig
PKGCONFIG += zlib

bin.path = /usr/bin/
bin.files += atrace
INSTALLS += bin
