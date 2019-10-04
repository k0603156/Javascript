/* eslint-disable indent */
const log = console.log;
const products = [
{name: 'A', price: 15000}, {name: 'B', price: 20000}, {name: 'C', price: 30000}, {name: 'D', price: 40000}
];
console.group('모든 물건의 가격 더하기');

const reduceA = (f, acc, iter) => {
  if (!iter) {
    iter = acc[Symbol.iterator]();
    acc = iter.next().value;
  }
  for (const a of iter) {
    acc = f(acc, a);
  }
  return acc;
};
log(
  reduceA((totalPrice, product) => totalPrice + product.price, 0, products)
);

console.groupEnd();

const list = [1, 2, 3, 4, 5];
console.group('홀수를 length 만큼 뽑아 제곱 후 더하기');

function ImF (list, length) {
  let i = 0;
  let acc = 0;
  for (const v of list) {
    if (v % 2) {
      acc = acc + v * v;
      if (++i === length) break;
    }
  }
  log(acc);
}
ImF(list, 3);

console.groupEnd();

console.group('홀수를 length 만큼 뽑아 제곱 후 더하기-함수형');

function * filter (f, iter) {
  for (const v of iter) {
    if (f(v)) yield v;
  }
}

function * map (f, iter) {
  for (const v of iter) {
    yield f(v);
  }
}

function take (length, iter) {
  const res = [];
  for (const v of iter) {
    res.push(v);
    if (res.length === length) return res;
  }
  return res;
}

let reduce = (f, acc, iter) => {
  for (const v of iter) {
    acc = f(acc, v);
  }
  return acc;
};

let add = (a, b) => a + b;

let funcF = (list, length) =>
  reduce(add, 0, take(length, map(v => v * v, filter(v => v % 2, list))));

log(funcF(list, 3));
console.groupEnd();

console.group('넘겨받은 함수를 순차적으로 실행');

let go = (a, ...fs) => reduce((a, f) => f(a), a, fs);

go(10, a => a + 10, a => a + 1, log);

console.groupEnd();

console.group('reduce 가변인자');

reduce = function (f, acc, iter) {
  if (arguments.length === 2) {
    iter = acc[Symbol.iterator]();
    acc = iter.next().value;
  }
  for (const v of iter) {
    acc = f(acc, v);
  }
  return acc;
};
log(reduce(add, list));

go = (...as) => reduce((a, f) => f(a), as);

funcF = (list, length) =>
  go(
    list,
    list => filter(v => v % 2, list),
    list => map(v => v * v, list),
    list => take(length, list),
    list => reduce(add, 0, list)
  );

log(funcF(list, 2));

console.groupEnd();

console.group('currying');

const curry = f => (a, ...bs) =>
  bs.length ? f(a, ...bs) : (...bs) => f(a, ...bs);

add = curry((a, b) => a + b);

log(add(10)(5));
log(add(10, 5));
const a = add(10);
log(a(5));

console.groupEnd();

console.group('currying2');

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
  }
  for (const v of iter) {
    acc = f(acc, v);
  }
  return acc;
});

// curryFuncF = (list, length) =>
//   go(
//     list,
//     list => L.curryFilter(v => v % 2)(list),
//     list => L.curryMap(v => v * v)(list),
//     list => curryTake(length)(list),
//     list => curryReduce(add)(list)
//   );
// =>
const curryFuncF = (list, length) =>
  go(
    list,
    L.curryFilter(v => v % 2), // 홀수
    L.curryMap(v => v * v), // 제곱
    curryTake(length), // 원하는개수만
    curryReduce(add) // 더하기
  );

log(curryFuncF(list, 2));
// list= [1,2,3,4,5]
// log(curryFuncF([1,2,3,4,5], 2));
// 결국 배열의 처음 부터 끝까지의 모든 요소가 필요하지 않기에 맨 처음 ImF함수가 더 효율 적이라 생각 할 수 있지만
// 내부적으로 보면 next()호출로 지연 평가가 이루어진다.
// curryFilter와 curryMap의 log함수 주석을 해제해보자.
console.groupEnd();

console.group('iterator next()');

const m = map(a => a + 1, [1, 2, 3]);
log(m.next());
log(m.next());
log(m.next());

console.groupEnd();

console.group('0에서 가장 가까운 홀수인 자연수 100개를 제곱한 합');

L.range = function * (stop) {
  let i = -1;
  while (++i < stop) yield i;
};
log([...L.range(10)]);
log(curryFuncF(L.range(Infinity), 100));

console.groupEnd();
