# cisco_wlanauth_proxy

This is a small utility that spins a web server which when accessed authenticates the machine to the web auth wireless guest network. It has the POST request needed to do authentication on the Cisco Wireless LAN Controller.
I find it to be most useful when a device doesn't properly authenticate to the guest WLAN, more precisely old laptops (mostly old MacBooks). Works wonders if an external guest has issues and a cabled connection isn't available.
Potentially it could be used to allow authentication via a QR code, assuming you set it up on a small server and create a QR code out of the web server URL.
