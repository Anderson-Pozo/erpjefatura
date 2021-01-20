function lista_vencimiento(){
    $('#tableVencimiento').DataTable({
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
    autoWidth: true,
    // scrollX: true,
    destroy: true,
    deferRender: true,
    ordering: true,
    ajax: {
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'searchdata'
        }, // parametros
        dataSrc: ""
    },
    columns: [
        { "data": "digito"},
        { "data": "no_obligado"},
        { "data": "obligado"},
        { "data": "acciones"},
    ],
    columnDefs: [
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
         alert('Datos cargados');
    }
    });
}



// function crear_contribuyente() {
//     var data = new FormData($('#form_creation').get(0));
//     $.ajax({
//         // data: $('#form_creation').serialize(),
//         url: $('#form_creation').attr('action'),
//         type: $('#form_creation').attr('method'),
//         data: data,
//         processData: false,
//         contentType: false,
//         success: function (response) {
//             $('#modalContribuyente').modal('hide');
//             show_notification_success(response.mensaje);
//             lista_contribuyentes();
//             // console.log(response);
//         },
//         error: function (error) {
//             show_notification_error(error.responseJSON.mensaje);
//             show_errors_modal(error);
//             console.log(error);
//         }
//     })
// }

$(document).ready(function () {
    lista_vencimiento();
})