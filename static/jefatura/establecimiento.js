$('#tableEstablecimientos').DataTable({
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
// responsive: true,
// autoWidth: false,
// destroy: true,
// deferRender: true,
// ajax: {
//     url: window.location.pathname,
//     type: 'POST',
//     data: {
//         'action': 'searchdata'
//     }, // parametros
//     dataSrc: ""
// },
// columns: [
//     // { "data": "nombres"},
//     // { "data": "apellidos"},
//     // { "data": "numero_cedula"},
//     // { "data": "ruc"},
//     // { "data": "tlf_celular"},
//     // { "data": "tipocontribuyente"},
//     // { "data": "tipocontribuyente"},
// ],
// columnDefs: [
//     {
//         targets: [-2],
//         class: 'text-center',
//         orderable: true,
//         render: function (data, type, row) {
//             if (row.tipocontribuyente == 'Natural'){
//                 return '<div class="badge badge-success badge-pill">' + row.tipocontribuyente + '</div></td>';
//                 // return 'Natural'
//             }
//             if (row.tipocontribuyente == 'Juridica') {
//                 return '<div class="badge badge-indigo badge-pill">' + row.tipocontribuyente +'</div></td>';
//                 // return 'Jurídico'
//             }
//         }
//     },
// ],
initComplete: function(settings, json) {
    // alert('Datos cargados');
}
});
