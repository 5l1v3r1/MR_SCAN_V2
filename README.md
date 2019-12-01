![MR_LOGO](https://i.imgur.com/TMCZw0G.png)

# MR_SCAN v1.0
MR_SCAN_V2 is a python3 script that scan your network using pings.
The V1 is avariable [here](https://github.com/b3rt1ng/MR_SCAN)
Note that this project has been only made for Linux.

## Next updates:

* Device conection power (how much does it take connection in the network)
* Choose an adress by it's position on the scanned adress list
* Linkable to MR_SPOOF

### what do you need to run this program ?

you will need:
```
Python 3
the uuid module
the netifaces module
```

i'll ad a PIP compatible file to install thoose directly.

### Installation

```
git clone https://github.com/b3rt1ng/MR_SCAN_V2
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Do not use this script for any illegal purposes.

### Limitations
the script is using a ping subprocees to check if a host is  up or not. because of the basics parameters of the ping command, the time between each ping cannot go below 1 second. if you want to do a faster ping scan, i higly recommand you to follow [this guide](https://null-byte.wonderhowto.com/how-to/turbo-ping-sweeping-with-python-0163098/). You can also use Nmap to scan a network precisely and pretty fastly. do your research...

