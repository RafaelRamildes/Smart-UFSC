new Chart(document.getElementById("progressao_semestre_x_curso"), {
    type: 'doughnut',
    data: {
      labels: ["Créditos do Semestre Atual", "Créditos Completos", "Créditos restantes no Curso"],
      datasets: [
        {
          label: "Créditos (horas)",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f"],
          data: [24,24,245]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Progressão de Créditos no Curso'
      }
    }
});