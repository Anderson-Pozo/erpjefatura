var $ = jQuery.noConflict();

function  list_contribuyentes() {
    $.ajax({
        // url: "/user/list_user/",
        type: "get",
        dataType: "json",
        success: function (response) {
        },
    })
}

$(document).ready(function () {
    list_contribuyentes();
})
