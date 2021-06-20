
let past_ans = []
window.onload = function(){ // WHen the window loads, run the ajax function trying to get the past asnwers
    $.ajax({
        url: '/test',
        type: 'GET',
        success: function(response){//If it gets a json response from flask, sends the dict to the grid.
            dict_to_grid(response);
        },
        error: function(error){//Arbitrary error.
            console.log(error);
        }
    });
};

function dict_to_grid(arr){
    let container = document.getElementById("answer_container");
    if(arr.length > 0){
        let grid = document.createElement('table')
        for(let i =0; i < arr.length;i++){
            let tr = document.createElement("tr");
            for(let j = 0; j < arr[i].length; j++){
                let cell = document.createElement("td");
                cell.innerText = arr[i][j];
                tr.appendChild(cell);
            }
            grid.appendChild(tr);
        }
        container.appendChild(grid);
    }
}