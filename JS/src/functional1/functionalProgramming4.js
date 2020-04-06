const {
  log, curryReduce
} = require('./lib.js');

// console.group('Monad, Promise');

// const g = a => a + 1;
// const f = a => a * a;
// // log(f(g(1)));
// [1].map(g).map(f).forEach(a => log(a));
// Promise.resolve(1).then(g).then(f).then(a => log(a));

// console.group('Kleisli Composition, Promise');

// const g2 = JSON.parse;
// const f2 = ({
//   k
// }) => k;
// const fg = x => Promise.resolve(x)
//   .then(g2)
//   .then(f2);
// fg('{"k":10}').then(log);
// fg('{"k:10}').catch(_ => 'err').then(log);

// console.group('1급 함수, Promise, go1');
// delay
const delay = (time, a) => new Promise(resolve =>
  setTimeout(() => resolve(a), time)
);
// delay(1000, 5).then(log);
// go
const go1 = (a, f) => a instanceof Promise ? a.then(f) : f(a);
const go = (...as) => curryReduce(go1, as);
// const a = 10;
// const b = delay(1000, 5);
// go1(a, log);
// go1(b, log);
const log2 = (a, bs) => {
  bs ? console.log(bs, a) : console.log(a);
  return a;
};
// const b = go(Promise.resolve(1),
//   a => a + 1,
//   a => log2(a, 'b1:'),
//   a => delay(1000, a + 2),
//   a => log2(a, 'b2:'),
//   a => delay(1000, a + 2),
//   a => log2(a, 'b3:'));
// b.then(log);

async function af () {
  const c = await go(Promise.resolve(1), a => a + 1,
    a => log2(a, 'c1:'),
    a => delay(1000, a + 2),
    a => log2(a, 'c2:'),
    a => delay(3000, a + 2)
  );
  const d = await go(Promise.resolve(1), a => a + 1,
    a => log2(a, 'd1:'),
    a => delay(1000, a + 2),
    a => log2(a, 'd2:'),
    a => delay(1000, a + 2)
  );
  log(c, d);
}
af();
