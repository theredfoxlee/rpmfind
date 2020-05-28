# rpmfind.py

simple rpm finder written in python that queries rpmfind.net and scraps the output

## usage
`rpmfind.py [-h] [-d] [-n N] [--dist DIST] [--arch ARCH] software`

## example
```bash
(.virtualenv) [john@doe rpmfind]$ ./rpmfind.py -n 2 --dist fedora --arch s390x gcc | column -s ',' -t
gcc-10.1.1-1.fc33.s390x     https://www.rpmfind.net/<...>/gcc-10.1.1-1.fc33.s390x.rpm     Fedora Rawhide for s390x
gcc-10.0.1-0.11.fc32.s390x  https://www.rpmfind.net/<...>/gcc-10.0.1-0.11.fc32.s390x.rpm  Fedora 32 for s390x
```
