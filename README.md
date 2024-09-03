## Decorator
함수나 메소드에 적용되어 기능을 확장하거나 변경하는 역할을 한다. 일반적으로 '@' 기호와 함께 사용되며, 함수 또는 메소드 상단에 위치한다. 데코레이터는 기본적으로 함수를 인자로 받고, 또 다른 함수를 반환하는 고자함수이다.
<br/><br/>
### 사용하는 이유
1) 코드 재사용성 향상
2) 코드 가독성 향상
3) 관심사 분리
### 주의 사항
* 함수의 메타데이터가 변경될 수 있다. 실행 순서에 주의해야 한다.

### Reference
* [데코레이터(decorator)란?](https://ctkim.tistory.com/entry/%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0decorator)
***
## *args, **kwargs
*args : (positional) arguments
<br/>
가변 인자를 위한 변수이다. 함수의 인자를 몇 개 받아지 모르는 경우에 사용한다. 여러 개의 인자를 하나의 튜플로 묶어 주고 이를 *args에 할당한다.
<br/><br/>
**kwargs : keyword arguments
<br/>
*args와 비슷하게 여러 개의 인자들을 받지만, 딕셔너리 형태로 저장한다. args와 달리 파라미터 명을 같이 보낼 수 있다.
<br/><br/>
### *args와 **kwargs를 같이 사용할 때 주의할 점
1) *args와 **kwargs를 같이 사용할 때, 순서에 맞춰서 쓰면 키워드 아규먼트가 나오기 전에까지는 args가 튜플로 사용하고, 뒤 이어서 키워드 아규먼트는 kwargs가 딕셔터리로 사용한다. <br/>순서를 바꿔서 사용하면 syntax error가 난다.
2) *args1가 있는 함수에서 *args2는 사용할 수 없다. (**kwargs도 마찬가지이다.)
3) 디폴트 값을 가지는 kwargs는 **kwargs 이전에 작성한다.<br/>def example(*args, a=1, b=2, **kwargs):

### Reference
* [파이썬에서 *args, **kwargs는 무엇일까?](https://legitcode267.tistory.com/13)
* [*args와 **kwargs가 뭐예요?](https://velog.io/@clueless_coder/%ED%8C%8C%EC%9D%B4%EC%8D%AC-args-%EC%99%80-kwargs-%EA%B0%80-%EB%AD%90%EC%98%88%EC%9A%94)