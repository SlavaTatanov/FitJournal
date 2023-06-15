from trainings.CONSTANCES import STRENGHT_STANDARTS
from trainings.Calculators.StrenghtStandartsCalculator.RSS import RSSExerciseDispatcher
from trainings.Calculators import Base


REGISTER_STANDARDS = {
    STRENGHT_STANDARTS.RSS: RSSExerciseDispatcher
}


class StandardDispatcher(Base.Dispatcher):
    """
    Класс, который принимает стандарт расчета, и упражнение и возвращает нужный калькулятор,
    если он есть
    """

    def __init__(self, standard: str, exercise: str):
        self._standard = standard
        self._exercise = exercise

    def get(self):
        return REGISTER_STANDARDS[self._standard](self._exercise).get()
