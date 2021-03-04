document.addEventListener('DOMContentLoaded', function () {

    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        locale: 'es',
        initialView: 'dayGridMonth',
        // initialDate: '2021-03-03',
        nextDayThreshold: '00:00:00',
        headerToolbar: {
            right: 'prev,next',
            left: 'title',
            end: 'dayGridMonth,timeGridWeek'
        },

        events: []
    });

    calendar.render();
});
