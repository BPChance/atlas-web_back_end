const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(function (req, res) {
    res.setHeader('Content-Type', 'text/plain');

    if (req.url === '/') {
        res.statusCode = 200;
        res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
        const dbFile = process.argv[2];
        res.write('This is the list of our students\n');

        const originalLog = console.log;
        const logs = [];
        console.log = (message) => logs.push(message);

        countStudents(dbFile)
            .then(() => {
                console.log = originalLog;
                res.end(logs.join('\n'));
            })
            .catch((error) => {
                console.log = originalLog;
                res.end(error.message);
            });
    } else {
        res.statusCode = 404;
        res.end('Not found');
    }
}).listen(1245);

module.exports = app;
