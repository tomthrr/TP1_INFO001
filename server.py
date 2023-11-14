import socket
import ssl

# Paramètres du serveur
HOST = '127.0.0.1'  # Adresse IP du serveur
PORT = 12345         # Port d'écoute du serveur
CERTFILE = 'serveur_http.cert.pem'  # Chemin vers le certificat du client
KEYFILE = 'serveur_http.pem'   # Chemin vers la clé privée du client

# Création du socket serveur SSL
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# Configuration du contexte SSL
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

print(f"Le serveur écoute sur {HOST}:{PORT}")

# Attente de la connexion d'un client
client_socket, client_address = server_socket.accept()
print(f"Connexion établie avec {client_address}")

# Wrapping du socket dans le contexte SSL
secure_client_socket = context.wrap_socket(client_socket, server_side=True)

while True:
    # Attente de données depuis le client
    data = secure_client_socket.recv(1024).decode('utf-8')

    if not data:
        break

    print(f"Client: {data}")

    # Réponse au client
    message = input("Serveur: ")
    secure_client_socket.send(message.encode('utf-8'))

# Fermeture des connexions
secure_client_socket.close()
server_socket.close()