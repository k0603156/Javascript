/* eslint-disable no-unused-vars */

const curry = f => (a, ...bs) =>
  bs.length ? f(a, ...bs) : (...bs) => f(a, ...bs);
exports.curry = curry;

const go = (a, ...fs) => curryReduce((a, f) => f(a), a, fs);
exports.go = go;

const curryFilter = curry(function * (f, iter) {
  for (const v of iter) {
    // log("filter:", v);
    if (f(v)) yield v;
  }
});
exports.curryFilter = curryFilter;

const curryMap = curry(function * (f, iter) {
  for (const v of iter) {
    // log("map:", v);
    yield f(v);
  }
});
exports.curryMap = curryMap;

const curryReduce = curry(function (f, acc, iter) {
  if (arguments.length === 2) {
    iter = acc[Symbol.iterator]();
    acc = iter.next().value;
  };
  for (const v of iter) {
    acc = f(acc, v);
  }
  return acc;
});
exports.curryReduce = curryReduce;

const curryTake = curry(function (length, iter) {
  const res = [];
  for (const v of iter) {
    res.push(v);
    if (res.length === length) return res;
  }
  return res;
});
exports.curryTake = curryTake;

const flat = function * (iter) {
  for (const a of iter) {
    if (a && a[Symbol.iterator]) {
      yield * a;
    } else yield a;
  }
};
exports.flat = flat;

exports.log = console.log;
