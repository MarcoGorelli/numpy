from typing import Any

import numpy as np
import numpy.ma
from typing_extensions import assert_type


m: np.ma.MaskedArray[Any, np.dtype[np.float64]] = np.ma.masked_array([1.5, 2, 3], mask=[True, False, True])

assert_type(int(m[1:2]), int)
assert_type(float(m[1:2]), int)
