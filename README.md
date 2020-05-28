# rpmfind.py

simple rpm finder written in python that queries rpmfind.net and scraps the output

## usage
usage: `rpmfind.py [-h] [-d] [-n N] [--dist DIST] [--arch ARCH] software`

positional arguments:  
- software / software name


optional arguments:  
- -h, --help / show this help message and exit  
- -d, --debug / turn on debug logging  
- -n N / head -n \<N>  
- --dist DIST / software distribution  
- --arch ARCH / software architecture   

## example
```bash
(.virtualenv) [john@doe rpmfind]$ ./rpmfind.py -n 2 --dist fedora --arch s390x gcc | column -s ',' -t
gcc-10.1.1-1.fc33.s390x     https://www.rpmfind.net/<...>/gcc-10.1.1-1.fc33.s390x.rpm     Fedora Rawhide for s390x
gcc-10.0.1-0.11.fc32.s390x  https://www.rpmfind.net/<...>/gcc-10.0.1-0.11.fc32.s390x.rpm  Fedora 32 for s390x
```
