function open_modal_contribuyente_juridico(url) {
    $('#modalContribuyenteJuridico').load(url, function () {
        $(this).modal('show');
    });
}

function close_modal_contribuyente_juridico() {
    $('#modalContribuyenteJuridico').modal('hide');
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
        error += '<div class="text-danger text-xs">' +
                    '<li><strong>' + errors.responseJSON.error[item] + '</strong></li>' +
                  '</div>';
    }
    $('#errors').append(error);
}
