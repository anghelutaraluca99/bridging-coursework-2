var editable = document.getElementById('Surname');
editable.addEventListener('input', function() {
    console.log('Hey, idk');
});

function submitChanges(){
    const surname = document.getElementById("Surname");
    console.log(surname.textContent);
}
