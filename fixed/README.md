# No error

`uv run mypy main.py`

```
aidandj@Aidans-MacBook-Pro broken % cd ../fixed/
aidandj@Aidans-MacBook-Pro fixed % uv run mypy main.py
main.py:5: note: Revealed type is "test_pb2._Test.ValueType"
Success: no issues found in 1 source file
```
