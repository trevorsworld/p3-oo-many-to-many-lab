class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    def __repr__(self):
        return f"Book(title={self.title})"


class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.contracts = []
        Author.all_authors.append(self)

    def __repr__(self):
        return f"Author(name={self.name})"

    def contracts(self):
        return self.contracts

    def books(self):
        return [contract.book for contract in self.contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("instance of Book class")
        if not isinstance(date, str):
            raise Exception("string")
        if not isinstance(royalties, int):
            raise Exception("integer")
        contract = Contract(self, book, date, royalties)
        self.contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts)


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("instance of Author class")
        if not isinstance(book, Book):
            raise Exception("class")
        if not isinstance(date, str):
            raise Exception("string")
        if not isinstance(royalties, int):
            raise Exception("integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    def __repr__(self):
        return f"Contract(author={self.author.name}, book={self.book.title}, date={self.date}, royalties={self.royalties})"

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("string")
        return [contract for contract in cls.all_contracts if contract.date == date]