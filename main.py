# Завдання 1

from queue import LifoQueue

# Створіть клас Project
# Атрибути:
#  tasks – стек з завданнями, об’єкти класу Task (початкове завдання передається в init)

class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []

    def do(self):
        """
        Виконує завдання, за потреби розбиває його на підзавдання
        :return: список підзавдань
        """
        if self.subtasks:
            print(f"Виконую завдання: {self.name}. Розбиваю на підзавдання")
        else:
            print(f"Завершено завдання: {self.name}")

        return self.subtasks


class Project:
    def __init__(self, initial_task: Task):
        self.initial_task = initial_task
        self.tasks = LifoQueue()
        self.tasks.put(self.initial_task)

    def is_finished(self):
        return self.tasks.empty()

    def do_task(self):
        if not self.is_finished():
            current_task = self.tasks.get()
            subtasks = current_task.do()
            for sub in subtasks:
                self.tasks.put(sub)


task = Task('Підготовка до зйомок')

task.subtasks = [
    Task('Пошук локацій'),
    Task('Підготовка сценарію'),
    Task('Кастинг акторів')
]

# Підзавдання для "Пошук локацій"
task.subtasks[0].subtasks = [
    Task('Огляд локацій у місті'),
    Task('Огляд локацій за містом'),
    Task('Узгодження місць для зйомок')
]

# Підзавдання для "Підготовка сценарію"
task.subtasks[1].subtasks = [
    Task('Написання основного сценарію'),
    Task('Редагування сценарію'),
    Task('Підготовка сценарних приміток'),
]

# Підзавдання для "Кастинг акторів"
task.subtasks[2].subtasks = [
    Task('Пошук головних акторів'),
    Task('Пошук другорядних акторів'),
    Task('Підготовка контрактів для акторів')
]

# Підзавдання для "Пошук локацій у місті"
task.subtasks[0].subtasks[0].subtasks = [
    Task('Вибір декорацій для зйомок'),
    Task('Узгодження з власниками приміщень')
]

# Підзавдання для "Огляд локацій за містом"
task.subtasks[0].subtasks[1].subtasks = [
    Task('Вибір лісу для сцени битви'),
    Task('Пошук старовинних будівель для сцени'),
]

# Підзавдання для "Написання основного сценарію"
task.subtasks[1].subtasks[0].subtasks = [
    Task('Написання першої частини'),
    Task('Написання другої частини'),
]

# Підзавдання для "Пошук головних акторів"
task.subtasks[2].subtasks[0].subtasks = [
    Task('Пошук актора на роль головного героя'),
    Task('Пошук актриси на роль головної героїні')
]

project = Project(task)
while not project.is_finished():
    project.do_task()