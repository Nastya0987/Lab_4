import datetime

class Date:
    """
    Клас для роботи з датами. Дозволяє створювати, порівнювати, додавати, віднімати дати,
    а також отримувати інформацію про високосний рік, назву місяця та дня тижня.

    Атрибути:
        _day (int): День місяця.
        _month (int): Місяць.
        _year (int): Рік.
    """

    def __init__(self, day: int, month: int, year: int):
        """
        Ініціалізує об'єкт класу Date з перевіркою коректності даних.

        Args:
            day (int): День місяця.
            month (int): Місяць.
            year (int): Рік.

        Raises:
            TypeError: Якщо параметри не є цілими числами.
            ValueError: Якщо день, місяць або рік некоректні.
        """
        if not all(isinstance(x, int) for x in (day, month, year)):
            raise TypeError("День, місяць і рік повинні бути цілими числами.")
        if year <= 0:
            raise ValueError("Рік повинен бути додатнім.")
        if month < 1 or month > 12:
            raise ValueError("Місяць повинен бути в діапазоні 1-12.")
        if day < 1:
            raise ValueError("День повинен бути додатнім.")

        # Визначаємо максимальний день у місяці з урахуванням високосного року
        if month == 2:
            max_day = 29 if self._is_leap_year(year) else 28
        elif month in [4, 6, 9, 11]:
            max_day = 30
        else:
            max_day = 31

        if day > max_day:
            raise ValueError(f"У {month}-му місяці не може бути {day} днів.")

        self._day = day
        self._month = month
        self._year = year

    def __str__(self):
        """
        Повертає рядкове представлення дати у форматі "дд.мм.рррр".

        Returns:
            str: Дата у форматі "дд.мм.рррр".
        """
        return f"{self._day:02d}.{self._month:02d}.{self._year}"

    def __eq__(self, other):
        """
        Перевіряє, чи дві дати рівні.

        Args:
            other (Date): Інша дата.

        Returns:
            bool: True, якщо дати рівні, інакше False.
        """
        if not isinstance(other, Date):
            return NotImplemented
        return (self._day, self._month, self._year) == (other._day, other._month, other._year)

    def __lt__(self, other):
        """
        Перевіряє, чи ця дата раніше за іншу.

        Args:
            other (Date): Інша дата.

        Returns:
            bool: True, якщо ця дата раніше, інакше False.
        """
        if not isinstance(other, Date):
            return NotImplemented
        return (self._year, self._month, self._day) < (other._year, other._month, other._day)

    def __gt__(self, other):
        """
        Перевіряє, чи ця дата пізніше за іншу.

        Args:
            other (Date): Інша дата.

        Returns:
            bool: True, якщо ця дата пізніше, інакше False.
        """
        if not isinstance(other, Date):
            return NotImplemented
        return (self._year, self._month, self._day) > (other._year, other._month, other._day)

    def __sub__(self, other):
        """
        Віднімає одну дату від іншої та повертає різницю у днях.

        Args:
            other (Date): Інша дата.

        Returns:
            int: Різниця у днях між датами.
        """
        if not isinstance(other, Date):
            return NotImplemented
        d1 = datetime.date(self._year, self._month, self._day)
        d2 = datetime.date(other._year, other._month, other._day)
        return (d1 - d2).days

    def __add__(self, days):
        """
        Додає до дати певну кількість днів.

        Args:
            days (int): Кількість днів для додавання.

        Returns:
            Date: Нова дата після додавання.
        """
        if not isinstance(days, int):
            return NotImplemented
        d = datetime.date(self._year, self._month, self._day) + datetime.timedelta(days=days)
        return Date(d.day, d.month, d.year)

    def is_leap_year(self):
        """
        Перевіряє, чи рік дати є високосним.

        Returns:
            bool: True, якщо рік високосний, інакше False.
        """
        return self._is_leap_year(self._year)

    @staticmethod
    def _is_leap_year(year):
        """
        Статичний метод для перевірки високосного року.

        Args:
            year (int): Рік.

        Returns:
            bool: True, якщо рік високосний, інакше False.
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def month_name(self):
        """
        Повертає назву місяця українською.

        Returns:
            str: Назва місяця.
        """
        months = [
            "січня", "лютого", "березня", "квітня", "травня", "червня",
            "липня", "серпня", "вересня", "жовтня", "листопада", "грудня"
        ]
        return f"{self._day} {months[self._month - 1]} {self._year} рік"

    def day_of_week(self):
        """
        Визначає день тижня для дати.

        Returns:
            str: Назва дня тижня українською.
        """
        days = [
            "Понеділок", "Вівторок", "Середа",
            "Четвер", "П’ятниця", "Субота", "Неділя"
        ]
        d = datetime.date(self._year, self._month, self._day)
        return days[d.weekday()]


if __name__ == "__main__":
    print("Демонстрація роботи класу Date:")
    # Коректні дати
    try:
        d1 = Date(16, 4, 2025)
        d2 = Date(29, 2, 2024)  # високосний рік
        d3 = Date(1, 1, 2025)
        print("d1:", d1)
        print("d2:", d2)
        print("d3:", d3)

        # Перевантажені оператори
        print("d1 == d3:", d1 == d3)
        print("d2 > d1:", d2 > d1)
        print("d3 < d1:", d3 < d1)
        print("d1 - d3 (різниця у днях):", d1 - d3)
        print("d3 + 10 днів:", d3 + 10)

        # Власні методи
        print("d2.is_leap_year():", d2.is_leap_year())
        print("d1.month_name():", d1.month_name())
        print("d2.day_of_week():", d2.day_of_week())

        # Некоректна дата (29 лютого у невисокосному році)
        try:
            d_bad = Date(29, 2, 2025)
        except ValueError as e:
            print("Помилка створення дати:", e)

        # Некоректний тип
        try:
            d_bad2 = Date("15", 2, 2025)
        except TypeError as e:
            print("Помилка типу:", e)

        # Некоректний місяць
        try:
            d_bad3 = Date(10, 13, 2025)
        except ValueError as e:
            print("Помилка місяця:", e)

    except Exception as e:
        print("Невідома помилка:", e)
