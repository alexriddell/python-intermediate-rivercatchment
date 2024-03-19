flag : bool = True

def greet(name: str) -> None:
 print("Hi " + name)
       
def greet_all(names: list[str]) -> None:
    for name in names:
        greet(name)

#  For some type t then list[t] captures lists of elements (all) of type t
some_data : tuple[int, bool, str] = (42, True, "Manchester")
    # see below when we change say True from bool to int that it gives error using my py
#some_more_data : tuple[int, bool, str] = (42, 42, "Manchester")

# dictionaries , captures recrods/dictonaries of key ka nd value v type
x: dict[str, float] = {"field1": 2.0, "field2": 3.0}

# t1 | t2 captures either type t1 or t2 type = using | symbol = pipe
def myDiv(x : float, y : float) -> (float | None):
 if y != 0: return x / y
 else: return None

myDict : dict[str, float | str] = {"temp" : 273.0, "units": "Kelvin"}
# union of the two data sets, either this thing or this thing

#complex is the name of the type- corresponding to the class
#any time define a class it use complex
# every class name is a type constructur
class Complex:
 def __init__(self, realpart, imagpart):
    self.r = realpart
    self.i = imagpart
h : Complex = Complex(3.0, -4.5)

#quering mypy
#asking mypy what it thinks the type is
#reveal_type(myDict)
# can use this to inseoct the type of functions etc.

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    reveal_type(len)


from typing import Iterable

#can capture the data type and select the right types
def greet_all(names: Iterable[str]) -> None:
    for name in names:
        greet(name)

def greet_all(names: Iterable[str]) -> None:
 for name in names:
    print('Hello ' + name)
names = ["Alice", "Brijesh", "Chenxi"]
greet_all(names) # Ok

from typing import TypeVar, Generic
T = TypeVar('T')
def first(xs : list[T]) -> type[T]:
 return xs[0]

example0 = first([1,2,3,4])
#reveal_type(example0)

from typing import Callable
S = TypeVar('S')
T = TypeVar('T')
def memo(f : Callable[[S], T], x : S) -> tuple[S,T]:
 return (x, f(x))
