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

describe('login endpoint', function () {
  it('should return welcome message', function (done) {
    chai
      .request('http://localhost:7865')
      .post('/login')
      .send({ userName: 'Braden' })
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.text).to.equal('Welcome Braden');
        done();
      });
  });

  it('should return 400 when no username', function () {
    chai
      .request('http://localhost:7865')
      .post('/login')
      .send({})
      .end((err, res) => {
        expect(res).to.have.status(400);
        expect(res.text).to.equal('Missing userName');
        done();
      });
  });
});
