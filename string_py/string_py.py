from datetime import datetime
from time import sleep
from asyncio import sleep as aio_sleep
from random import choices, randint
import string


class Color:
    """Color variations for prints"""
    bold = "\u001b[1m",
    underline = "\u001b[4m",
    reset = "\u001b[0m",
    force = "\u001b[0m",
    error = "\u001b[31m",
    basic = "\u001b[37m"


class Printer:
    """Adds new print methods to work with.

    Parameters
    ----------
    :param active:`True`
        If set to False, no more prints are executed. Exception: force Parameter is set to True.
    """

    def __init__(self, active: bool = True):
        self.active = active

    def time(self, args: str, dt: bool = True, force: bool = False, error: bool = False) -> None:
        """ Timestamp print: Print with the current day and time.

        Parameters
        ----------
        :param args:`str`
            The text to print.
        :param dt:`True`
            Set to `False` to turn off timestamp.
        :param force:`False`
            Set to `True` to print always, even if :class:`active` is set to False.
        :param error:`False`
            Set to `True` to print always, even if :class:`active` is set to False, gets highlighted with red color.
        """
        if self.active or force or error:
            color = Color.error if error else Color.force if force else Color.basic
            if dt:
                print(f"[{datetime.now().strftime('%d.%m | %H:%M:%S')}] {color}{args}\u001b[0m")
            else:
                print(f"{color}{args}\u001b[0m")

    def slow(self, args: str, speed: float = 0.2, force: bool = False, error: bool = False) -> None:
        """Slow print: Char after char gets printed in a certain speed

        Parameters
        ----------
        :param args:`str`
            The text to print.
        :param speed:`0.1`
            The speed in wich the chars will get printed out
        :param force:`False`
            Set to `True` to print always, even if :class:`active` is set to False.
        :param error:`False`
            Set to `True` to print always, even if :class:`active` is set to False, gets highlighted with red color.
        """
        if self.active or force or error:
            color = Color.error if error else Color.force if force else Color.basic
            for char in args:
                print(color + char, end="")
                sleep(speed)

    async def aio_slow(self, args: str, speed: float = 0.1, force: bool = False, error: bool = False) -> None:
        """Async slow print: Char after char gets printed in a certain speed

        Parameters
        ----------
        :param args:`str`
            The text to print.
        :param speed:`0.1`
            The speed in wich the chars will get printed out
        :param force:`False`
            Set to `True` to print always, even if :class:`active` is set to False.
        :param error:`False`
            Set to `True` to print always, even if :class:`active` is set to False, gets highlighted with red color.
        """
        if self.active or force or error:
            color = Color.error if error else Color.force if force else Color.basic
            for char in args:
                print(color + char, end="")
                await aio_sleep(speed)


class Str(str):
    """Functions to work with strings

    Parameters
    ----------
    :param values: `str`
        The value you want to work with
    """

    def __init__(self, values: str):
        self.values = values
        self.chars = [*values]
        self.ascii = {
            "ascii_lowercase": string.ascii_lowercase,
            "ascii_uppercase": string.ascii_uppercase,
            "digits": string.digits,
            "punctuation": string.punctuation
        }

    def generate(self, length: int = None, min_: int = None, max_: int = None) -> str:
        """Generate a random string out of :class:`values`
        :param length:
            Generate with certain length
        :param min_:
            Generate with random length, `max_` required
        :param max_:
            Generate with random length, `min_` required
        :return:
            Returns random string out of :class:`values` with length out of parameters
        """
        if (min_ is None and max_ is None) and length is None:
            raise AttributeError("min_ and max_ or length must have a value")
        elif length:
            return "".join(choices(self.chars, k=length))
        elif min_ is not None and max_ is not None:
            if min_ > max_:
                raise AttributeError("min_ must have a smaller value then max_")
            return "".join(choices(self.chars, k=randint(min_, max_)))
        else:
            raise AttributeError("min_ and max_ or length must have a value")

    def remove(self, chars: str) -> str:
        """Remove chars from string

        Parameters:
        -----------
        :param chars:
            The chars you want to remove
        """
        return self.values.replace(chars, "")

    def split(self, each: int = None, chars: str = None) -> list[str]:
        """An extension of the built-in .split method. Also split on certain index

        Parameters
        ----------
        :param each:
            The index you want to split at
        :param chars:
            The char or word you want to split at
        :return:
            Returns list with splittet :class:`values`
        """
        if not each and not chars:
            raise AttributeError("each or chars must have a value")
        if each:
            return [self.values[i:i + each] for i in range(0, len(self.values), each)]
        else:
            return self.values.split(chars)

    def first(self, length: int = 1, remove=False) -> str:
        """A simplification for getting/removing the first chars in a string

        Parameters:
        -----------
        :param length:
            The amount of chars
        :param remove:
            If set to `True` removes `length` of :class:`values`
        """
        if len(self.values) < length:
            raise AttributeError("Length must be smaller then value")
        if remove:
            return self.values[length:]
        else:
            return self.values[:length]

    def last(self, length: int = 1, remove=False) -> str:
        """A simplification for getting/removing the last chars in a string

        Parameters:
        -----------
        :param length:
            The amount of chars
        :param remove:
            If set to `True` removes `length` of :class:`values`
        """
        if len(self.values) < length:
            raise AttributeError("Length must be smaller then value")
        if remove:
            return self.values[:-length]
        else:
            return self.values[-length:]

    def __get(self, type_: str, index: bool) -> list[str] | dict[int, str]:

        gets = [] if index is False else {}
        for num, char in enumerate(self.values):
            if char in self.ascii[type_]:
                if index is False:
                    gets.append(char)
                else:
                    gets[num] = char
        return gets

    def get_upper(self, chars: bool = True, index: bool = False) -> int | list[str] | dict[int, str]:
        """Get how many upper chars are in :class:`values`

        Parameters
        ----------
        :param chars:`True`
            If set to True, returns a list of all uppercase chars
            If set to False, returns the number of uppercase chars
        :param index:`False`
            If set to True, also returns the Indexes of lower chars (`chars` MUST be `True`)
        """
        upper = self.__get("ascii_uppercase", index)
        return upper if chars else len(upper)

    def get_lower(self, chars: bool = True, index: bool = False) -> int | list[str] | dict[int, str]:
        """Get how many lower chars are in :class:`values`

        Parameters
        ----------
        :param chars:`True`
            If set to True, returns a list of all lower chars
            If set to False, returns the number of lower chars
        :param index:`False`
            If set to True, also returns the Indexes of lower chars (`chars` MUST be `True`)
        """
        if not chars and index:
            raise AttributeError("If index is set to True, chars can't be False")

        lower = self.__get("ascii_lowercase", index)
        return lower if chars else len(lower)

    def get_numeric(self, chars: bool = True, index: bool = False) -> int | list[str] | dict[int, str]:
        """Get how many numeric chars are in :class:`values`

        Parameters
        ----------
        :param chars:`True`
            If set to True, returns a list of all numeric chars
            If set to False, returns the number of numeric chars
        :param index:`False`
            If set to True, also returns the Indexes of numeric chars (`chars` MUST be `True`)
        """
        if not chars and index:
            raise AttributeError("If index is set to True, chars can't be False")

        numeric = self.__get("digits", index)
        return numeric if chars else len(numeric)

    def get_punctuation(self, chars: bool = True, index: bool = False) -> int | list[str] | dict[int, str]:
        """Get how many punctuation chars are in :class:`values`

        Parameters
        ----------
        :param chars:`True`
            If set to True, returns a list of all punctuation chars
            If set to False, returns the number of punctuation chars
        :param index:`False`
            If set to True, also returns the Indexes of punctuation chars (`chars` MUST be `True`)
        """
        if not chars and index:
            raise AttributeError("If index is set to True, chars can't be False")

        punctuation = self.__get("punctuation", index)
        return punctuation if chars else len(punctuation)


class Format:
    """Format texts"""

    @staticmethod
    def surround(values: str, char: str = "*") -> str:
        """Surround a text with chars

        Parameters
        ----------
        :param values:`str`
            Text to surround
        :param char:`*`
            Char to surround with
        :return:
            Returns a string with the text surrounded with certain chars
        """
        return f"{char * (len(values) + 4)}\n{char} {values} {char}\n{char * (len(values) + 4)}"

    @staticmethod
    def align(values: dict[str, str]):
        """Align a text

        Parameters
        ----------
        :param values:`dict[str, str]`
            Texts to align {"Left side": "Right side"}
        :return:
            Returns a string with the key aligned left and the value right dependent from the keys

        Examples
        --------
        values = {"Username:": "John", "Register Date:": "01.01.2001"}
        Username:        John
        Register Date:   01.01.2001
        """
        length = max([len(x) for x in list(values.keys())])
        aligned_text = ""
        for key in values:
            aligned_text += key + " " * ((length + 3) - len(key)) + values[key] + "\n"
        return aligned_text

    @staticmethod
    def table(values: list[list[str]], border: bool = True) -> str:
        """Create a table

        Parameters
        ----------
        :param values:`list[list[str]]`
            The values you want to print
        :param border:`True`
            Set to `False` to remove the border
        :return:
            Returns the table as string
        """

        length = [max([len(str(x)) for x in column]) for column in zip(*values)]
        if border:
            table = "\u250C" + "\u2500" * (sum(length) + (3 * len(values) - 1)) + "\u2510\n"
            for index, row in enumerate(values):
                table += "\u2502"
                for i, column in enumerate(row):
                    table += " " + column + " " * (length[i] - len(column)) + " \u2502"
                if index == 0:
                    table += "\n\u251C" + "\u2500" * (sum(length) + (3 * len(values) - 1)) + "\u2524" + "\n"
                else:
                    if index != len(values) - 1:
                        table += "\n\u2502" + "\u2500" * (sum(length) + (3 * len(values) - 1)) + "\u2502" + "\n"
                    else:
                        table += "\n\u2514" + "\u2500" * (sum(length) + (3 * len(values) - 1)) + "\u2518"
        else:
            table = ""
            for index, row in enumerate(values):
                for i, column in enumerate(row):
                    table += " " + column + " " * (length[i] - len(column)) + " "
                if index != len(values) - 1:
                    table += "\n"
        return table
