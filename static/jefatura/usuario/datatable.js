$(() => {
    $('#tableUsuarios').DataTable({
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
                    return `<button class="btn btn-datatable btn-icon btn-outline-yellow mr-2"
                        onclick="open_modal_edition('/usuario/editar/${row.id}')">
                        <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-datatable btn-icon btn-outline-orange"
                        onclick="open_modal_elimination('/usuario/eliminar/${row.id}')">
                        <i class="fas fa-user-minus"></i>
                        </button>`;
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: true,
                render: function (data, type, row) {
                    if (row.is_active) {
                        return '<span class="badge badge-success">Activo</span>';
                    } else {
                        return '<span class="badge badge-danger">Inactivo</span>';
                    }
                }
            }
        ],
        initComplete: function (settings, json) {
            // alert('Datos cargados');
        }
    });
});


function crear_usuario() {
    let form = $('#form_usuario');
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
            $('#tableUsuarios').DataTable().ajax.reload(null, false);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.mensaje);
            show_errors_creation(error);
        }
    })
}


function editar_usuario() {
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
            $('#tableUsuarios').DataTable().ajax.reload(null, false);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
            show_errors_edition(error);
        }
    })
}


function eliminar_usuario(pk) {
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/usuario/eliminar/' + pk + '/',
        type: 'post',
        success: function (response) {
            show_notification_success(response.message);
            close_modal_elimination();
            $('#tableUsuarios').DataTable().ajax.reload(null, false);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
        }
    });
}
