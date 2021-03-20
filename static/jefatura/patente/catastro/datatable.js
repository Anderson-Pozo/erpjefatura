$(() => {
    let tbl_catastro = $('#tableCatastro').DataTable({
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
            {"data": "estado_pago"},
            {"data": "ruc"},
            {"data": "nombre_contribuyente"},
            {"data": "tipocontribuyente"},
            {"data": "nombre_establecimiento"},
            {"data": "total_patrimonio"},
            {"data": "estado"},
            {"data": "acciones"},
        ],
        columnDefs: [
            {
                targets: [0],
                class: 'text-center',
                orderable: true,
                render: function (data, type, row) {
                    if (row.estado_pago){
                        return `<h6><span class="badge badge-danger">Pendiente <span class="badge badge-white">${row.dias_retraso}</span></span></h6>`
                    }else {
                        return `<h6><span class="badge badge-success">Abonado</span></h6>`;
                    }
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    let menuOpt = `<div class="row"></div><div class="dropdown no-caret">
                        <button class="btn btn-transparent-dark btn-datatable dropdown-toggle"
                        id="dropdownPeople1" type="button" data-toggle="dropdown" aria-haspopup="true"
                        aria-expanded="false"><i class="fas fa-ellipsis-v"></i></button>
                        <div class="dropdown-menu dropdown-menu-right animated--fade-in-up" aria-labelledby="dropdownPeople1">
                                <a class="dropdown-item btn-light" href="/patente/especie_renovacion/${row.id}">
                                    <div class="dropdown-item-icon">
                                        <i class="fas fa-sync-alt"></i>
                                    </div>
                                    Renovar
                                </a>
                                <a class="dropdown-item btn-light" href="/patente/report_declaracion/${row.id}" target="_blank">
                                    <div class="dropdown-item-icon">
                                        <i class="fas fa-print"></i>
                                    </div>
                                    Declaración
                                </a>
                                <a rel="details" class="dropdown-item btn-light">
                                    <div class="dropdown-item-icon">
                                        <i class="fas fa-funnel-dollar"></i>
                                    </div>
                                    Historial
                                </a>
                                <button onclick="open_modal_edition('/patente/editar/${row.id}')" 
                                    class="dropdown-item btn-light">
                                    <div class="dropdown-item-icon">
                                        <i class="fas fa-edit"></i>
                                    </div>
                                    Exonerar
                                </button>
                                <button onclick="open_modal_elimination('/patente/suspender/${row.id}')" 
                                    class="dropdown-item btn-light">
                                    <div class="dropdown-item-icon">
                                        <i class="fas fa-minus-circle"></i>
                                    </div>
                                    Suspender
                                </button>`;
                    if (row.estado_pago){
                        menuOpt += `<button onclick="open_modal_correo('/patente/enviar_correo/${row.id}')" 
                                    class="dropdown-item btn-light">
                                    <div class="dropdown-item-icon">
                                        <i class="fas fa-envelope"></i>
                                    </div>
                                    Notificar
                                </button>`;
                    }
                    menuOpt += `</div></div>`

                    return menuOpt;
                }
            },
            {
                targets: [-2],
                class: 'text-center',
            }
        ],
    });

    $('#tableCatastro tbody')
        .on('click', 'a[rel="details"]', function () {
            let tr = tbl_catastro.cell($(this).closest('td, li')).index();
            let data = tbl_catastro.row(tr.row).data();
            // console.log(data);

            $('#tblDet').DataTable({
                language: {
                    'url': 'https://raw.githubusercontent.com/Jhon-Paillacho/ERP-estaticos/main/language.json'
                },
                responsive: true,
                autoWidth: false,
                destroy: true,
                deferRender: true,
                order: [[0, "desc"]],
                //data: data.det,
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    {"data": "fecha"},
                    {"data": "impuesto"},
                    {"data": "interes"},
                    {"data": "multa"},
                    {"data": "servicios_administrativos"},
                    {"data": "total"},
                ],
                initComplete: function (settings, json) {

                }
            });
            $('#myModelDet').modal('show');
        })
});


function suspender_patente(pk) {
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
        },
        url: '/patente/suspender/' + pk + '/',
        type: 'post',
        success: function (response) {
            show_notification_success(response.message);
            close_modal_elimination();
            $('#tableCatastro').DataTable().ajax.reload(null, false);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
        }
    });
}

function exonerar_patente(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
        },
        url: '/patente/editar/' + pk + '/',
        type: 'post',
        success: function (response) {
            show_notification_success(response.message);
            close_modal_edition();
            $('#tableCatastro').DataTable().ajax.reload(null, false);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
        }
    });
}

function enviar_correo() {
    let form = $('#form_correo');
    let data = new FormData(form.get(0));
    $.ajax({
        url: form.attr('action'),
        type: form.attr('method'),
        data: data,
        processData: false,
        contentType: false,
        success: function (response) {
            close_modal_correo();
            show_notification_success(response.message);
        },
        error: function (error) {
            // console.log(error);
            show_notification_error(error.responseJSON.message);
            show_errors_creation(error);
        }
    })
}