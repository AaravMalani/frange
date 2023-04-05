"""
This module implements frange (range() for floats)
"""
from __future__ import annotations
import typing


class FRangeIterator:
    """
    Backend iterator for the frange function
    """

    def __init__(self, stop: float, start: float = 0.0, step: float = 1.0):
        self.stop = stop
        self.start = start
        self.step = step
        self.val: typing.Optional[float] = None

    def __iter__(self):
        """
        Initialize iterator

        Returns FRangeIterator
        """
        self.val = self.start
        return self

    def __next__(self) -> float:
        """Yields next value

        Raises:
            StopIteration: If the frange reaches the end

        Returns:
            float: Returns the next value
        """
        if self.val >= self.stop:
            raise StopIteration
        self.val += self.step
        return self.val - self.step

    def __contains__(self, item: float) -> bool:
        """Check if item is in frange

        Args:
            item (float): Item who's existence to check for

        Returns:
            bool: Returns whether item is in frange
        """
        return self.start <= item < self.stop and (item - self.start) % self.step == 0

    def __getitem__(self, items: typing.Union[int, slice]) -> typing.Union[float, FRangeIterator]:
        """Returns item in frange

        Args:
            items (Union[int, slice]): Items to check for

        Raises:
            TypeError: If items is not a int or slice
            IndexError: If the index is not in range

        Returns:
            Union[float, FRangeIterator]: Returns a float if indexed or another iterator if sliced
        """
        if isinstance(items, int):
            if items < 0:
                items = len(self) + items
            if items < 0 or self.start + (items*self.step) >= self.stop or (self.stop - self.start)/self.step < 0:
                raise IndexError("frange object index out of range")
            return self.start + (items*self.step)
        elif isinstance(items, slice):
            start, stop, step = items.start or 0, items.stop or len(
                self), items.step or 1

            if start < 0:
                start = len(self) + start
            if stop < 0:
                stop = len(self) + stop
            return FRangeIterator(self.start + (self.step*stop), self.start+(self.step*start), step*self.step)
        raise TypeError(
            "frange indices must be integers or slices, not "+items.__class__.__name__)

    def __len__(self) -> int:
        """Returns length of frange

        Returns:
            int: Length of frange
        """
        return max(int((self.stop - self.start)//self.step), 0)

    def __repr__(self) -> str:
        """Returns string representation of object

        Returns:
            str: String representation of object
        """
        return f"frange({self.start}, {self.stop}, {self.step})"


def frange(start: float, stop: float = None, step: float = None) -> FRangeIterator:
    """Returns an FRangeIterator 

    Args:
        start (float): If stop is set then the starting value else the stop value
        stop (float, optional): The stopping value if set else defaults the start value to 0.
        step (float, optional): The step (increment). Defaults to 1.

    Returns:
        FRangeIterator: The created iterator
    """
    return FRangeIterator(stop or start, (start if stop else 0), step or 1)
