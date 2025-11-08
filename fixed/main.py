from typing import reveal_type

import test_pb2

reveal_type(test_pb2.Test.Value("VALUE_A"))
