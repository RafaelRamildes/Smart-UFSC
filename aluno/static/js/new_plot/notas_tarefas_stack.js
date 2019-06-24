new Chart(document.getElementById("notas_tarefas_stack"), {

    type: 'horizontalBar',
    data: {
        labels: ["Tarefa 1", "Tarefa 2", "Tarefa 3", "Tarefa 4", "Tarefa 5", "Tarefa 6", "Tarefa 7"],
        datasets: [
          {
            label: "Suas notas",
            backgroundColor: "#3e95cd",
            data: [10,7,8,9,10,10,10,0]
          }, {
            label: "Média da turma",
            backgroundColor: "#8e5ea2",
            data: [10,5,6,5,7.5,5,7,0]
          }
        ]
      },
      options: {
        title: {
          display: true,
          text: 'Feedback em Tarefas'
        }
      }
  });