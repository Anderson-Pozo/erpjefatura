$(() => {
    $('#tableGrupos').DataTable({
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
            {"data": "id"},
            {"data": "name"},
            {"data": "acciones"},
        ],
        columnDefs: [
            {
                targets: [0],
                class: 'text-center'
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return `<button class="btn btn-datatable btn-icon btn-outline-yellow mr-2"
                        onclick="open_modal_edition('/usuario/editar_grupo/${row.id}')">
                        <i class="fas fa-edit"></i>
                        </button>`;
                }
            }
        ],
        initComplete: function (settings, json) {
            // alert('Datos cargados');
        }
    });
});


function crear_grupo() {
    let form = $('#form_grupo');
    let data = new FormData(form.get(0));
    $.ajax({
        url: form.attr('action'),
        type: form.attr('method'),
        data: data,
        processData: false,
        contentType: false,
        success: function (response) {
            close_modal_creation();
            show_notification_success(response.mensaje);
            $('#tableGrupos').DataTable().ajax.reload(null, false);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.mensaje);
            show_errors_creation(error);
        }
    })
}


function editar_grupo() {
    let form = $('#form_edition');

    let data = new FormData(form.get(0));
    $.ajax({
        url: form.attr('action'),
        type: form.attr('method'),
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: function (response) {
            show_notification_success(response.message);
            close_modal_edition();
            $('#tableGrupos').DataTable().ajax.reload(null, false);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
            show_errors_edition(error);
        }
    })
}
