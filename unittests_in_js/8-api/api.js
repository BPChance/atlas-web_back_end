import express from 'express';

const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

let server = null;

if (process.env.NODE_ENV !== 'test') {
  server = app.listen(7865, () => {
    console.log('API available on localhost port 7865');
  });
}
