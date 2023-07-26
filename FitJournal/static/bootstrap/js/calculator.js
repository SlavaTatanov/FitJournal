function calculate1RM (weight, reps) {
  /**
   * Функция выполняет расчет одноповторного максимума,
   * расчет выполняется по формуле Эпли и округляется до одного знака после запятой
   */
  let res = weight * (1 + reps / 30);
  return res.toFixed(1);
}

console.log(calculate1RM(70, 4))