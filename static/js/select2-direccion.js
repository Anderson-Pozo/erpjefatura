$(function () {
    // Select comprador
    const select_search = $('#search_direccion');
    const input_direccion = $('input[name="direccion"]');

    select_search.on('change', () => {
        const value = select_search.select2('data')[0].id;
        input_direccion.val(value);
        //console.log(input_comprador);
    });

    select_search.select2({
        theme: "bootstrap4",
        language: {
            inputTooShort: () => {
                return "Ingrese más de dos caracteres";
            },
            searching: () => {
                return "Buscando..."
            },
            noResults: () => {
                return 'No hay resultados'
            }
        },
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: '/direccion/get_direcciones/',
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'get_direccion'
                }
                return queryParameters;
            },
            processResults: function (data) {
                console.log(data);
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese parroquia, barrio o calle',
        minimumInputLength: 2,
    });
})