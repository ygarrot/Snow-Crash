from scapy.all import *

p = rdpcap("level02.pcap")
i = 0
st = ""
for packet in p:
    i+=1
    if i > 44 and packet[TCP].haslayer(Raw):
        # st += str(packet[TCP][Raw].load)
        print(str(packet[TCP][Raw].load))
print (st)
#ft_waNDReL0L
