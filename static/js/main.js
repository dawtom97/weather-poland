

const element = document.getElementById("Btn")

function changeColor () {
    document.body.style.background = "green"
}

element.addEventListener("click",() => changeColor() )