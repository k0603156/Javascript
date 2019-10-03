const log = console.log;
const products = [{
    name: 'A',
    price: 15000
  },
  {
    name: 'B',
    price: 20000
  },
  {
    name: 'C',
    price: 30000
  },
  {
    name: 'D',
    price: 40000
  },
];
console.group("모든 물건의 가격 더하기");

const reduceA = (f, acc, iter) => {
  if (!iter) {
    iter = acc[Symbol.iterator]();
    acc = iter.next().value;
  }
  for (const a of iter) {
    acc = f(acc, a);
  }
  return acc;
}
log(reduceA((total_price, product) => total_price + product.price, 0, products));

console.groupEnd();

const list = [1, 2, 3, 4, 5];
console.group("홀수를 length 만큼 뽑아 제곱 후 더하기");

function ImF(list, length) {
  let i = 0;
  let acc = 0;
  for (const v of list)
    if (v % 2) {
      acc = acc + v * v;
      if (++i == length) break;
    }
  log(acc)
}
ImF(list, 3);

console.groupEnd();

console.group("홀수를 length 만큼 뽑아 제곱 후 더하기-함수형");

function* filter(f, iter) {
  for (const v of iter) {
    if (f(v)) yield v;
  }
}

function* map(f, iter) {
  for (const v of iter) {
    yield f(v);
  }
}

function take(length, iter) {
  let res = [];
  for (const v of iter) {
    res.push(v);
    if (res.length == length) return res;
  }
  return res;
}

function reduce(f, acc, iter) {
  for (const v of iter) {
    acc = f(acc, v);
  }
  return acc;
}

const add = (a, b) => a + b;

const funcF = (list, length) =>
  reduce(add, 0,
    take(length,
      map(v => v * v,
        filter(v => v % 2, list))))

log(funcF(list, 3));
console.groupEnd();