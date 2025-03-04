import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// set new keyvalue pair in redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) console.error(err);
    console.log(`Reply: ${reply}`);
  });
}

// get the value of a key from redis
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
    if (err) console.error(err);
    console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
