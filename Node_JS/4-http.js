// create a small HTTP server using the http module:
// It should be assigned to the variable app and this one must be exported
// HTTP server should listen on port 1245
// Displays Hello Holberton School! in the page body for any endpoint as plain text

const http = require('http');

const app = http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.write('Hello Holberton School!');
    res.end();
}).listen(1245);

module.exports = app;
