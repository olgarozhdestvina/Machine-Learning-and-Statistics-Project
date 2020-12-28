// Adapted from stack overflow posts.
function calculate() {
    speed = parseFloat(document.querySelector('input[name="speed"]').value,10)
    //console.log(speed)
    power(speed)
} 

host = window.location.origin
function power(speed) {
    console.log(typeof(speed));
    $.ajax({
        "url": host+"/calculate/",
        "method": "POST",
        "data": {"speed": speed},
        "success": function (result) {
            console.log(result);
            //addDentistToTable(result)
        },
        "error": function (xhr, status, error) {
            alert(error);
        }
    });
};