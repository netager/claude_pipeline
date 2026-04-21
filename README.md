# claude_pipeline

## Functions

### `add`

```python
def add(a: int | float, b: int | float) -> int | float
```

두 수를 더해 반환합니다.

**예시**

```python
from ex_pipeline import add

add(1, 2)      # 3
add(1.5, 2.5)  # 4.0
```

---

### `divide`

```python
def divide(a: int | float, b: int | float) -> float
```

`a`를 `b`로 나눈 결과를 `float`으로 반환합니다.

- `a`, `b`가 `int` 또는 `float`이 아니면 `TypeError`를 발생시킵니다.
- `b`가 `0`이면 `ValueError`를 발생시킵니다.
- `b`가 `inf` / `-inf` / `nan` 같은 비유한 수이면 `ValueError`를 발생시킵니다.

**예시**

```python
from ex_pipeline import divide

divide(10, 2)    # 5.0
divide(7, 2)     # 3.5
divide(1, 0)     # ValueError: Cannot divide by zero
divide(1, "x")   # TypeError: 'b' must be int or float, got 'str'
```
