const express = require('express'); 
const https = require('https');
const fs = require('fs');

const app = express();

// Charger les certificats TLS
const options = {
  key: fs.readFileSync('nginx-reverse/ssl/serveur_http.pem'),
  cert: fs.readFileSync('nginx-reverse/ssl/serveur_http.cert.pem')
};

  // Route pour la réception de messages
app.post('/messages', (req, res) => {
  // Recevoir et afficher le message
  console.log('Message reçu :', req.body.message);
  res.sendStatus(200);
});

// Démarrer le serveur HTTPS
https.createServer(options, app).listen(443, () => {
  console.log('Serveur démarré sur le port 443');
});
