function lista_logs() {
    $('#tableLogs').DataTable({
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
            {"data": "date"},
            {"data": "user"},
            {"data": "object_repr"},
            {"data": "change_message"},
        ],
        columnDefs: [
        {
            targets: [-1],
            orderable: true,
            render: function (data, type, row) {
                if (row.action_flag == 1){
                    return `<i class="fas fa-plus mr-2 text-green"></i> ${row.change_message}`;
                }else if (row.action_flag == 2){
                    return `<i class="fas fa-pen-square mr-2 text-yellow"></i> ${row.change_message}`;
                }else {
                    return `<i class="fas fa-minus-circle mr-2 text-red"></i> ${row.change_message}`;
                }
            }
        },
        ],
        order: [[1, 'desc']],
    initComplete: function(settings, json) {
        // alert('Datos cargados');
    }
    });
}

$(document).ready(function () {
    lista_logs();
});
