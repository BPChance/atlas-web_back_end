const express = require('express');
const app = express();
const countStudents = require('./3-read_file_async');

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
})

app.get('/students', (req, res) => {
    const dbFile = process.argv[2];
    header = 'This is the list of our students\n';

    const originalLog = console.log;
    const logs = [];
    console.log = (message) => logs.push(message);

    countStudents(dbFile)
        .then(() => {
            console.log = originalLog;
            res.send(header + logs.join('\n'));
        })
        .catch((error) => {
            console.log = originalLog;
            res.send(header + error.message);
        });
});

app.listen(1245);
