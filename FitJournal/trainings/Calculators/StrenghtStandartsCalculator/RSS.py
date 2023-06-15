from trainings.Calculators import Base
from trainings.CONSTANCES import EXERCISE

REGISTER_CALCULATORS = {
    EXERCISE.SQUAT: "Функция для приседаний",
    EXERCISE.DEADLIFT: "Функция для становой тяги",
    EXERCISE.BENCH_PRESS: "Функция для жима лежа"
}


class RSSExerciseDispatcher(Base.Dispatcher):
    """
    Диспетчер упражнений для RSS стандарта
    """

    def __init__(self, exercise):
        self.exercise = exercise

    def get(self):
        """
        Возвращаем калькулятор
        """
        return REGISTER_CALCULATORS[self.exercise]
