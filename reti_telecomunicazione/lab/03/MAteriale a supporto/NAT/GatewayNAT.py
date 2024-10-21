import tkinter as tk

class GatewayNAT:
    def __init__(self):
        self.public_ip = '203.0.113.1'
        self.dns_table = {'www.example.com': '93.184.216.34'}  # DNS fittizio
        self.nat_table = []  # Tabella NAT vuota all'inizio
        self.current_step = 0  # Passo della simulazione
        self.pc_ip_private = '192.168.1.2'  # IP privato del PC
        self.pc_ip_public = None  # IP pubblico dopo la traduzione NAT
        
        # Finestra Tkinter per il Gateway
        self.window = tk.Tk()
        self.window.title("Gateway NAT Simulation")
        
        # Label per visualizzare gli step
        self.status_label = tk.Label(self.window, text="In attesa di richieste dagli host della LAN...")
        self.status_label.pack()
        
        # Tabella NAT
        self.nat_table_label = tk.Label(self.window, text="Tabella NAT (vuota):")
        self.nat_table_label.pack()

        self.nat_table_frame = tk.Frame(self.window)
        self.nat_table_frame.pack()
        
        self.update_nat_table()

        # Bottone per gestire lo step successivo
        self.button = tk.Button(self.window, text="Gestisci passo successivo", command=self.handle_next_step)
        self.button.pack()

    def update_nat_table(self):
        # Cancella il contenuto attuale della tabella NAT
        for widget in self.nat_table_frame.winfo_children():
            widget.destroy()
        
        # Intestazione della tabella NAT
        tk.Label(self.nat_table_frame, text="IP Privato", borderwidth=1, relief="solid").grid(row=0, column=0)
        tk.Label(self.nat_table_frame, text="IP Pubblico", borderwidth=1, relief="solid").grid(row=0, column=1)
        tk.Label(self.nat_table_frame, text="IP Destinazione", borderwidth=1, relief="solid").grid(row=0, column=2)
        
        # Mostra i dati della tabella NAT
        for i, entry in enumerate(self.nat_table):
            tk.Label(self.nat_table_frame, text=entry['private_ip'], borderwidth=1, relief="solid").grid(row=i+1, column=0)
            tk.Label(self.nat_table_frame, text=entry['public_ip'], borderwidth=1, relief="solid").grid(row=i+1, column=1)
            tk.Label(self.nat_table_frame, text=entry['destination_ip'], borderwidth=1, relief="solid").grid(row=i+1, column=2)

    def handle_next_step(self):
        # Gestione step della simulazione
        if self.current_step == 0:
            self.status_label.config(text="Query DNS ricevuta dal PC verso www.example.com...")
        elif self.current_step == 1:
            self.status_label.config(text="Risoluzione del nome avvenuta. IP address: 93.184.216.34")
        elif self.current_step == 2:
            self.status_label.config(text="Invio risposta DNS al PC. IP risolto: 93.184.216.34")
        elif self.current_step == 3:
            self.status_label.config(text="Richiesta HTTP ricevuta dal PC verso 93.184.216.34")
        elif self.current_step == 4:
            # Step NAT: Sostituzione dell'IP sorgente del PC con l'IP pubblico del Gateway
            self.pc_ip_public = self.public_ip
            self.status_label.config(text=f"Sostituzione IP sorgente con IP pubblico: {self.public_ip}")
            
            # Aggiunta dell'entrata nella tabella NAT
            self.nat_table.append({
                'private_ip': self.pc_ip_private,
                'public_ip': self.public_ip,
                'destination_ip': '93.184.216.34'
            })
            
            self.update_nat_table()  # Aggiorna la visualizzazione della tabella NAT

        elif self.current_step == 5:
            self.status_label.config(text="Comunicazione inoltrata verso l'indirizzo 93.184.216.34 con IP pubblico.")
        elif self.current_step == 6:
            # Step 6: La pagina web torna indietro dal server al Gateway
            self.status_label.config(text="Risposta HTTP ricevuta dall'IP 93.184.216.34.")
        elif self.current_step == 7:
            # Step 7: Il Gateway inoltra la risposta HTTP al PC, sostituendo l'IP pubblico con l'IP privato del PC
            self.status_label.config(text=f"Inoltro della risposta HTTP al PC {self.pc_ip_private} (sostituzione IP pubblico con IP privato).")
        else:
            self.status_label.config(text="Transazione completata. Il PC ha ricevuto la pagina web.")
        
        self.current_step += 1
        self.window.update()

    def run(self):
        self.window.mainloop()

# Avvio dell'applicazione Gateway NAT
if __name__ == "__main__":
    gateway = GatewayNAT()
    gateway.run()
