### git stash

- 우선순위 요청이 들어와 진행중이던 작업을 멈추고 브랜치를 변경해야 할 상황
- 완료되지 않은 작업을 커밋하고 싶지 않을 때

마무리 되지 않은 작업을 스택에 잠시 저장할 수 있는 명령어.

commit에 추가 하지 않고 다시 꺼내와 진행할 수 있다.

```bash
$git stash
```

- 워킹 디렉토리에서 수정한 파일들만 저장한다.
- stash는 아래 해당하는 파일들을 보관하는 장소
  - modified && tracked state
    - tracked 파일을 수정
    - tracked: commit 되어 스냅샷에 넣어진 추적 대상 파일
  - staging area에 있는 파일
    - git add 된 파일
    - git add 는 새로운 파일을 추적 할 때, 수정된 파일을 staged 로 만들 때 사용

위 명령어를 사용 해 stash 스택에 작업을 임시로 저장한다.

다른 브랜치로 checkout 이 가능하다.

```bash
$git stash list

stash@{0}:.....
stash@{1}:.....
```

stash stack 의 리스트를 확인할 수 있다.

```bash
$git stash apply
or
$git stash apply [stash name]
#git stash apply stash@{1}
```

stash stack 의 작업을 가져온다.

```bash
$git stash apply --index
```

파일의 staged state도 복원

```bash
$git stash drop
or
$git stash drop [stash name]
```

stash stack 에서 제거

```bash
1)
$git stash show -p | git apply -R
2)
$git stash show -p [stash name] | git apply -R
```

1)가장 최근의 stash를 사용하여 패치를 만들고 반대로 적용.
2)stash 이름에 해당하는 stash를 반대로 적용
