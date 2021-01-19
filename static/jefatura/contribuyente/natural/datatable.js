function lista_contribuyentes_naturales(){
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
        { "data": "numero_cedula"},
        { "data": "ruc"},
        { "data": "nombres"},
        { "data": "apellidos"},
        { "data": "tlf_celular"},
        // { "data": "tipocontribuyente"},
        { "data": "acciones"},
    ],
    columnDefs: [
        // {
        //     targets: [0],
        //     orderable: true,
        //     render: function (data, type, row) {
        //         return '<p>' + row.nombres + '</p>';
        //     }
        // },
        // {
        //     targets: [-2],
        //     class: 'text-center',
        //     orderable: true,
        //     render: function (data, type, row) {
        //         if (row.tipocontribuyente == 'Natural'){
        //             return '<div class="badge badge-success badge-pill">' + row.tipocontribuyente + '</div></td>';
        //             // return 'Natural'
        //         }
        //         if (row.tipocontribuyente == 'Jurídica') {
        //             return '<div class="badge badge-indigo badge-pill">' + row.tipocontribuyente +'</div></td>';
        //             // return 'Jurídico'
        //         }
        //     }
        // },
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
}


function crear_contribuyente() {
    var data = new FormData($('#form_creation').get(0));
    $.ajax({
        // data: $('#form_creation').serialize(),
        url: $('#form_creation').attr('action'),
        type: $('#form_creation').attr('method'),
        data: data,
        processData: false,
        contentType: false,
        success: function (response) {
            $('#modalContribuyente').modal('hide');
            show_notification_success(response.mensaje);
            lista_contribuyentes_naturales();
            // console.log(response);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.mensaje);
            show_errors_modal(error);
            console.log(error);
        }
    })
}

function delete_user(pk) {
    // console.log($("[name='csrfmiddlewaretoken']").val())
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/user/delete_user/'+pk+'/',
        type: 'post',
        success: function (response) {
            show_notification_success(response.message);
            close_modal_elimination();
            list_users();
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
        }
    });
}

function edit_user() {
    $.ajax({
        data: $('#form_edition').serialize(),
        url: $('#form_edition').attr('action'),
        type: $('#form_edition').attr('method'),
        success: function (response) {
            show_notification_success(response.message);
            close_modal_edition();
            list_users();
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
            show_errors_modal_edition(error);
        }
    })
}

$(document).ready(function () {
    // let nameTable = '#tableContribuyente'
    lista_contribuyentes_naturales();
})