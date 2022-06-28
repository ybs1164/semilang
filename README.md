# semilang

본 semilang(세미랭)은 **일반인을 위한 프로그래밍 언어**입니다.


## 개발 기여 규칙

변수, 함수명들은 전부 snail_case 로 작성해주세요.

class 명들은 전부 UpperCamelCase 로 작성해주세요.


## 문법

문법은 아직 완성되지 않았습니다. 문법에 대한 의견이 있다면 언제든지 제시 부탁드리겠습니다.
아래에 표기된 문법은 현재 구현되어야 할 문법들입니다. 구현된 문법들은 Notion 문서를 참고해주세요.

    <block> ::= <stat>+ <laststat>?
    
    <stat> ::= <define> | <print> | <if>

    <laststat> ::= 'return' <expr>
    
    <define> ::= <identifier> 'is' <expr>
    
    <print> ::= 'print' <expr>
    
    <if> ::= 'if' <expr> 'then' <block> ('else' <if>) 'else' <block> 'end'

    <expr> ::= <number> | <string> | <function> | <prexpr> | <expr> <binop> <expr>
    
    <function> ::= 'function' '(' <identifier> ')' <block> 'end'

    <prexpr> ::= <identifier> | <application> | '(' <expr> ')'

    <application> ::= <prexpr> '(' <expr> ')'
    
    <binop> ::= '+' | '-' | '*' | '/' | '<' | '>' | '<=' | '>=' | '==' | '!=' | 'and' | 'or'

    <string> ::= '"' %s '"'
    
    <number> ::= [0-9]+
    
    <identifier> ::= [a-z | A-Z | _][a-z | A-Z | _ | 0-9]*


## Notion Document

https://www.notion.so/4bce2542163547fdb88e2a168efba270


## 실행 방법

직접 돌려보고픈 분들을 위해 가이드라인을 간단하게라도 작성해보겠습니다.

일단 제가 돌려본 환경은 `wsl2 ubuntu`이므로, 안돌아간다면 저에게 연락을 남겨주시면 감사하겠습니다.

1. `python3 (>=3.9)`, `pip3`을 깔아주셔야 하고, `poetry`를 통해 관련 라이브러리들을 다운받아주시면 됩니다.

2. `./semilang --help`또는 `poetry run semilang --help`를 통해 사용법을 확인해주세요.

3. 사용법을 읽어주시고, `./semilang [args]`또는 `poetry run semilang [args]`를 통해 `semilang`을 사용해보시면 됩니다.



## TODOist

> impl function

> impl string

> impl float


## Reference

rply - https://github.com/alex/rply

