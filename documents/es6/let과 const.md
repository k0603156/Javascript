## let과 const

ES2015가 등장하기 전까지는 변수를 선언하기 위해 var 키워드를 주로 사용했다. var 키워드는 이름이 같은 변수를 중복 선언해도 오류가 발생하지 않는다.
또한 블록 단위의 스코프를 지원하지 않는다. var 키워드는 함수 단위의 스코프만 지원한다. { }로 묶여진 블록 내에서 선언한 변수는 별도의 스코프를 만들지 않는다는 것을 의미한다.

ES2015에서는 이러한 문제를 해결하기 위해 let 키워드를 지원한다. 블록 단위의 스코프도 해결했고, 변수의 중복 선언을 방지할 수 있다.

const는 상수 기능을 제공한다. 즉 한 번 값이 주어지면 다시 변경할 수 없다. const 또한 블록 스코프를 제공한다.

기존 var 키워드는 중복 선언을 허용한다. 즉 아래 코드는 오류를 일으키지 않는다.

```javascript
var a = 6;
var a = "js";
var a = { language: "javascript", version: 6 };
```

반면 let과 const는 중복 선언을 허용하지 않는다. 위 코드에서 var 를 let으로 변경하면 오류가 발생한다.

1. const를 기본으로 사용한다.
2. 변경이 될 수 있는 변수는 let을 사용한다.
3. var는 사용하지 않는다.

```
let
block (function, for, if 등) 안에서 유효한 변수

const
const는 수정 불가능한 불변성(immutable)을 말하는 것이 아니라 값 재할당이 불가능한 것이다.
const를 사용하더라도, 배열과 오브젝트의 값을 변경하는 게 가능하다.
```

```javascript
const list = ["godori", "irodog", "roodig"];
list.push("dorigo");
console.log(list); // ["godori","irodog","roodig","dorigo"]
```

##### immutable array

다음과 같은 예제를 보면, 기존 배열을 두고 새로운 배열을 만들어 데이터를 추가한다.

```javascript
const list1 = ["goodori", "irodog", "roodig"];
list2 = [].concat(list1, "dorigo");
console.log(list1 === list2); // false
```

리액트 등에서 state값이 변경되는 경우를 예로 들 수 있다.

주로 리덕스의 리듀스를 이용해 새로운 값을 계속 반환할 때 immutable array를 많이 사용하게 된다.

immutable.js라는 라이브러리를 쓰면 객체 원본은 그대로 두고 복사본을 만드는 방법을 제공한다.

혹은 ES6의 스프레드 연산자를 사용하는 방법도 존재.
