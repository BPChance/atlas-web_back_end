const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromApi', function () {
  it('should return a resolved promise when success is true', function (done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.deep.equal({
          data: 'Successful response from the API',
        });
        done();
      })
      .catch((error) => done(error));
  });
});
