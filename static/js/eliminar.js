const btnsEliminacion = document.querySelectorAll('.btnEliminacion');

(function (){
        btnsEliminacion.forEach(btn => {
            btn.addEventListener('click', function (e){
                let confirmacion = confirm("¿confirma la elimnacion?");
                if( !confirmacion){
                    e.preventDefault();
                }
            });
        })
})();