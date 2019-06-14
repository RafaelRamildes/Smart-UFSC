// aluno_todas_notas.js 
//Mostra as notas do Aluno em todas as disciplinas

new Chart(document.getElementById("frequencia"), {
    type: 'doughnut',
    data: {
      labels: ["Presenças", "Faltas", "Restante"],
      datasets: [
        {
          label: "Aulas",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f"],
          data: [20,30,10]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Frequência do Aluno'
      }
    }
});