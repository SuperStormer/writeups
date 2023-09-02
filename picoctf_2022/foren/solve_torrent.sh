#!/bin/sh
tshark.exe -r torrent.pcap -Y 'bt-dht.bencoded.string==info_hash' -Tfields -e 'bt-dht.bencoded.string' | cut -d, -f 5 | sort | uniq
