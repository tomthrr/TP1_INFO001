const https = require('https');

// Options de la requête HTTPS
const options = {
  hostname: 'www.thierry.fr',
  port: 443,
  path: '/messages',
  method: 'POST',
  // Ici, il faut indiquer au client de valider le certificat du serveur
  // Pour cela, tu peux utiliser l'option `rejectUnauthorized`
  rejectUnauthorized: true
};

// Message à envoyer au serveur
const message = JSON.stringify({ message: 'Bonjour depuis le client!' });

// Envoi de la requête HTTPS au serveur
const req = https.request(options, (res) => {
  console.log('Code de réponse :', res.statusCode);
});

req.on('error', (e) => {
  console.error(e);
});

// Envoyer le message dans le corps de la requête
req.write(message);
req.end();
