function basicos(){
    localStorage.setItem('nivel', 1)
    window.location.href = 'Galeria.html'
}

function intermedios(){
    localStorage.setItem('nivel', 2)
    window.location.href = 'Galeria.html'
}

function avanzados(){
    localStorage.setItem('nivel', 3)
    window.location.href = 'Galeria.html'
}

function elite(){
    localStorage.setItem('nivel', 4)
    window.location.href = 'Galeria.html'
}


async function eliminarTodo(){
    const res = await fetch("/api/equipos/deleteAll",{
        method: 'DELETE'
    });
    const data = await res.json()
}

