let estudiantes = []
let eqEliminar = 0

window.addEventListener("DOMContentLoaded", async () => {
    const response = await fetch("/api/estudiantes");
    const data = await response.json()
    estudiantes = data
    renderEst(estudiantes)
});



function renderEst(estudiantes) {
    const galeria = document.querySelector('#galeria')

    estudiantes.forEach(estudiante => {
        const item = document.createElement('div')
        item.classList = 'col'
        item.innerHTML = `
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <h5>${estudiante.codigo_est}</h5>
                        <p>Nombre: ${estudiante.nom_est}</p>
                        <p>Apellido: ${estudiante.ape_est}</p>
                        <p>Carrera: ${estudiante.carrera}</p>
                        <p>Materia: ${estudiante.materia_programacion}</p>
                    </div>

                    <div class="boton-modal mb-2">
                        <button type="button" id="boton-m" class="btn_delte btn btn-dark" data-toggle="modal" data-target="#exampleModal">
                            Eliminar estudiante
                        </button>
                    </div>
                </div>
            </div>
            `;

        const btdDelete = item.querySelector('.btn_delte')

        btdDelete.addEventListener('click', () => {
            eqEliminar = estudiante.codigo_est
        })

        galeria.append(item)
    });
}


async function eliminarEquipo() {
    const res = await fetch("/api/estudiantes/" + eqEliminar, {
        method: 'DELETE'
    });
    const data = await res.json()
    console.log(data)
}