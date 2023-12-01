const teamForm = document.querySelector('#teamForm')

//Crear un equipo
teamForm.addEventListener('submit', async e => {
    e.preventDefault()

    const nom_equipo = teamForm['nombre'].value
    const id_competencia = teamForm['competencia'].value

    const response = await fetch('/api/equipos', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            nom_equipo,
            id_competencia
        })
    })

    const data = await response.json()
    console.log(data)
    teamForm.reset()
})