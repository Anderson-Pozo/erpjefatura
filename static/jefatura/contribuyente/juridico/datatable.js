function lista_contribuyentes(){
    $('#tableContribuyenteJuridico').DataTable({
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
        { "data": "ruc"},
        { "data": "razon_social"},
        { "data": "tlf_celular"},
        { "data": "email"},
        { "data": "nombres_representante"},
        { "data": "telefono_representante"},
        { "data": "acciones"},
    ],
    columnDefs: [
        {
            targets: [-1],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                let buttons = '<button class="btn btn-datatable btn-icon btn-outline-yellow mr-2"' +
                                ' onclick="open_modal_edition(\'/contribuyente/natural/editar/' + row.id +'/\')">' +
                                '<i class="fas fa-edit"></i>' +
                                '</button>';
                buttons += '<button class="btn btn-datatable btn-icon btn-outline-orange" onclick="alert("Hola")">' +
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


function crear_contribuyente_juridico() {
    var data = new FormData($('#form_creation').get(0));
    $.ajax({
        // data: $('#form_creation').serialize(),
        url: $('#form_creation').attr('action'),
        type: $('#form_creation').attr('method'),
        data: data,
        processData: false,
        contentType: false,
        success: function (response) {
            $('#modalContribuyenteJuridico').modal('hide');
            show_notification_success(response.mensaje);
            lista_contribuyentes();
            // console.log(response);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.mensaje);
            show_errors_modal(error);
            // console.log(error);
        }
    })
}

$(document).ready(function () {
    lista_contribuyentes();
})