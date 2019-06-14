new Chart(document.getElementById("atual"), {
    type: 'bar',
    data: {
      labels: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"],
      datasets: [{
          label: "Nº de Faltas Possiveis",
          type: "line",
          borderColor: "#3e95cd",
          data: ["20", "19", "18", "17", "16", "15", "14", "13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
          fill: false
        },{
          label: "Nº de Alunos",
          type: "bar",
          backgroundColor: "rgba(0,0,0,0.2)",
          backgroundColorHover: "#3e95cd",
          data: [10, 15, 5, 6, 7, 8, 4, 3, 4, 6, 8, 5, 2, 1, 1, 2, 4, 5, 4, 4, 2, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0],
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Population growth (millions): Europe & Africa'
      },
      legend: { display: false }
    }
});