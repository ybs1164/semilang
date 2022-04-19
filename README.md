# semilang

본 semilang(세미랭)은 **일반인을 위한 프로그래밍 언어**입니다.

## 개발 기여 규칙

변수, 함수명들은 전부 snail_case 로 작성해주세요.

class 명들은 전부 UpperCamelCase 로 작성해주세요.

문자열들은 전부 "" 로 통일합니다.

## 문법

! 문법은 아직 완성되지 않았습니다. 문법에 대한 의견이 있다면 언제든지 제시 부탁드리겠습니다.

    <block> ::= <stat>+
    
    <stat> ::= <define> '\n'
    
    <define> ::= <identifier> 'is' <expr>

    <expr> ::= <number> | <identifier>
    
    <number> ::= (0-9)+
    
    <identifier> ::= (a-z | A-Z | _)(a-z | A-Z | _ | 0-9)*

## Notion Document

https://www.notion.so/4bce2542163547fdb88e2a168efba270


## TODOist

> C transpiler

> `__repr__` implement of `ast_.py`

## Reference

rply - https://github.com/alex/rply

