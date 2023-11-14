import socket
import ssl

# Paramètres du client
HOST = 'www.thierry.fr'  # Adresse IP du serveur
PORT = 12345         # Port d'écoute du serveur
CERTFILE = 'serveur_http.cert.pem'  # Chemin vers le certificat du client
KEYFILE = 'serveur_http.pem'   # Chemin vers la clé privée du client

# Création du socket client SSL
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuration du contexte SSL
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

# Connexion au serveur
secure_client_socket = context.wrap_socket(client_socket, server_hostname=HOST)
secure_client_socket.connect((HOST, PORT))

print(f"Connecté au serveur {HOST}:{PORT}")

while True:
    # Envoi de données au serveur
    message = input("Client: ")
    secure_client_socket.send(message.encode('utf-8'))

    # Attente de la réponse du serveur
    data = secure_client_socket.recv(1024).decode('utf-8')
    print(f"Serveur: {data}")

# Fermeture de la connexion
secure_client_socket.close()