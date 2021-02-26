$(function () {
    const select_search = $('#search');
    const input_comprador = $('input[name="comprador"]');

    select_search.on('change', function () {
        const value = select_search.select2('data')[0].id;
        input_comprador.val(value);
        //console.log(input_comprador);
    });

    select_search.select2({
        theme: "bootstrap4",
        language: {
            inputTooShort: function () {
                return "Ingrese más de dos caracteres";
            },
            searching: function () {
                return "Buscando..."
            }
        },
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: '/alcabala/get_personas/',
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'autoselect'
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
        placeholder: 'Ingrese número de cédula',
        minimumInputLength: 2,
    });


    const select_search_vendedor = $('#search_vendedor');
    const input_vendedor = $('input[name="vendedor"]');

    select_search_vendedor.on('change', function () {
        const value = select_search_vendedor.select2('data')[0].id;
        input_vendedor.val(value);
        //console.log(input_comprador);
    });

    select_search_vendedor.select2({
        theme: "bootstrap4",
        language: {
            inputTooShort: function () {
                return "Ingrese más de dos caracteres";
            },
            searching: function () {
                return "Buscando..."
            }
        },
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: '/alcabala/get_personas/',
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'getvendedor'
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
        placeholder: 'Ingrese número de cédula',
        minimumInputLength: 2,
    });


    const select_search_predio = $('#search_predio');
    const input_predio = $('input[name="predio"]');

    select_search_predio.on('change', function () {
        const value = select_search_predio.select2('data')[0].id;
        input_predio.val(value);
        //console.log(input_comprador);
    });

    select_search_predio.select2({
        theme: "bootstrap4",
        language: {
            inputTooShort: function () {
                return "Ingrese más de dos caracteres";
            },
            searching: function () {
                return "Buscando..."
            }
        },
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: '/alcabala/get_personas/',
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'getpredio'
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
        placeholder: 'Ingrese un valor',
        minimumInputLength: 2,
    });
})