## Module - export import

모듈이란 애플리케이션을 구성하는 개별적 요소로서 재사용 가능한 코드 조각을 말한다. 모듈은 세부 사항을 캡슐화하고 공개가 필요한 API만을 외부에 노출한다.

웹에서는 해당 페이지의 모든 파일을 미리 불러와야하고 각 파일마다 스코프를 가지지 않고 결국 하나의 전역객체를 공유하게 된다.
이로 인해 변수가 중복될 위험이 높아지는 것이다.
JS파일을 로딩하는 순서도 중요해 예로 jQuery의 경우 스크립트의 최 상위에 올려 두지않으면 \$ is not defined 같은 에러를 볼 수있다.

패키지의 의존성에서도 모든 스크립트를 불러오기 때문에 각 파일에서 사용하는 패키지를 서로 다른 파일들에서 접근 할 수있다는 점도 문제이다.

이를 해결하기 위한 방법으로 Module이라는 개념이 도입되었다.

Chrome 61, FF 60, SF 10.1, Edge 16 이상에서 사용가능

```javascript
<script type="module" src="lib.mjs"></script>
<script type="module" src="app.mjs"></script>
```

단, 아래와 같은 이유로 아직까지는 브라우저가 지원하는 ES6 모듈 기능보다는 Webpack 등의 모듈 번들러를 사용하는 것이 일반적이다.

-IE를 포함한 구형 브라우저는 ES6 모듈을 지원하지 않는다.

-브라우저의 ES6 모듈 기능을 사용하더라도 트랜스파일링이나 번들링이 필요하다.

-아직 지원하지 않는 기능(Bare import 등)이 있다.

-점차 해결되고는 있지만 아직 몇가지 이슈가 있다.

사용법

```javascript
export { name1, name2, …, nameN };
export { variable1 as name1, variable2 as name2, …, nameN };
export let name1, name2, …, nameN; // var, const에서 동일
export let name1 = …, name2 = …, …, nameN; // var, const에서 동일
export function FunctionName(){...}
export class ClassName {...}

export default expression;
export default function (…) { … } // class, function* 에서 동일
export default function name1(…) { … } // class, function* 에서 동일
export { name1 as default, … };

export * from …;
export { name1, name2, …, nameN } from …;
export { import1 as name1, import2 as name2, …, nameN } from …;
export { default } from …;
```

```javascript
import name from "module-name";
import * as name from "module-name";
import { member } from "module-name";
import { member as alias } from "module-name";
import { member1 , member2 } from "module-name";
import { member1 , member2 as alias2 , [...] } from "module-name";
import defaultMember, { member [ , [...] ] } from "module-name";
import defaultMember, * as alias from "module-name";
import defaultMember from "module-name";
import "module-name";
```

-ES6 모듈은 파일 자체의 스코프를 제공한다. 즉, ES6 모듈은 독자적인 모듈 스코프를 갖는다. 따라서, 모듈 내에서 var 키워드로 선언한 변수는 더 이상 전역 변수가 아니며 window 객체의 프로퍼티도 아니다.

-모듈 내에서 선언한 변수는 모듈 외부에서 참조할 수 없다. 스코프가 다르기 때문이다.

Node.js에서 require("")를 사용 하듯 Node.js에서는 아직 ES6의 모듈 시스템을 완벽하게 지원하지 않는다.
