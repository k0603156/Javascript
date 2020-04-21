### git add . 대신 git add -p

```bash
$git add .
```

흔한 실수

- 커밋하면 안되는 파일을 커밋에 포함
- debug 코드를 커밋에 포함

```bash
$git status
```

modified, not staged 파일 리스트를 확인하며 staging

하지만 파일단위의 리스트 코드까지 체크할 수는 없다.

커밋에 추가 되어야할 것은 변경사항(코드)이지 파일이 아니다.

```bash
$git add -p

diff --git del.js add.js
index 2rf23rw1..35w342e 221323
--- del.js
+++ add.js

- code.....
+ code.....
Stage this hunk [y,n,q,a,d,/,s,e,?]
```

modified 파일의 수정 부분을 단위별로 분할해 추가 여부를 확인한다.

?를 입력 하면 명령어 상세를 볼 수 있다.

```bash
y - stage this hunk
n - do not stage this hunk
q - quit; do not stage this hunk or any of the remaining ones
a - stage this hunk and all later hunks in the file
d - do not stage this hunk or any of the later hunks in the file
g - select a hunk to go to
/ - search for a hunk matching the given regex
j - leave this hunk undecided, see next undecided hunk
J - leave this hunk undecided, see next hunk
k - leave this hunk undecided, see previous undecided hunk
K - leave this hunk undecided, see previous hunk
s - split the current hunk into smaller hunks
e - manually edit the current hunk
? - print help
```

```
y - hunk를 stage에 추가
n - stage에 추가하지 않음. 다음으로
q - 과정을 종료
s - hunk의 단위를 더 세분화
```

- staging 이전 추가 되는 변경사항(코드)을 확인 가능.
  - 이 단계에서 디버깅 코드나 불필요한 코드를 제거가능.
- 함수의 의존, 테스트, 수정중 발견된 버그 등 여러 이유로 커밋단위 이외 작업이 섞이는 경우
  - 작업의 완료 후 관련된 부분을 나누어 staging할 수 있다.
- 더 논리적인 단위의 커밋이 가능
- untracked 파일은 -p 할 때 나오지 않음. 새로운 파일의 추가를 의식하게 됨.
