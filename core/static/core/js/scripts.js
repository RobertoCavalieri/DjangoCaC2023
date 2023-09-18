document.getElementById('mostrar-notificacion').addEventListener('click', function() {
    var notificacion = document.getElementById('notificacion');
    notificacion.style.display = 'block';

    document.getElementById('cerrar-notificacion').addEventListener('click', function() {
        notificacion.style.display = 'none';
    });
});