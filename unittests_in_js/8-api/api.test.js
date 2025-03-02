const chai = require('chai');
const chaiHttp = require('chai-http');
const { expect } = chai;
const app = require('./api');

chai.use(chaiHttp);

describe('api', function () {
  it('should return correct status code', function (done) {
    chai
      .request(app)
      .get('/')
      .end((err, res) => {
        expect(res).to.have.status(200);
        done();
      });
  });
});
