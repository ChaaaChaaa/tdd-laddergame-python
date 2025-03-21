# 사다리 타기 TDD 구현 프로젝트

이 프로젝트는 next-step의 TDD, 클린 코드 with Java를 Python으로 바꿔 사다리 타기 게임을 구현한 Python 프로젝트입니다. 클린 코드 원칙을 준수하며 단계별로 기능을 확장했습니다.

## 프로젝트 개요

사다리 타기 게임을 TDD 방식으로 구현하며, 다음과 같은 단계로 진행했습니다:
- 1단계: 사다리 생성 및 출력 기능 [ladder-ver1](https://github.com/ChaaaChaaa/tdd-laddergame-python/tree/ladder-ver1)
- 2단계: 사다리 실행 결과 출력 기능 추가 [ladder-ver2](https://github.com/ChaaaChaaa/tdd-lotto-python/tree/lotto-ver2)

## 테스트 전략 및 구현

### 테스트 시뮬레이션

전체 애플리케이션 흐름을 테스트하기 위한 통합 테스트를 구현했습니다:

- 사용자 입력 모킹을 통한 전체 시나리오 테스트
- 각 단계별 기능 검증:
  - 참여자 이름 입력 및 검증
  - 사다리 높이 입력 및 생성
  - 사다리 구조 생성 및 출력
  - 실행 결과 입력 및 개인별/전체 결과 출력



### 단위 테스트

주요 기능별 단위 테스트를 구현했습니다:

#### 사다리 생성 관련 테스트 (ladder_maker)
- 사다리 크기 (높이, 너비) 검증
- 가로 라인 겹치지 않도록 생성 로직 검증
- 랜덤 라인 생성 로직 모킹하여 일관성 있는 결과 검증
- 특수 케이스 처리 (예: 참가자가 한 명일 때)

#### 랜덤 라인 생성 테스트 (random_line_maker)
- 랜덤성 모킹하여 특정 값 반환 여부 검증

#### 입출력 테스트 (script)
- 사용자 입력 처리 테스트
- 결과 출력 테스트


## 테스트 코드 구조

```
tests/
├── integration/
│   └── test_simulation.py - 전체 시뮬레이션 통합 테스트
├── ladder_maker/
│   ├── test_ladder_maker.py - 사다리 구조 생성 로직 테스트
│   └── test_random_line_maker.py - 랜덤 라인 생성 로직 테스트
├── script/
│   ├── test_input.py - 사용자 입력 처리 테스트
│   └── test_output.py - 결과 출력 형식 테스트
└── utils/
    └── test_result_calculator.py - 결과 계산 유틸리티 테스트 (ver2 추가)

```

## 주요 테스트 기법

### 모킹(Mocking)

- 사용자 입력(builtins.input) 모킹
- 랜덤 라인 생성 함수 모킹 (random.choice)
- 출력 함수(sys.stdout) 모킹 및 호출 검증

### 테스트 케이스 설계

- 정상 케이스 검증
- 경계값 케이스 (이름 길이 제한 등)
- 예외 상황 처리 (참가자 한 명 등 특수 케이스)

### 검증 기법

- 예상 결과와 실제 결과 비교 (`assertEqual`)
- 함수 호출 검증 (`assert_called_with`, `assert_has_calls`)
- 예외 발생 검증 (`assertRaises`)

## 구현된 기능

- 참여자 이름 입력 및 길이 제한(최대 5글자)
- 참여자 이름과 높이에 따른 사다리 자동 생성 및 출력
- 가로 라인이 겹치지 않도록 보장하는 로직 구현
- 실행 결과 입력 및 매칭 로직 구현
- 개인별 또는 전체 실행 결과 조회 기능 추가

## 프로젝트 구조

```
ladder/
├── src/
│   ├── ladder_maker/
│   │   ├── ladder_maker.py - 사다리 구조 생성 클래스
│   │   └── random_line_maker.py - 랜덤 라인 생성 함수
│   ├── script/
│   │   ├── input.py - 사용자 입력 처리 함수들
│   │   └── output.py - 결과 출력 처리 함수들
│   └── utils/
│       └── result_calculator.py - 실행 결과 계산 유틸리티
└── tests/ - 위에 설명된 테스트 구조
```


## 기술 스택

- Python 3.10
- unittest 프레임워크
- unittest.mock 모듈

## 개발 원칙

1. TDD 사이클 준수: 실패하는 테스트 작성 → 테스트 통과하는 코드 작성 → 리팩토링
2. 클린 코드 원칙 준수: 의미 있는 이름, 작은 함수, 단일 책임 원칙 등
3. SOLID 원칙 적용
4. 모킹을 통한 외부 의존성 제거
5. 테스트 가능한 코드 설계

## 테스트 실행 방법

```bash
# 모든 테스트 실행하기
python -m unittest discover tests

# 특정 파일만 실행하기 예시:
python -m unittest tests.ladder_maker.test_ladder_maker
python -m unittest tests.integration.test_simulation

```
