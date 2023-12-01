var materias={
    sistemas: ['Programación básica', 'POO', 'Programación avanzada', 'Modelos I', 'Modelos II'],
    otros: ['Programación básica', 'POO', 'Programación avanzada']
}

var carreras = document.getElementById('inputCarrera');
var input_materia = document.getElementById('inputMateria');

carreras.addEventListener('change', function(){
    if(this.value == 'Ing. de sistemas'){
        var opcion_selecionada = materias['sistemas'];
    }else{
        var opcion_selecionada = materias['otros'];
    }

    while(input_materia.options.length >0){
        input_materia.options.remove(0);
    }

    Array.from(opcion_selecionada).forEach(function(el){
        let option = new Option(el, el);

        input_materia.appendChild(option);
    })
})