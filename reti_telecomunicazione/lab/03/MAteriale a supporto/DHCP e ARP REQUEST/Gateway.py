import tkinter as tk

class GatewayServer:
    def __init__(self):
        self.dhcp_offer = {
            "IP": "192.168.1.10",
            "Netmask": "255.255.255.0",
            "Gateway": "192.168.1.1",
            "DNS": "8.8.8.8"
        }
        self.arp_requests = []
        self.step = 0
        self.create_window()

    def create_window(self):
        self.window = tk.Tk()
        self.window.title("Gateway / DHCP Server Simulation")

        # Labels to show information
        self.label_status = tk.Label(self.window, text="Gateway is starting...", justify=tk.LEFT)
        self.label_status.pack()

        # Button to move step by step
        self.button_next = tk.Button(self.window, text="Next Step (Click Here)", command=self.next_step)
        self.button_next.pack()

        self.window.mainloop()

    def next_step(self):
        # Step 1: Ricezione della DHCP Discovery
        if self.step == 0:
            self.label_status.config(text="Step 1: Ricevuta richiesta DHCP Discovery dal PC.")
            self.step += 1
        
        # Step 2: Invio della DHCP Offer
        elif self.step == 1:
            self.label_status.config(text=f"Step 2: Invio DHCP Offer:\nIP: {self.dhcp_offer['IP']}\nNetmask: {self.dhcp_offer['Netmask']}\nGateway: {self.dhcp_offer['Gateway']}\nDNS: {self.dhcp_offer['DNS']}")
            self.step += 1
        
        # Step 3: DHCP Request dal PC
        elif self.step == 2:
            self.label_status.config(text="Step 3: Ricevuta DHCP Request dal PC.\nAttesa conferma.")
            self.step += 1
        
        # Step 4: DHCP Acknowledge
        elif self.step == 3:
            self.label_status.config(text=f"Step 4: DHCP Acknowledge inviato al PC.\nIP assegnato: {self.dhcp_offer['IP']}")
            self.step += 1

        # Step 5: Ricezione ARP Request
        elif self.step == 4:
            self.label_status.config(text="Step 5: Ricevuta ARP Request in broadcast dal PC.")
            self.step += 1

        # Step 6: Invio ARP Reply
        elif self.step == 5:
            gateway_mac = "00:0c:29:ab:cd:ef"
            self.label_status.config(text=f"Step 6: ARP Reply inviato con il MAC: {gateway_mac}.")
            self.step += 1

        # Step 7: Comunicazione avviata
        elif self.step == 6:
            self.label_status.config(text="Step 7: Comunicazione avviata con il PC.")
            self.step += 1

# Esecuzione del server Gateway
gateway_simulation = GatewayServer()
