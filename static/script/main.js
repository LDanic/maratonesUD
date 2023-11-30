const studentForm = document.querySelector('#studentForm')

studentForm.addEventListener('submit', e=>{
    e.preventDefault()

    const nombre = studentForm['nombre'].value
    const apellido = studentForm['apellido'].value
    const codigo = studentForm['codigo'].value
    const carrera = studentForm['carrera'].value

    console.log(nombre, apellido, codigo, carrera)
})