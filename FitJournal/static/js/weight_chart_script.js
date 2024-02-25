function dateConvert (date) {
    var resultList = [];
    for (i=0; i<date.length; i++) {
        resultList.push(new Date(date[i]))
    };
    return resultList
}

/**
 * Создает график веса. Первым параметром принимает даты, вторым вес.
 */
function createChart (weightDate, weight, label="Вес") {
    var ctx = document.getElementById('weight_chart');
    weightDate = dateConvert(weightDate);
    var myChart = new Chart(ctx, {
      type: 'line',
      data:{
        datasets: [{
          data: weight,
          label: label,
          borderColor: "#4682B4",
          backgroundColor: "#4682B4",
          tension: 0.3
        }],
        labels: weightDate
      },
      options: {
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: 'month'
                }
            }
        }
    }
    });
    return myChart;
}