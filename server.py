import socket
import ssl

# Chemin vers les fichiers de certificat et de clé privée
certfile = 'serveur_http.cert.pem'
keyfile = 'serveur_http.pem'

# Configuration du contexte SSL
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=certfile, keyfile=keyfile)

# Création du socket SSL
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 443))
server_socket.listen(1)

# Attente de connexion
print("En attente de connexion...")
client_socket, addr = server_socket.accept()

# Handshake SSL
ssl_socket = context.wrap_socket(client_socket, server_side=True)
print(f"Connexion établie avec {addr}")

# Réception et affichage du message du client
data = ssl_socket.recv(1024)
print(f"Message reçu du client : {data.decode()}")

# Fermeture des connexions
ssl_socket.close()
server_socket.close()
