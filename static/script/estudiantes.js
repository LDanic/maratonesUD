const stuForm = document.querySelector('#studentForm')

//Crear un estudiante
stuForm.addEventListener('submit', async e => {
    e.preventDefault()

    const nombre = stuForm['nombre'].value
    const apellido = stuForm['apellido'].value
    const codigo = stuForm['codigo'].value
    const carrera = stuForm['carrera'].value
    const materia = stuForm['materia'].value
    const equipo = stuForm['equipo'].value

    const response = await fetch('/api/estudiantes', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            nom_est: nombre,
            ape_est: apellido,
            codigo_est: codigo,
            carrera: carrera,
            materia_programacion: materia,
            id_equipo: equipo
        })
    })

    const data = await response.json()
    if(!response.ok){
        alert('team is full')
    }
    console.log(response)
    stuForm.reset()
})

var input_materia = document.getElementById('inputMateria');
var input_equipo = document.getElementById('inputEquipo');

input_materia.addEventListener('change', async function () {
    var data = []

    if (this.value == 'Programación básica') {
        const response = await fetch("/api/equipos/1");
        data = await response.json();
    } else if (this.value == 'POO') {
        const response = await fetch("/api/equipos/2");
        data = await response.json();
    } else if (this.value == 'Programación avanzada') {
        const response = await fetch("/api/equipos/3");
        data = await response.json();
    } else {
        const response = await fetch("/api/equipos/4");
        data = await response.json();
    }

    while (input_equipo.options.length > 0) {
        input_equipo.options.remove(0);
    }


    Array.from(data).forEach(function (eq) {
        let option = new Option(eq.nom_equipo, eq.id_equipo);

        input_equipo.appendChild(option);
    })
})