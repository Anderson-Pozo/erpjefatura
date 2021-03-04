document.addEventListener('DOMContentLoaded', function () {

    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        locale: 'es',
        views: {
            dayGridMonth: { // name of view
                titleFormat: {year: 'numeric', month: 'long'}
                // other view-specific options here
            }
        },
        initialView: 'dayGridMonth',
        // initialDate: '2021-03-03',
        nextDayThreshold: '00:00:00',
        headerToolbar: {
            right: 'prev,next',
            left: 'title',
            end: 'dayGridMonth'
        },
        events: [
            {
                title: "Retrasado",
                start: "2021-03-01",
                end: "2021-03-10",
                description: 'Hola mundo',
                backgroundColor: '#e03131',
                borderColor: '#e03131'
            },
        ]
    });
    console.log(calendar);

    calendar.render();
});
