function lista_contribuyentes_naturales(){
    $('#tableContribuyente').DataTable({
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
        { "data": "numero_cedula"},
        { "data": "ruc"},
        { "data": "nombres"},
        { "data": "apellidos"},
        { "data": "tlf_celular"},
        // { "data": "tipocontribuyente"},
        { "data": "estado"},
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
                let buttons = '<button class="btn btn-datatable btn-icon btn-outline-yellow mr-2"' +
                                ' onclick="open_modal_edition(\'/contribuyente/natural/editar/' + row.id +'/\')">' +
                                '<i class="fas fa-edit"></i>' +
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
            close_modal_creation();
            show_notification_success(response.mensaje);
            lista_contribuyentes_naturales();
            // console.log(response);
        },
        error: function (error) {
            show_notification_error(error.responseJSON.mensaje);
            show_errors_creation(error);
            // console.log(error);
        }
    })
}

function editar_contribuyente_natural() {
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
            lista_contribuyentes_naturales();
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
            show_errors_edition(error);
            // show_errors_modal_edition(error);
            // console.log(error.responseJSON.message);
        }
    })
}

function eliminar_contribuyente_natural(pk) {
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/contribuyente/natural/eliminar/'+ pk +'/',
        type: 'post',
        success: function (response) {
            show_notification_success(response.message);
            close_modal_elimination();
            lista_contribuyentes_naturales();
        },
        error: function (error) {
            show_notification_error(error.responseJSON.message);
        }
    });
}

$(document).ready(function () {
    lista_contribuyentes_naturales();
})