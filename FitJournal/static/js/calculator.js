function calculate1RM (weight, reps) {
  /**
   * Функция выполняет расчет одноповторного максимума,
   * расчет выполняется по формуле Эпли и округляется до одного знака после запятой
   */
  let res = weight * (1 + reps / 30);
  return res.toFixed(1);
}

function get1RM() {
  /**
   * Функиця забирает значения из input полей, делает расчет и заполняет таблицу
   */

  // Берем значения из input
  let weight = document.getElementById("weight").value;
  let reps = document.getElementById("reps").value;

  // Выполняем расчет
  let res = calculate1RM(Number(weight), Number(reps));

  // Заполняем таблицу
  let rm100 = document.getElementById("rm100");
  rm100.innerHTML = res;

  // Проходимся циклом по остальным элементам таблицы
  let td_id = ["rm95", "rm90", "rm85", "rm80", 
  "rm75", "rm70", "rm65", "rm60", "rm50"];
  for(i=0; i<td_id.length; i++) {
    let coeff = td_id[i].replace("rm", "0.");
    coeff = Number(coeff);
    let rm = document.getElementById(td_id[i]);
    rm.innerHTML = (Number(res) * coeff).toFixed(1);
  }
}