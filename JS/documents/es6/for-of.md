### for-of Array

#### 기존의 for-in :

```javascript
var languages = ["javascript", "python"];
Array.prototype.frameworks = ["nodejs", "django"];

for (let idx in languages) {
  console.log(languages[idx]); // javascript, python, ["nodejs", "django"]
}
```

what??!
상위 프로토타입의 객체도 포함해버린다.

#### for-of :

index가 아닌 value 순회가 가능하므로 위와 같은 문제를 방지할 수 있다.

```javascript
var languages = ["javascript", "python"];
Array.prototype.frameworks = ["nodejs", "django"];

for (let language of languages) {
  console.log(language); // javascript, python
}
```

for-in은 인덱스를 받지만 for-of는 배열의 값을 받는다.
