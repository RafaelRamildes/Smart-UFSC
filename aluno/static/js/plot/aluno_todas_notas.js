// aluno_todas_notas.js 
//Mostra as notas do Aluno em todas as disciplinas

new Chart(document.getElementById("aluno_todas_notas.js"), {
    type: 'bar',
    data: {
      labels: ["P1", "P2", "P3"],
      datasets: [
        {
          label: "MTM3101",
          backgroundColor: "#1b9e77",
          data: [10,8,9,0]
        }, 
                
        {
          label: "MTM5512",
          backgroundColor: "#7570b3",
          data: [7,3,4]
        }, 
        
        {
          label: "DAS5334",
          backgroundColor: "#e7298a",
          data: [2,4,5]
        }, 
        
        {
          label: "DAS5411",
          backgroundColor: "#66a61e",
          data: [7,3,1]
        }, 
        
        {
          label: "EGR5606",
          backgroundColor: "#e6ab02",
          data: [9,10,10]
        }, 
        
        {
          label: "FSC5101",
          backgroundColor: "#a6761d",
          data: [0,3,4]
        }, 
        
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Notas em Todas as Avaliações'
      }
    }
});