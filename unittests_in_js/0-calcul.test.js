const calculateNumber = require('./0-calcul');
const assert = require('assert').strict;

describe(['calculateNumber test'], function() {
    it(['should round the numbers and give their sum'], function() {
            assert.strictEqual(calculateNumber(1.4, 2.6), 4);
            assert.strictEqual(calculateNumber(5, 6), 11);
            assert.strictEqual(calculateNumber(-1.3, -2.7), -4);
            assert.strictEqual(calculateNumber(0, 0), 0);
            assert.strictEqual(calculateNumber(12.45678, 5.6789), 18);
    });
});
