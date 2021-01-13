function open_modal_creacion(url) {
    $('#modalContribuyente').load(url, function () {
        $(this).modal('show');
    });
}