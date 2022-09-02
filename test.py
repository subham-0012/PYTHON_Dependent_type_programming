from typing_extensions import Literal


def function(x: Literal[1]) -> Literal[1]:
     return x

function(1)
# => OK!

function(2)
# => Argument has incompatible type "Literal[2]"; expected "Literal[1]"