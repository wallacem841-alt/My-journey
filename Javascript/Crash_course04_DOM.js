let heading = document.getElementById('myHeading');
heading.innerText = "New Heading Text";

document.getElementById("Change_heading").onclick = function(){
    heading.textContent = 'Hello, World!';
}

document.getElementById('collor_blue').onclick = function(){
    heading.style.color = '#1B888C';
}

document.getElementById('Alert').onclick = function(){
    alert('button was clicked');
}