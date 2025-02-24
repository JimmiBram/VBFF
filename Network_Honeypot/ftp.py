import socket
import logging

# Konfigurer logging
logging.basicConfig(filename="ftp_connections.log", level=logging.INFO, 
                    format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

def start_ftp_emulator():
    host = "0.0.0.0"  # Lyt på alle netværksinterfaces
    port = 21          # FTP standardport
    
    # Opret en socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Fake FTP-server lytter på {host}:{port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Forbindelse fra {client_address}")
            logging.info(f"Forbindelse fra {client_address}")
            
            # Send en falsk FTP velkomstbesked
            try:
                client_socket.sendall(b"220 Fake FTP Server\r\n")
            except Exception as e:
                logging.error(f"Fejl ved afsendelse af velkomstbesked: {e}")
            
            client_socket.close()

if __name__ == "__main__":
    start_ftp_emulator()
