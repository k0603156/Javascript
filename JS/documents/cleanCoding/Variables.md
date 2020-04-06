## Variables - 변수

#### 의미 있고 읽기 쉬운 변수명 사용

```
Bad: const yyyymmdstr = moment().format("YYYY/MM/DD");

Good: const currentDate = moment().format("YYYY/MM/DD");
```

#### 같은 타입의 변수에 같은 어휘를 사용.

```
Bad:
getUserInfo();
getClientData();
getCustomerRecord();

Good: getUser();
```

#### 검색 가능한 이름을 사용.

```
Bad:
setTimeout(blastOff, 86400000);// 86400000???
Good:


const MILLISECONDS_IN_A_DAY = 86400000;// 대문자 상수로 네이밍
setTimeout(blastOff, MILLISECONDS_IN_A_DAY);
```
