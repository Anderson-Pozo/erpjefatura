function format(d) {
    return '<table cellpadding="5" cellspacing="0" style="padding-left:50px; border: hidden">' +
        '<tr>' +
        '<td>Nombres representante:</td>' +
        '<td>' + d.nombres_representante + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Apellidos representante:</td>' +
        '<td>' + d.apellidos_representante + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Email representante:</td>' +
        '<td>' + d.correo_representante + '</td>' +
        '</tr>' +
        '</table>';
}

function lista_contribuyentes() {
    let table = $('#tableContribuyenteJuridico').DataTable({
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
        destroy: true,
        deferRender: true,
        ordering: true,
        // buttons: ['copy', 'csv', 'excel'],
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            }, // parametros
            dataSrc: ""
        },
        columns: [
            {
                "className": 'details-control',
                "orderable": false,
                "data": null,
                "defaultContent": '',
                // render: (data, type, row) =>{
                //     let datos = new Object(data);
                //     // console.log(datos);
                //     // return `<button onclick="show_childs( ${datos})"></buttonon>`;
                //     // return '<button onclick="show_childs(\'' + datos +'\')">aC</button>';
                // }
            },
            {"data": "ruc"},
            {"data": "razon_social"},
            {"data": "tlf_celular"},
            {"data": "email"},
            {"data": "nombres_representante"},
            {"data": "estado"},
            {"data": "acciones"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    let buttons = '<button class="btn btn-datatable btn-icon btn-outline-yellow mr-2"' +
                        ' onclick="open_modal_edition(\'/contribuyente/juridico/editar/' + row.id + '/\')">' +
                        '<i class="fas fa-edit"></i>' +
                        '</button>';
                    buttons += '<button class="btn btn-datatable btn-icon btn-outline-orange" ' +
                        ' onclick="open_modal_elimination(\'/contribuyente/juridico/eliminar/' + row.id + '/\')">' +
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
                    if (row.estado) {
                        return '<span class="badge badge-success">Activo</span>';
                    } else {
                        return '<span class="badge badge-danger">Suspendido</span>';
                    }
                }
            }
        ],
        initComplete: function (settings, json) {
            // alert('Datos cargados');
        },
    });
    $('#tableContribuyenteJuridico tbody').on('click', 'td.details-control',
        function () {
            let tr = $(this).closest('tr');
            let row = table.row(tr);

            if (row.child.isShown()) {
                row.child.hide();
                tr.removeClass('shown');
            } else {
                row.child(format(row.data())).show();
                // console.log(row.data());
                tr.addClass('shown');
            }
        });
}

function show_childs(variable) {
    console.log(JSON.parse(variable));

    // let table = $('#tableContribuyenteJuridico').DataTable();
    // $('#tableContribuyenteJuridico tbody').
    //     on('click', 'td.details-control',
    //     function () {
    //         let tr = $(this).closest('tr');
    //         let row = table.row( tr );
    //
    //         if ( row.child.isShown() ) {
    //             row.child.hide();
    //             tr.removeClass('shown');
    //         }
    //         else {
    //             row.child( format(row.data()) ).show();
    //             console.log(row.data());
    //             tr.addClass('shown');
    //         }
    // } );
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
        success: (response) => {
            show_notification_success(response.message);
            close_modal_edition();
            // lista_contribuyentes();
            $(document).ready(() => lista_contribuyentes());
            // setTimeout(window.location.reload(),1000);
            // window.location.reload();
        },
        error: (error) => {
            show_notification_error(error.responseJSON.message);
            show_errors_edition(error);
        }
    })
}

function eliminar_contribuyente(pk) {
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/contribuyente/juridico/eliminar/' + pk + '/',
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

$(document).ready(() => lista_contribuyentes());
