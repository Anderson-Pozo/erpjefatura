function lista_multa() {
    $('#tableMulta').DataTable({
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
            {"data": "fecha"},
            {"data": "porcentaje"},
            {"data": "acciones"},
        ],

        columnDefs: [
            //     {
            //         targets: [-1],
            //         class: 'text-center',
            //         orderable: false,
            //         render: function (data, type, row) {
            //             let buttons = '<button class="btn btn-datatable btn-icon btn-outline-yellow mr-2">' +
            //                 '<i class="fas fa-edit"></i>' +
            //                 '</button>';
            //             buttons += '<button class="btn btn-datatable btn-icon btn-outline-orange">' +
            //                 '<i class="fas fa-trash"></i>' +
            //                 '</button>';
            //             return buttons;
            //         }
            //     },
            // ],
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    let buttons = '<button class="btn btn-datatable btn-icon btn-outline-yellow mr-2"' +
                        ' onclick="open_modal_edition(\'/impuesto/multa/editar/' + row.id + '/\')">' +
                        '<i class="fas fa-edit"></i>' +
                        '</button>';
                    buttons += '<button class="btn btn-datatable btn-icon btn-outline-orange" ' +
                        ' onclick="open_modal_elimination(\'/impuesto/multa/eliminar/' + row.id + '/\')">' +
                        '<i class="fas fa-trash"></i>' +
                        '</button>';
                    return buttons;
                }
            }
        ],
        initComplete: function (settings, json) {
            // alert('Datos cargados');
        }
    });
}


function crear_multa() {
    var data = new FormData($('#form_creation').get(0));
    $.ajax({
        url: $('#form_creation').attr('action'),
        type: $('#form_creation').attr('method'),
        data: data,
        processData: false,
        contentType: false,
        success: function (response) {
            close_modal_creation();
            show_notification_success(response.mensaje);
            lista_multa();
            // console.log(response);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.mensaje);
            show_errors_creation(error);
            // console.log(error);
        }
    })
}


function editar_multa() {
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
            lista_multa();
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
            show_errors_edition(error);
            // show_errors_modal_edition(error);
            // console.log(error.responseJSON.message);
        }
    })
}


function eliminar_multa(pk) {
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/impuesto/multa/eliminar/' + pk + '/',
        type: 'post',
        success: function (response) {
            show_notification_success(response.message);
            close_modal_elimination();
            lista_multa();
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
        }
    });
}


$(document).ready(function () {
    lista_multa();
})