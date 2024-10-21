import tkinter as tk

class PC:
    def __init__(self):
        self.private_ip = '192.168.1.2'
        self.destination_ip = None  # IP risolto dal DNS
        
        # Finestra Tkinter per il PC
        self.window = tk.Tk()
        self.window.title("PC NAT Simulation")
        
        # Label per visualizzare gli step
        self.status_label = tk.Label(self.window, text="In attesa di avviare la connessione...")
        self.status_label.pack()
        
        # Bottone per inviare la richiesta DNS
        self.button = tk.Button(self.window, text="Invia richiesta DNS", command=self.send_dns_request)
        self.button.pack()
        
        # Variabile per gestire gli step successivi
        self.current_step = 0

    def send_dns_request(self):
        if self.current_step == 0:
            # Step 1: Invia richiesta DNS
            self.status_label.config(text="Richiesta DNS per risoluzione indirizzo www.example.com...")
            self.current_step += 1
        elif self.current_step == 1:
            # Step 2: Ricezione dell'indirizzo IP risolto dal DNS
            self.destination_ip = '93.184.216.34'  # IP fittizio risolto
            self.status_label.config(text=f"DNS risolto con successo. Indirizzo IP: {self.destination_ip}")
            self.button.config(text="Invia richiesta HTTP")
            self.current_step += 1
        elif self.current_step == 2:
            # Step 3: Invia richiesta HTTP all'indirizzo IP risolto
            self.status_label.config(text=f"Richiesta HTTP inviata verso {self.destination_ip}...")
            self.button.config(state="disabled")  # Disabilita il bottone dopo la richiesta
            self.current_step += 1

    def run(self):
        self.window.mainloop()

# Avvio dell'applicazione PC
if __name__ == "__main__":
    pc = PC()
    pc.run()

