import socket
import ssl

# Configuration du contexte SSL
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations('nginx-reverse/ssl/serveur_http.pem')

# Création du socket SSL
client_socket = socket.create_connection(('localhost', 443))
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

# Envoi d'un message au serveur
message = "Bonjour depuis le client!"
ssl_socket.send(message.encode())

# Fermeture de la connexion
ssl_socket.close()
