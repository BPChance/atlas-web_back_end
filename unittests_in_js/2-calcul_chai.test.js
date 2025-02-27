const calculateNumber = require('./2-calcul_chai');
const assert = require('assert').strict;
const expect = require('chai').expect;

describe('calculateNumber test ADD', function () {
  it('should round the numbers and return their sum', function () {
    expect(calculateNumber('SUM', 1, 2)).to.equal(3);
    expect(calculateNumber('SUM', 1.5, 3.6)).to.equal(6);
    expect(calculateNumber('SUM', 5, 6)).to.equal(11);
    expect(calculateNumber('SUM', -1.3, -2.7)).to.equal(-4);
    expect(calculateNumber('SUM', 0, 0)).to.equal(0);
    expect(calculateNumber('SUM', 12.45678, 5.6789)).to.equal(18);
  });
});

describe('calculateNumber test SUBSTRACT', function () {
  it('should round the numbers and return their difference', function () {
    expect(calculateNumber('SUBTRACT', 1.5, 3.6)).to.equal(-2);
    expect(calculateNumber('SUBTRACT', 6, 5)).to.equal(1);
    expect(calculateNumber('SUBTRACT', -1.3, -2.7)).to.equal(2);
    expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
    expect(calculateNumber('SUBTRACT', 12.45678, 5.6789)).to.equal(6);
  });
});

describe('calculateNumber test DIVIDE', function () {
  it('should round the numbers and return their quotient', function () {
    expect(calculateNumber('DIVIDE', 4.2, 1.6)).to.equal(2);
    expect(calculateNumber('DIVIDE', 6, 3)).to.equal(2);
    expect(calculateNumber('DIVIDE', -8.2, -3.7)).to.equal(2);
    expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 12.45678, 5.6789)).to.equal(2);
  });
});
