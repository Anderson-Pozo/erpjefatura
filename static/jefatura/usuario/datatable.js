function lista_usuarios() {
    $('#tableUsuarios').DataTable({
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
            // {"data": "numero"},
            {"data": "username"},
            {"data": "email"},
            {"data": "first_name"},
            {"data": "last_name"},
            {"data": "is_active"},
            {"data": "acciones"},
        ],
        columnDefs: [
        {
            targets: [-1],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                let buttons = '<button class="btn btn-datatable btn-icon btn-outline-yellow mr-2"' +
                                ' onclick="open_modal_edition(\'/usuario/editar/' + row.id +'/\')">' +
                                '<i class="fas fa-edit"></i>' +
                                '</button>';
                buttons += '<button class="btn btn-datatable btn-icon btn-outline-orange" ' +
                            ' onclick="open_modal_elimination(\'/usuario/eliminar/' + row.id +'/\')">' +
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
                if (row.is_active){
                    return '<span class="badge badge-success">Activo</span>';
                }else {
                    return '<span class="badge badge-danger">Desactivo</span>';
                }
            }
        }
    ],
    initComplete: function(settings, json) {
        // alert('Datos cargados');
    }
    });
}


function crear_usuario() {
    var data = new FormData($('#form_usuario').get(0));
    $.ajax({
        url: $('#form_usuario').attr('action'),
        type: $('#form_usuario').attr('method'),
        data: data,
        processData: false,
        contentType: false,
        success: function (response) {
            close_modal_creation();
            show_notification_success(response.mensaje);
            lista_usuarios();
            // console.log(response);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.mensaje);
            show_errors_creation(error);
            // console.log(error);
        }
    })
}


function editar_usuario() {
    let data = new FormData($('#form_edition').get(0));
    $.ajax({
        url: $('#form_edition').attr('action'),
        type: $('#form_edition').attr('method'),
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: function (response) {
            show_notification_success(response.message);
            close_modal_edition();
            lista_usuarios();
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
            show_errors_edition(error);
            // show_errors_modal_edition(error);
            // console.log(error.responseJSON.message);
        }
    })
}


function eliminar_usuario(pk) {
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/usuario/eliminar/'+ pk +'/',
        type: 'post',
        success: function (response) {
            show_notification_success(response.message);
            close_modal_elimination();
            lista_usuarios();
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
        }
    });
}


$(document).ready(function () {
    lista_usuarios();
})
