/* eslint-disable no-unused-vars */
exports.log = console.log;

const log2 = (a, bs) => {
  bs ? console.log(bs, a) : console.log(a);
  return a;
};
exports.log2 = console.log2;

const curry = f => (a, ...bs) =>
  bs.length ? f(a, ...bs) : (...bs) => f(a, ...bs);
exports.curry = curry;

const go = (a, ...fs) => curryReduce((a, f) => f(a), a, fs);
exports.go = go;

const go1 = (a, f) => a instanceof Promise ? a.then(f) : f(a);
exports.go1 = go1;

const go2 = (...as) => curryReduce(go1, as);
exports.go2 = go2;

const curryFilter = curry(function * (f, iter) {
  for (const v of iter) {
    // log("filter:", v);
    if (f(v)) yield v;
  }
});
exports.curryFilter = curryFilter;

const curryMap = curry(function * (f, iter) {
  for (const v of iter) {
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

const curryTakeWhile = curry(function (f, iter) {
  const res = [];
  for (const v of iter) {
    if (!f(v)) return res;
    res.push(v);
  }
  return res;
});
exports.curryTakeWhile = curryTakeWhile;

const curryTakeWhile2 = curry(function (f, iter) {
  iter = iter[Symbol.iterator]();
  iter.return = null; // promise라도 return하지 않음
  const res = [];
  return (function recur () {
    for (const v of iter) {
      const b = go1(v, f);
      if (!b) return res;
      if (b instanceof Promise) return b.then(async b => b ? (res.push(await v), recur()) : res);
      res.push(v);
    }
    return res;
  }());
});
// curryTakeWhile2(a => a < 2, [Promise.resolve(1)], [Promise.resolve(2)]).then(log);
exports.curryTakeWhile2 = curryTakeWhile2;

const flat = function * (iter) {
  for (const a of iter) {
    if (a && a[Symbol.iterator]) yield * a; else yield a;
  }
};
exports.flat = flat;

const delay = (time, a) => new Promise(resolve =>
  setTimeout(() => resolve(a), time)
);
exports.delay = delay;

const range = function * (stop) {
  let i = -1;
  while (++i < stop) yield i;
};
exports.range = range;
