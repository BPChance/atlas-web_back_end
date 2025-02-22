const readline = require('readline');

// create readline interface
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// display welcome
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// read input line
rl.on('line', (input) => {
    const name = input.trim();
    console.log(`Your name is: ${name}`);
    rl.close();
});

// display close message if input is piped
rl.on('close', () => {
    if (!process.stdin.isTTY) {
        console.log('This important software is now closing');
    }
});
