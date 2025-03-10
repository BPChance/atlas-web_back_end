import chai from 'chai';
import chaiHttp from 'chai-http';
const { expect } = chai;

chai.use(chaiHttp);

describe('Index page', function () {
  it('should return correct status code', function (done) {
    chai
      .request('http://localhost:7865')
      .get('/')
      .end((err, res) => {
        expect(res).to.have.status(200);
        done();
      });
  });

  it('should return correct text response', function (done) {
    chai
      .request('http://localhost:7865')
      .get('/')
      .end((err, res) => {
        expect(res.text).to.equal('Welcome to the payment system');
        done();
      });
  });
});
