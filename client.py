import socket
import ssl

# Création d'une socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect(('www.thierry.fr', 8080))

# Configuration du contexte SSL
ssl_context = ssl.create_default_context()

# Utilisation du contexte SSL pour sécuriser la connexion
secure_client_socket = ssl_context.wrap_socket(client_socket, server_hostname='www.thierry.fr')

# Envoi de données au serveur
message = "Message du client : Bonjour serveur !"
secure_client_socket.sendall(message.encode())

# Réception des données du serveur
data = secure_client_socket.recv(1024)
print(f"Données reçues du serveur : {data.decode()}")

# Fermeture de la connexion
secure_client_socket.close()