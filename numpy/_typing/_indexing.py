from types import EllipsisType
from typing import SupportsIndex

from ._array_like import _ArrayLikeInt_co

# Anything that can be used as a key for (basic or advanced) indexing
type _ToIndices = (
    SupportsIndex
    | slice
    | EllipsisType
    | _ArrayLikeInt_co
    | tuple[SupportsIndex | slice | EllipsisType | _ArrayLikeInt_co | None, ...]
    | None
)
