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

describe('Cart page', function () {
  it('should return correct status code when id is a number', function (done) {
    chai
      .request('http://localhost:7865')
      .get('/cart/123')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.text).to.equal('Payment methods for cart 123\n');
        done();
      });
  });

  it('should return 404 when id is not a number', function (done) {
    chai
      .request('http://localhost:7865')
      .get('/cart/abc')
      .end((err, res) => {
        expect(res).to.have.status(404);
        done();
      });
  });
});
