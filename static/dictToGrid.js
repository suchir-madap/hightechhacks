window.onload = function dict_to_grid(){
    let answers = document.getElementById("pastans").innerText
    answers = answers.replace("[", "")
    
    answers = answers.split(",")
    console.log(answers)
    if(answers.length > 0){
        let grid = document.createElement('table')
        for(let i =0; i < answers.length / 2;i++){
            let tr = document.createElement("tr");
            for(let j = 0; j < 2; j++){
                let cell = document.createElement("td");
                cell.innerText = answers[i + j];
                tr.appendChild(cell);
            }
            grid.appendChild(tr)
        }
        document.getElementById("pastans").innerText.remove()
        body.appendChild(grid);
    }
}