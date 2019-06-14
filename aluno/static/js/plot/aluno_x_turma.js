// aluno_x_turma.js 
//Mostra as notas do Aluno em uma disciplina

new Chart(document.getElementById("aluno_x_turma"), {
    type: 'bar',
    data: {
      labels: ["P1", "P2", "P3"],
      datasets: [
        {
          label: "Aluno",
          backgroundColor: "#3e95cd",
          data: [10,7,8,0]
        }, {
          label: "Média da Turma",
          backgroundColor: "#8e5ea2",
          data: [7,5,6,0]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: '[NOME DA MATÉRIA]'
      }
    }
});