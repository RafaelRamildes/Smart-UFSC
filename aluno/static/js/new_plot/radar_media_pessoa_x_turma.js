new Chart(document.getElementById("radar_media_pessoa_x_turma"), {
    type: 'radar',
    data: {
      labels: ["DAS5334", "DAS5411", "EGR5606", "FSC5101", "MTM3101", "MTM5512"],
      datasets: [
        {
          label: "Suas Médias",
          fill: true,
          backgroundColor: "rgba(62, 149, 205, 0.2)",
          borderColor: "rgba(62, 149, 205, 1)",
          pointBorderColor: "#fff",
          pointBackgroundColor: "rgba(62, 149, 205, 1)",
          data: [8.77,10,8.22,6.62,6.82,10]
        }, {
          label: "Média da Turma",
          fill: true,
          backgroundColor: "rgba(142, 94, 162, 0.2)",
          borderColor: "rgba(142, 94, 162, 1)",
          pointBorderColor: "#fff",
          pointBackgroundColor: "rgba(142, 94, 162, 1)",
          pointBorderColor: "#fff",
          data: [5.77,7,6.3,4.62,4.2,5]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Média das Notas do Usuário e da Turma'
      }
    }
  });