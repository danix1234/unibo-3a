import tkinter as tk

class PCClient:
    def __init__(self, pc_name, mac_address):
        self.pc_name = pc_name
        self.mac_address = mac_address
        self.ip_address = None
        self.arp_table = {}
        self.dhcp_offer = None
        self.step = 0
        self.create_window()

    def create_window(self):
        self.window = tk.Tk()
        self.window.title(f"{self.pc_name} - PC Network Simulation")

        # Labels to show information
        self.label_status = tk.Label(self.window, text="PC is starting...", justify=tk.LEFT)
        self.label_status.pack()

        self.label_arp = tk.Label(self.window, text="ARP Table: Empty", justify=tk.LEFT)
        self.label_arp.pack()

        # Button to move step by step
        self.button_next = tk.Button(self.window, text="Next Step (Click Here)", command=self.next_step)
        self.button_next.pack()

        self.window.mainloop()

    def next_step(self):
        # Step 1: Configurazione MAC e richiesta IP
        if self.step == 0:
            self.label_status.config(text=f"Step 1: Configurazione MAC: {self.mac_address}.\nRichiesta IP tramite DHCP Discovery in broadcast.")
            self.step += 1
            self.send_dhcp_discovery()
        
        # Step 2: DHCP Offer
        elif self.step == 1 and self.dhcp_offer:
            self.label_status.config(text=f"Step 2: DHCP Offer ricevuta:\nIP: {self.dhcp_offer['IP']}\nNetmask: {self.dhcp_offer['Netmask']}\nGateway: {self.dhcp_offer['Gateway']}\nDNS: {self.dhcp_offer['DNS']}")
            self.step += 1
        
        # Step 3: DHCP Request & Acknowledge
        elif self.step == 2:
            self.label_status.config(text="Step 3: Invio DHCP Request...\nAttesa conferma.")
            self.step += 1
        elif self.step == 3 and self.dhcp_offer:
            self.ip_address = self.dhcp_offer['IP']
            self.label_status.config(text=f"Step 4: DHCP Acknowledge ricevuto.\nConfigurazione IP: {self.ip_address}")
            self.step += 1
        
        # Step 4: ARP Request
        elif self.step == 4:
            self.label_status.config(text=f"Step 5: Invio ARP Request in broadcast per risolvere l'IP del Gateway.")
            self.step += 1

        # Step 5: Simulazione ARP Reply dal gateway
        elif self.step == 5:
            # Simulazione ARP Reply dal gateway
            gateway_ip = "192.168.1.1"
            gateway_mac = "00:0c:29:ab:cd:ef"
            self.arp_table[gateway_ip] = gateway_mac
            self.label_status.config(text=f"Step 6: ARP Reply ricevuto.\nMAC del Gateway: {gateway_mac}")
            self.label_arp.config(text=f"ARP Table: {gateway_ip} -> {gateway_mac}")
            self.step += 1
            
        # Step 6: Comunicazione all'interno della rete
        elif self.step == 6:
            self.label_status.config(text="Step 7: Comunicazione avviata con il Gateway.")
            self.step += 1

    def send_dhcp_discovery(self):
        # Invia la richiesta DHCP Discovery al Gateway (qui simulata)
        self.dhcp_offer = {
            "IP": "192.168.1.10",
            "Netmask": "255.255.255.0",
            "Gateway": "192.168.1.1",
            "DNS": "8.8.8.8"
        }
        print("Invio DHCP Discovery in broadcast...")

# Esecuzione del client PC
pc1_simulation = PCClient("PC1", "00:0a:95:9d:68:16")
