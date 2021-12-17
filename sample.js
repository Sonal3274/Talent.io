var squares;
//Trying to get value from local storage 
//if not creating new array and assigning it to local storage.
if (localStorage.getItem('squares') !== null) {
    squares = JSON.parse(localStorage.getItem('squares'));
} else {
    squares = new Array(10);
    localStorage.setItem("squares", JSON.stringify(squares));
}

//Function to insert color in the array.
function insertColorToArray(color) {
    squares.pop();
    squares.unshift(color);
    localStorage.setItem("squares", JSON.stringify(squares));
    refreshColors();
}

//Function to refresh colors.
function refreshColors() {
    for (let index = 0; index < squares.length; index++) {
        if (squares[index] !== undefined && squares[index] !== null) {
            var current = 'sq' + (index + 1) + '';
            document.getElementById(current).style.backgroundColor = squares[index];
        }
    }
}

function addColor(color) {
    insertColorToArray(color);
}