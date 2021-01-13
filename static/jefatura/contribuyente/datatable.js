$('#tableContribuyente').DataTable({
language: {
    "decimal": "",
    "emptyTable": "No hay información",
    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
    "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
    "infoPostFix": "",
    "thousands": ",",
    "lengthMenu": "Mostrar _MENU_ entradas",
    "loadingRecords": "Cargando...",
    "processing": "Procesando...",
    "search": "Buscar:",
    "zeroRecords": "Sin resultados encontrados",
    "paginate": {
        "first": "Primero",
        "last": "Último",
        "next": "Siguiente",
        "previous": "Anterior",
    },
},
responsive: true,
autoWidth: false,
destroy: true,
deferRender: true,
ajax: {
    url: window.location.pathname,
    type: 'POST',
    data: {
        'action': 'searchdata'
    }, // parametros
    dataSrc: ""
},
columns: [
    { "data": "nombres"},
    { "data": "apellidos"},
    { "data": "numero_cedula"},
    { "data": "ruc"},
    { "data": "tlf_celular"},
    { "data": "tipocontribuyente"},
    { "data": "tipocontribuyente"},
],
columnDefs: [
    {
        targets: [-2],
        class: 'text-center',
        orderable: true,
        render: function (data, type, row) {
            if (row.tipocontribuyente == 'Natural'){
                return '<div class="badge badge-success badge-pill">' + row.tipocontribuyente + '</div></td>';
                // return 'Natural'
            }
            if (row.tipocontribuyente == 'Juridica') {
                return '<div class="badge badge-indigo badge-pill">' + row.tipocontribuyente +'</div></td>';
                // return 'Jurídico'
            }
        }
    },
    {
        targets: [-1],
        class: 'text-center',
        orderable: false,
        render: function (data, type, row) {
            let buttons = '<button class="btn btn-datatable btn-icon btn-outline-yellow mr-2">' +
                            '<i class="fas fa-edit"></i>' +
                            '</button>';
            buttons += '<button class="btn btn-datatable btn-icon btn-outline-orange">' +
                        '<i class="fas fa-trash"></i>' +
                        '</button>';
            return buttons;
        }
    }
],
initComplete: function(settings, json) {
    // alert('Datos cargados');
}
});


function register_user() {
    $.ajax({
        data: $('#form_creation').serialize(),
        url: $('#form_creation').attr('action'),
        type: $('#form_creation').attr('method'),
        success: function (response) {
            // show_notification_success(response.message);
            // close_modal_creation();
        },
        error: function (error) {
            // show_notification_error(error.responseJSON.message);
            // show_errors_modal(error);
        }
    })
}