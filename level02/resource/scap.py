from scapy.all import rdpcap, TCP, Raw

p = rdpcap("level02.pcap")
st = []
for i, packet in enumerate(p):
    if i > 43 and packet[TCP].haslayer(Raw):
        b = str(packet[TCP][Raw].load, 'utf-8')
        if b.isalnum():
            st.append(b)
        elif ord(b[0]) == 0x7f:
            st = st[:-1]
        #print(str(packet[TCP][Raw].load))
print(''.join(st))
#ft_waNDReL0L
