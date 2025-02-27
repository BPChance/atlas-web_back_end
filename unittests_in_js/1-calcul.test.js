const calculateNumber = require('./1-calcul');
const assert = require('assert').strict;

describe('calculateNumber test ADD', function () {
  it('should round the numbers and return their sum', function () {
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.6), 6);
    assert.strictEqual(calculateNumber('SUM', 5, 6), 11);
    assert.strictEqual(calculateNumber('SUM', -1.3, -2.7), -4);
    assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
    assert.strictEqual(calculateNumber('SUM', 12.45678, 5.6789), 18);
  });
});

describe('calculateNumber test SUBSTRACT', function () {
  it('should round the numbers and return their difference', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.6), -2);
    assert.strictEqual(calculateNumber('SUBTRACT', 6, 5), 1);
    assert.strictEqual(calculateNumber('SUBTRACT', -1.3, -2.7), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 0, 0), 0);
    assert.strictEqual(calculateNumber('SUBTRACT', 12.45678, 5.6789), 6);
  });
});

describe('calculateNumber test DIVIDE', function () {
  it('should round the numbers and return their quotient', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 4.2, 1.6), 2);
    assert.strictEqual(calculateNumber('DIVIDE', 6, 3), 2);
    assert.strictEqual(calculateNumber('DIVIDE', -8.2, -3.7), 2);
    assert.strictEqual(calculateNumber('DIVIDE', 0, 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 12.45678, 5.6789), 2);
  });
});
