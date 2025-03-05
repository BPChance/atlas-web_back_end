import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const hashKey = 'HolbertonSchools';

const schools = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

function storeHashData() {
  for (const [field, value] of Object.entries(schools)) {
    client.hset(hashKey, field, value, (err, reply) => {
      if (err) console.error(err);
      console.log(`Reply: ${reply}`);
    });
  }
}

function displayHashData() {
  client.hgetall(hashKey, (err, result) => {
    if (err) console.error(err);
    console.log(result);
  });
}

storeHashData();
setTimeout(displayHashData, 1000);
