// Abrir modales de acciones
function open_modal_creation(url) {
    $('#creacion').load(url, function () {
        $(this).modal('show');
    });
}

function open_modal_edition(url) {
    $('#edicion').load(url, function () {
        $(this).modal('show');
    });
}

function open_modal_elimination(url) {
    $('#eliminacion').load(url, function () {
        $(this).modal('show');
    });
}

function open_modal_correo(url) {
    $('#correo').load(url, function () {
        $(this).modal('show');
    });
}

//Cerrar modales
function close_modal_creation() {
    $('#creacion').modal('hide');
}

function close_modal_edition() {
    $('#edicion').modal('hide');
}

function close_modal_elimination() {
    $('#eliminacion').modal('hide');
}

function close_modal_correo() {
    $('#correo').modal('hide');
}