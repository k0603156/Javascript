const {
  delay, go2, curryFilter, range, log, curryMap, curryTakeWhile2, flat, curryTake
} = require('./lib.js');

console.group('아임포트 결제 누락 싱크');

const Impt = {
  payments: {
    0: [{iid: 11, oid: 1}, {iid: 12, oid: 2}, {iid: 13, oid: 3}],
    1: [{iid: 14, oid: 4}, {iid: 15, oid: 5}, {iid: 16, oid: 6}],
    2: [{iid: 17, oid: 7}, {iid: 18, oid: 8}],
    3: [],
    4: []
  }, // 아임포트 서버 데이터. 기결제
  getPayments: page => {
    console.log(`http://..?page=${page}`);
    return delay(100, Impt.payments[page]);
  },
  canclePayment: paymentId => Promise.resolve(`${paymentId}: 취소완료`)
};

const getOrders = ids => delay(100, [{id: 1}, {id: 3}, {id: 7}]);
// 사측 서버 데이터. 기결제
async function job () {
  const payments = await go2(range(Infinity),
    curryMap(Impt.getPayments),
    curryTakeWhile2(ps => ps.length),
    flat,
    curryTake(Infinity));
  const orderIds = await go2(payments,
    curryMap(p => p.oid),
    curryTake(Infinity),
    getOrders,
    curryMap(o => o.id),
    curryTake(Infinity)
  );
  return Promise.all(go2(payments,
    curryFilter(p => !orderIds.includes(p.oid)),
    curryMap(p => p.iid),
    curryTake(Infinity),
    curryMap(Impt.canclePayment),
    curryTake(Infinity)
  ));
}
async function recur () {
  return Promise.all([delay(1000 * 3), job().then(log)]).then(recur);
}
recur();
// curryTakeWhile2(a => a < 2, [Promise.resolve(1)], [Promise.resolve(2)]).then(log);
