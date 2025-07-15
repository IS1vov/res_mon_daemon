#!/bin/bash
set -e
mkdir -p build/usr/bin
mkdir -p build/etc/systemd/system
mkdir -p build/DEBIAN

cp resource-monitor build/usr/bin/
cp etc/systemd/system/resource_monitor.service build/etc/systemd/system/
cp debian/control build/DEBIAN/
chmod 755 build/DEBIAN
dpkg-deb --build build resource-monitor.deb
