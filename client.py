import socket
import ssl

HOSTNAME = 'www.thierry.fr'
SERVER_HOSTNAME = 'www.thierry.fr'
PORT = 8080

# Création d'une socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect((HOSTNAME, PORT))

# Configuration du contexte SSL
ssl_context = ssl.create_default_context()

# Utilisation du contexte SSL pour sécuriser la connexion
secure_client_socket = ssl_context.wrap_socket(client_socket, server_hostname=SERVER_HOSTNAME)

# Envoi de données au serveur
message = "Message du client : Bonjour serveur !"
secure_client_socket.sendall(message.encode())

# Réception des données du serveur
data = secure_client_socket.recv(1024)
print(f"Données reçues du serveur : {data.decode()}")

# Récupération du certificat du serveur
server_cert = secure_client_socket.getpeercert()

# Affichage des informations du certificat
print("Informations du certificat reçu :")
print(f"Émetteur (issuer): {server_cert['issuer']}\n")

if (SERVER_HOSTNAME in server_cert['subjectAltName'][0][1]):
    print("Le certificat est valide pour le domaine", SERVER_HOSTNAME)  

# Fermeture de la connexion
secure_client_socket.close()