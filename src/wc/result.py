from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar, Union, cast

Input = TypeVar("Input")
Output = TypeVar("Output")
Error = TypeVar("Error")
NewError = TypeVar("NewError")

@dataclass(frozen=True)
class Ok(Generic[Input]):
    value: Input

    def map(self, f: Callable[[Input], Output]) -> Result[Output, Error]:
        return Ok(f(self.value))
    
    def bind(self, f: Callable[[Input], Result[Output, NewError]]) -> Result[Output, NewError]:
        return f(self.value)
    
    def map_err(self, f: Callable[[Error], NewError]) -> Result[Input, NewError]:
        return cast(Result[Input, NewError], self)
    
@dataclass(frozen=True)
class Err(Generic[Error]):
    error: Error

    def map(self, f: Callable[[Input], Output]) -> Result[Output, Error]:
        return cast(Result[Output, Error], self)
    
    def bind(self, f: Callable[[Input], Result[Output, Error]]) -> Result[Output, Error]:
        return cast(Result[Output, Error], self)
    
    def map_err(self, f: Callable[[Error], NewError]) -> Result[Input, NewError]:
        return Err(f(self.error))

Result = Union[Ok[Input], Err[Error]]

__all__ = ["Ok", "Err", "Result"]