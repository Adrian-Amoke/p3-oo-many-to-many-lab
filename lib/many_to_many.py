class Book:
    _all = []

    def __init__(self, title):
        self.title = title
        self.__class__._all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value

    def contracts(self):
        return [contract for contract in Contract.all() if contract.book == self]

    def authors(self):
        return list({contract.author for contract in self.contracts()})

    @classmethod
    def all(cls):
        return cls._all


class Author:
    _all = []

    def __init__(self, name):
        self.name = name
        self.__class__._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value

    def contracts(self):
        return [contract for contract in Contract.all() if contract.author == self]

    def books(self):
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    @classmethod
    def all(cls):
        return cls._all


class Contract:
    _all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__._all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        self._royalties = value

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def contracts_by_date(cls, date):
        from datetime import datetime

        # Parse the input date string
        input_date = datetime.strptime(date, "%m/%d/%Y")

        # Filter contracts by matching date
        filtered_contracts = [contract for contract in cls._all if datetime.strptime(contract.date, "%m/%d/%Y") == input_date]

        # Sort contracts by date, then author name, then book title for consistent ordering
        sorted_contracts = sorted(
            filtered_contracts,
            key=lambda c: (datetime.strptime(c.date, "%m/%d/%Y"), c.author.name, c.book.title)
        )
        return sorted_contracts
