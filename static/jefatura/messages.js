// Mostrar Swal alert
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

// Mensajes de error para creación y edición
function show_errors_creation(errors) {
    $('#errors').html("");
    let error = '';
    for(let item in errors.responseJSON.error){
        error += '<div class="text-danger text-xs">' +
                    '<li><strong>' + errors.responseJSON.error[item] + '</strong></li>' +
                  '</div>';
    }
    $('#errors').append(error);
}

function show_errors_edition(errors) {
    $('#errors_edition').html("");
    let error = '';
    for(let item in errors.responseJSON.error){
        error += '<div class="text-danger text-xs">' +
                    '<li><strong>' + errors.responseJSON.error[item] + '</strong></li>' +
                  '</div>';
    }
    $('#errors_edition').append(error);
}
