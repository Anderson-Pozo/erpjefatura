function lista_establecimientos() {
    $('#tableEstablecimientos').DataTable({
        language: {
            'url': 'https://raw.githubusercontent.com/Jhon-Paillacho/ERP-estaticos/main/language.json'
        },
        dom: "<'row'<'col-sm-12 col-md-6'B><'col-sm-12 col-md-6'f>>" +
            "<'row'<'col-sm-12'tr>>" +
            "<'row'<'col-sm-12 col-md-5'li><'col-sm-12 col-md-7'p>>",
        buttons: [
            {
                extend: 'excelHtml5',
                text: 'Exportar Excel <i class="fas fa-file-excel"></i>',
                titleAttr: 'Excel',
                className: 'btn btn-green btn-flat btn-xs'
            },
            {
                extend: 'pdfHtml5',
                text: 'Exportar PDF <i class="fas fa-file-pdf"></i>',
                titleAttr: 'PDF',
                className: 'btn btn-red btn-flat btn-xs'
            },
            {
                extend: 'print',
                text: 'Imprimir <i class="fas fa-print"></i>',
                titleAttr: 'Imprimir',
                className: 'btn btn-teal btn-flat btn-xs'
            },
            // 'excel', 'pdf', 'print'
        ],
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
            {"data": "nombre"},
            {"data": "fecha_inicio_actividad"},
            {"data": "total_patrimonio"},
            {"data": "tipo_actividad"},
            {"data": "direccion"},
            // {"data": "estado"},
            {"data": "acciones"},
        ],
        columnDefs: [
            {
                targets: [0, 1, 2, 3],
                class: 'text-center',
                width: "15%"
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    let buttons = '<button class="btn btn-datatable btn-icon btn-outline-yellow mr-2"' +
                        ' onclick="open_modal_edition(\'/establecimiento/editar/' + row.id + '/\')">' +
                        '<i class="fas fa-edit"></i>' +
                        '</button>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
            // alert('Datos cargados');
        }
    });
}


function crear_establecimientos() {
    var data = new FormData($('#form_establecimientos').get(0));
    $.ajax({
        url: $('#form_establecimientos').attr('action'),
        type: $('#form_establecimientos').attr('method'),
        data: data,
        processData: false,
        contentType: false,
        success: function (response) {
            $('#modalEstablecimiento').modal('hide');
            close_modal_creation();
            show_notification_success(response.mensaje);
            lista_establecimientos();
            // console.log(response);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.mensaje);
            show_errors_creation(error);
            // console.log(error);
        }
    })
}


function editar_establecimientos() {
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
            lista_establecimientos();
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
            show_errors_edition(error);
            // show_errors_modal_edition(error);
            // console.log(error.responseJSON.message);
        }
    })
}


function eliminar_establecimientos(pk) {
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: 'eliminar/' + pk + '/',
        type: 'post',
        success: function (response) {
            show_notification_success(response.message);
            close_modal_elimination();
            lista_establecimientos();
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
        }
    });
}


$(document).ready(function () {
    lista_establecimientos();
})
