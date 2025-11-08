gen:
	uv run python -m grpc_tools.protoc test.proto --python_out=. --mypy_out=. -I .
	# Copy the generated files to the broken and fixed workspaces
	cp test_pb2.py ../broken/test_pb2.py
	cp test_pb2.pyi ../broken/test_pb2.pyi
	cp test_pb2.py ../fixed/test_pb2.py
	cp test_pb2.pyi ../fixed/test_pb2.pyi
