from typing import IO, Any, overload
from typing_extensions import Literal

#Overloaded methods
@overload
def open_file(filename: str, mode: Literal['r']) -> IO[str]:
    """When 'r' is supplied we return 'str'."""

@overload
def open_file(filename: str, mode: Literal['rb']) -> IO[bytes]:
    """When 'rb' is supplied we return 'bytes' instead of a 'str'."""

@overload
def open_file(filename: str, mode: str) -> IO[Any]:
    """Any other options might return Any-thing!."""

#original method
#Wrapper to original file open command
def open_file(filename: str, mode: str) -> IO[Any]:
    return open(filename, mode)



reveal_type(open_file('some.txt', 'r'))# => Revealed type is 'typing.IO[builtins.str]'
reveal_type(open_file('some.txt', 'rb'))# => Revealed type is 'typing.IO[builtins.bytes]'
reveal_type(open_file('some.txt', 'other'))# => Revealed type is 'typing.IO[Any]'
