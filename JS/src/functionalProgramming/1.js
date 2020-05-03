console.group('Simbol');

log(typeof Symbol('')); // 'symbol'
const mySymbol1 = Symbol('mySymbol');
const mySymbol2 = Symbol('mySymbol');
log(mySymbol1 === mySymbol2); // false

console.groupEnd();

console.group('obj');

const prop2 = Symbol('prop2');
const prop3 = Symbol('prop2');
// var prop2 = Symbol.for('prop2')
// var prop3 = Symbol.for('prop2')
const obj = {
  prop1: 1,
  ['prop' + 1]: 2,
  [prop2]: 3,
  [prop3]: 4
};
for (const key in obj) {
  log(key);
}
log(obj.prop1);
// log(obj[prop1]);
log(obj.prop1);
log(obj[prop2]);
log(obj[prop3]);
log(Object.keys(obj));
log(Object.getOwnPropertyNames(obj));
console.groupEnd();
console.group('obj2');
const arr = ['victor', 'dio', 'taek'];
const obj2 = {
  items: [],
  set: function (arr) {
    this.items = arr;
  },
  get: function () {
    return this.items;
  }
};
obj2.setItems = arr;
log(obj2);

obj2[Symbol.iterator] = function * () {
  for (const item of this.items) {
    yield item;
  }
};
log(obj2);

console.groupEnd();
console.group('countdown');
const countdown = {
  max: 3,
  [Symbol.iterator] () {
    return this;
  },
  next () {
    if (this._max === undefined) {
      this._max = this.max;
    }
    if (this._max > -1) {
      return {value: this._max--};
    } else {
      return {done: true};
    }
  }
};
const count = countdown[Symbol.iterator]();

for (const value of count) {
  log(value);
}
console.groupEnd();
console.group('countdown2');
const countdown2 = {
  items: [1, 2, 3],
  max: 0,
  to: 0,
  [Symbol.iterator] () {
    return this;
  },

  next () {
    if (this._max === undefined || this._items === undefined) {
      this._max = this.max;
      this._items = this.items;
      this._to = this.items.length;
    }
    if (this._max < this._to) {
      return {value: this._items[this._max++]};
    } else {
      return {done: true};
    }
  }
};

const count2 = countdown2[Symbol.iterator]();

for (const value of count2) {
  log(value);
}
console.groupEnd();
console.group('mapset');
const map = new Map();
const set = new Set();

map.set('name', 'Mommoo');
map.set('age', 'secret');

set.add('Mommoo');
set.add('secret');

map.forEach((value, key, mapObject) => console.log(key + ' , ' + value));

set.forEach((value1, value2, setObject) => console.log(value1 + ' , ' + value2));

for (const item of map) {
  log(item[0] + ' , ' + item[1]);
}

const map2 = new Map();
const set2 = new Set();

map2.set('name', 'Mommoo');
map2.set('age', 'secret');

set2.add('Mommoo');
set2.add('secret');

const mapIterator = map2.entries();

while (!mapIterator.next().done) {
  const [key, value] = mapIterator.next().value;
  console.log(key + ' , ' + value);
}

const setIterator = set2.entries();

while (!setIterator.next().done) {
  const [value1, value2] = setIterator.next().value;
  console.log(value1 + ' , ' + value2);
}

console.groupEnd();

function log (parm) {
  console.log(parm);
}
