// var $ = jQuery.noConflict();

function  list_contribuyentes() {
    $.ajax({
        url: "/contribuyente/lista_contribuyentes/",
        type: "get",
        dataType: "json",
        success: function (response) {
            $('#tableContribuyente tbody').html("");
            for (let i = 0; i < response.length; i++){
                let fila = "<tr>";
                fila += '<td>' + response[i]['fields']['nombres'] + '</td>';
                fila += '<td>' + response[i]['fields']['apellidos'] + '</td>';
                fila += '<td>' + response[i]['fields']['numero_cedula'] + '</td>';
                fila += '<td>' + response[i]['fields']['ruc'] + '</td>';
                fila += '<td>' + response[i]['fields']['tlf_celular'] + '</td>';
                fila += '<td>' + response[i]['fields']['email'] + '</td>';
                // fila += '<td><button class="btn btn-primary" onclick="open_modal_edition(\'/user/edit_user/'+response[i]['pk']+'/\');"><i class="fa fa-edit"></i></button><span>&nbsp; &nbsp;</span>';
                // fila += '<button class="btn btn-danger" onclick="open_modal_elimination(\'/user/delete_user/'+response[i]['pk']+'/\');"><i class="fa fa-trash"></i></button></td>';
                fila += "</tr>";
                $('#tableContribuyente tbody').append(fila);
            }
        },
        error: function (error) {
            console.log(error)
        }
    })
}

$(document).ready(function () {
    list_contribuyentes();
})
