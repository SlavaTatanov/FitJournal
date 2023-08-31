function calculate1RM (weight, reps) {
  /**
   * Функция выполняет расчет одноповторного максимума,
   * расчет выполняется по формуле Эпли и округляется до одного знака после запятой
   */
  let res = weight * (1 + reps / 30);
  return res.toFixed(1);
}

function get1RMCalc() {
  /**
   * Функиця забирает значения из input полей, делает расчет и заполняет таблицу
   */

  // Берем элементы inputs
  var weightEl = document.getElementById("weight");
  var repsEl = document.getElementById("reps");

  // Берем значения из input
  let weight = weightEl.value;
  let reps = repsEl.value;

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

function checkWeight() {
  /**
   * Проверяем поле веса
   */
  let el = document.getElementById("weight");
  let val = el.value;
  if (!isNaN(val) && val.length > 0) {
    return true;
  } else {
    elementAlert(el);
    document.getElementById("weightAlert").innerText = "Ошибка ввода";
    return false;
  }
}

function checkReps() {
  /**
   * Проверяем поле повторений
   */
  let el = document.getElementById("reps");
  let val = el.value;
  if (!isNaN(val) && val.length > 0) {
    return true;
  } else {
    elementAlert(el);
    document.getElementById("repsAlert").innerText = "Ошибка ввода";
    return false;
  }
}

function elementAlert(el) {
  /**
   * Окрашивает элемент в красный цвет
   */
  el.style.borderColor = "red";
  el.style.borderWidth = "2px";  
}

function resetInputAlertWeigth () {
  /**
   * Сбрасываем алерт поля при фокусе
   */
  let el = document.getElementById("weight");
  resetInputAlert(el);
  document.getElementById("weightAlert").innerText = "";
}

function resetInputAlertReps () {
  /**
   * Сбрасываем алерт поля при фокусе
   */
  let el = document.getElementById("reps");
  resetInputAlert(el);
  document.getElementById("repsAlert").innerText = "";
}

function resetInputAlert(el) {
  /**
   * Сбрасываем цвет к дефолтному
   */
  el.style.borderColor = "#dee2e6";
  el.style.borderWidth = "1px";
}

function get1RM() {
  /**
   * Расчет одноповторного максимума
   */
  let w = checkWeight();
  let r = checkReps();
  if (w && r) {
    get1RMCalc();
  }
}
