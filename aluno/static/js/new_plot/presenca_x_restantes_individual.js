new Chart(document.getElementById("presenca_x_restantes_individual"), {

  type: 'horizontalBar',
  data: {
    labels: ["DAS5334", "DAS5411", "EGR5606", "FSC5101", "MTM3101", "MTM5512"],
    datasets: [
      {
        label: 'Presenças',
        data: [40, 52, 50, 54, 56, 56, 58],
        backgroundColor: '#3cba9f',
      },
      {
        label: 'Restantes',
        data: [22, 22, 22, 22, 22, 22],
        backgroundColor: '#fee08b',
      },
      {
        label: 'Faltou',
        data: [18, 6, 8, 4, 2, 2, 0],
        backgroundColor: '#c45850',
      }
    ]
  },
  options: {
    title: {
        display: true,
        text: 'Presença em cada Matéria'
    },
      
    scales: {
      xAxes: [{ stacked: true }],
      yAxes: [{ stacked: true }]
    }
}
});