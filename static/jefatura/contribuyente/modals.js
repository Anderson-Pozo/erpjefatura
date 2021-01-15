function open_modal_creacion(url) {
    $('#modalContribuyente').load(url, function () {
        $(this).modal('show');
    });
}

function close_modal_creacion() {
    $('#modalContribuyente').modal('hide');
}

function show_notification_success(message) {
    Swal.fire({
        title: 'Acción procesada de forma correcta',
        text: message,
        icon: 'success'
    })
}

function show_notification_error(message) {
    Swal.fire({
        title: 'Error',
        text: message,
        icon: 'error'
    })
}

function show_errors_modal(errors) {
    $('#errors').html("");
    let error = '';
    for(let item in errors.responseJSON.error){
        error += '<div class="alert alert-danger">' +
                    '<strong>' + errors.responseJSON.error[item] + '</strong>' +
                  '</div>';
    }
    $('#errors').append(error);
}