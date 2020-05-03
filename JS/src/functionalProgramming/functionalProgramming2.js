const log = console.log;
const go = (a, ...fs) => curryReduce((a, f) => f(a), a, fs);
const curry = f => (a, ...bs) =>
  bs.length ? f(a, ...bs) : (...bs) => f(a, ...bs);
const add = (a, b) => a + b;
const L = {};
L.curryFilter = curry(function * (f, iter) {
  for (const v of iter) {
    // log("filter:", v);
    if (f(v)) yield v;
  }
});

L.curryMap = curry(function * (f, iter) {
  for (const v of iter) {
    // log("map:", v);
    yield f(v);
  }
});

const curryTake = curry(function (length, iter) {
  const res = [];
  for (const v of iter) {
    res.push(v);
    if (res.length === length) return res;
  }
  return res;
});

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

const arr = [
  [1, 3], 3, 4, 5, [6, 7, 8], [9, 10]
];

console.group('2차원배열');

// L.flat = function* (iter) {
//   for (const a of iter) {
//     if (a && a[Symbol.iterator]) {
//       for (const b of a) yield b;
//     } else yield a;
//   }
// }; =>
L.flat = function * (iter) {
  for (const a of iter) {
    if (a && a[Symbol.iterator]) {
      yield * a;
    } else yield a;
  }
};
const it = L.flat(arr);
log(it.next());
log(it.next());

go(arr,
  L.flat,
  L.curryFilter(a => a % 2),
  L.curryMap(a => a * a),
  curryTake(3),
  curryReduce(add),
  log);
console.groupEnd();
