# Generates error

`uv run mypy main.py`

```
test_pb2.pyi:7: error: Cannot find implementation or library stub for module named "google"  [import-not-found]
test_pb2.pyi:7: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
main.py:5: note: Revealed type is "Any"
Found 1 error in 1 file (checked 1 source file)
```
