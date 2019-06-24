new Chart(document.getElementById("barras_4_provas_e_turma"), {
    type: 'bar',
    data: {
      labels: ["Data P1", "Data P2", "Data P3", "Data P4"],
      datasets: [
        {
          label: "Você",
          backgroundColor: "#3e95cd",
          data: [66,65,64,63, 0, 100]
        }, {
          label: "Sua Turma",
          backgroundColor: "#8e5ea2",
          data: [56,55,54,53, 0, 100]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Provas da Matéria X'
      }
    }
});