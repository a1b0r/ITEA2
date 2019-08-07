# Создайте класс ПЕРСОНА с абстрактными методами, позволяющими вывести на экран информацию о персоне,
# а также определить ее возраст (в текущем году).
# Создайте дочерние классы: АБИТУРИЕНТ (фамилия, дата рождения, факультет),
# СТУДЕНТ (фамилия, дата рождения, факультет, курс),
# ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
# со своими методами вывода информации на экран и определения возраста. Создайте список из n персон,
# выведите полную информацию из базы на экран, а также организуйте поиск персон,
# чей возраст попадает в заданный диапазон.


from abc import ABC, abstractmethod
from datetime import datetime


class Persona(ABC):
    _second_name = None
    _birthday = None
    _department = None

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def second_name(self):
        pass

    @abstractmethod
    def birthday(self):
        pass

    @abstractmethod
    def department(self):
        pass

    @abstractmethod
    def birthday(self):
        pass

    @abstractmethod
    def get_actual_age(self):
        pass

    @abstractmethod
    def show_all_information(self):
        pass

class Enrollee(Persona):

    def _calc_actual_age(birthday):
        return datetime.today().year - datetime.strptime(birthday, '%d.%m.%Y').year

    def __init__(self, second_name, birthday, department):
        self._second_name = second_name
        self._birthday = birthday
        self._department = department
        self._actual_age = Enrollee._calc_actual_age(self._birthday)

    @property
    def second_name(self):
        return self._second_name

    @second_name.setter
    def second_name(self, second_name):
        self._second_name = second_name

    @second_name.deleter
    def second_name(self):
        del self._second_name

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        self._birthday = birthday

    @birthday.deleter
    def birthday(self):
        del self._birthday

    def get_actual_age(self):
        return self._actual_age

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department

    @department.deleter
    def department(self):
        del self._department

    def show_all_information(self):
        print('''second name     is {}
birthday        is {}
department      is {}
age             is {}'''.format(self.second_name, self.birthday, self.department, self.get_actual_age()))
        if type(self) == Enrollee:
            print('=' * 20)


class Student(Enrollee):
    _course = None

    def __init__(self, second_name, birthday, department, course):
        super().__init__(second_name, birthday, department)
        self._course = course

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        self._course = course

    @course.deleter
    def course(self):
        del self._course

    def show_all_information(self):
        super().show_all_information()
        print('course          is {}'.format(self.course))
        print('=' * 20)


class Teacher(Enrollee):
    _position = None
    _work_experience = None

    def __init__(self, second_name, birthday, department, position, work_experience):
        super().__init__(second_name, birthday, department)
        self._position = position
        self._work_experience = work_experience

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @position.deleter
    def position(self):
        del self._position

    @property
    def work_experience(self):
        return self._work_experience

    @work_experience.setter
    def work_experience(self, work_experience):
        self._work_experience = work_experience

    @work_experience.deleter
    def work_experience(self):
        del self._work_experience

    def show_all_information(self):
        super().show_all_information()
        print('''position        is {}
work experience is {}'''.format(self.position, self.work_experience))
        print('=' * 20)


personas = []
personas.append(Enrollee('Peregrin', '12.06.2001', 'D1'))
personas.append(Enrollee('Samwise', '23.08.2001', 'D2'))
personas.append(Enrollee('Bilbo', '09.05.2001', 'D3'))
personas.append(Enrollee('Frodo', '01.01.2001', 'D3'))

personas.append(Student('Aragorn', '06.12.1998', 'D1', 4))
personas.append(Student('Legolas', '08.02.1963', 'D2', 3))
personas.append(Student('Boromir', '03.07.1997', 'D2', 5))
personas.append(Student('Gimli', '28.02.1996', 'D3', 6))

personas.append(Teacher('Gandalf', '04.06.1963', 'D1', 'professor', 40))
personas.append(Teacher('Sauron', '24.06.1959', 'D2', 'evil', 44))
personas.append(Teacher('Elrond', '18.11.1955', 'D3', 'proffessor', 48))

for persona in personas:
    persona.show_all_information()


age_from = 20
age_to = 80

age_range = range(age_from, age_to)
print(f'Range is from {age_from} to {age_to}')
for persona in personas:
    if persona.get_actual_age() in age_range:
        print(f"{persona.second_name} in range with age {persona.get_actual_age()}")

