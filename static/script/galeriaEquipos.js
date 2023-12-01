let teams = []
let infoMiembro = ''
let eqEliminar = 0

window.addEventListener("DOMContentLoaded", async () => {
    const nivel = localStorage.getItem('nivel')
    if (nivel == 1) {
        const response = await fetch("/api/equipos/1");
        const data = await response.json()
        teams = data
    } else if (nivel == 2) {
        const response = await fetch("/api/equipos/2");
        const data = await response.json()
        teams = data
    }
    else if (nivel == 3) {
        const response = await fetch("/api/equipos/3");
        const data = await response.json()
        teams = data
    }
    else if (nivel == 4) {
        const response = await fetch("/api/equipos/4");
        const data = await response.json()
        teams = data
    }
    renderEq(teams)
});

async function traerMiembros(id) {
    const res = await fetch("/api/equipos/miembros/" + id);
    const data = await res.json()

    let info = '-'
    data.forEach(member => {
        info += member.codigo_est + "-" + member.nom_est + " " + member.ape_est + "<br>-"
    })

    if(info=='-'){
        info = '-<br>-<br>-<br>'
    }

    infoMiembro = info
}


function renderEq(equipos) {
    const galeria = document.querySelector('#galeria')

    equipos.forEach(team => {

        return traerMiembros(team.id_equipo).then(() => {
            const item = document.createElement('div')
            item.classList = 'col'
            item.innerHTML = `
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <h5>${team.nom_equipo}</h5>
                        <p>${infoMiembro}</p>
                    </div>

                    <div class="boton-modal mb-2">
                        <button type="button" id="boton-m" class="btn_delte btn btn-dark" data-toggle="modal" data-target="#exampleModal">
                            Eliminar equipo
                        </button>
                    </div>
                </div>
            </div>
            `;

            const btdDelete = item.querySelector('.btn_delte')

            btdDelete.addEventListener('click', ()=>{
                eqEliminar =team.id_equipo
            })

            galeria.append(item)

        })
    });
}


async function eliminarEquipo(){
    console.log(eqEliminar)
    const res = await fetch("/api/equipos/" + eqEliminar,{
        method: 'DELETE'
    });
    const data = await res.json()
    console.log(data)
}