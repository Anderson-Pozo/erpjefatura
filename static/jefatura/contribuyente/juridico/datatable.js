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
        // { "data": "telefono_representante"},
        { "data": "estado"},
        { "data": "acciones"},
    ],
    columnDefs: [
        {
            targets: [-1],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                let buttons = '<button class="btn btn-datatable btn-icon btn-outline-yellow mr-2"' +
                                ' onclick="open_modal_edition(\'/contribuyente/juridico/editar/' + row.id +'/\')">' +
                                '<i class="fas fa-edit"></i>' +
                                '</button>';
                buttons += '<button class="btn btn-datatable btn-icon btn-outline-orange" ' +
                            ' onclick="open_modal_elimination(\'/contribuyente/juridico/eliminar/' + row.id +'/\')">' +
                            '<i class="fas fa-trash"></i>' +
                            '</button>';
                return buttons;
            }
        },
        {
            targets: [-2],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                if (row.estado){
                    return '<span class="badge badge-success">Activo</span>';
                }else {
                    return '<span class="badge badge-danger">Suspendido</span>';
                }
            }
        }
    ],
    initComplete: function(settings, json) {
        // alert('Datos cargados');
    }
    });
}


function crear_contribuyente_juridico() {
    let data = new FormData($('#form_creation').get(0));
    $.ajax({
        url: $('#form_creation').attr('action'),
        type: $('#form_creation').attr('method'),
        data: data,
        processData: false,
        contentType: false,
        success: function (response) {
            close_modal_creation();
            show_notification_success(response.mensaje);
            lista_contribuyentes();
            // console.log(response);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.mensaje);
            show_errors_creation(error);
            // console.log(error);
        }
    })
}


function editar_contribuyente_juridico() {
    let data = new FormData($('#form_edition_juridico').get(0));
    $.ajax({
        url: $('#form_edition_juridico').attr('action'),
        type: $('#form_edition_juridico').attr('method'),
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: function (response) {
            show_notification_success(response.message);
            close_modal_edition();
            lista_contribuyentes();
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
            show_errors_edition(error);
            // show_errors_modal_edition(error);
            // console.log(error.responseJSON.message);
        }
    })
}

function eliminar_contribuyente(pk) {
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/contribuyente/juridico/eliminar/'+ pk +'/',
        type: 'post',
        success: function (response) {
            show_notification_success(response.message);
            close_modal_elimination();
            lista_contribuyentes();
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
        }
    });
}

$(document).ready(function () {
    lista_contribuyentes();
})