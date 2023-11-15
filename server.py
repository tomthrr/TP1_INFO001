import socket
import ssl

# Création d'une socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison de la socket au port
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(5)

print("Le serveur écoute...")

# Accepter les connexions entrantes
client_socket, client_address = server_socket.accept()

# Configuration du contexte SSL avec votre certificat et votre clé
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('serveur_http.cert.pem', 'serveur_http.pem')

# Utilisation du contexte SSL pour sécuriser la connexion
secure_client_socket = ssl_context.wrap_socket(client_socket, server_side=True)

# Réception des données du client
data = secure_client_socket.recv(1024)
print(f"Données reçues du client : {data.decode()}")

# Envoi de données au client
secure_client_socket.sendall("Message du serveur : Bonjour !".encode())

# Fermeture de la connexion
secure_client_socket.close()
server_socket.close()