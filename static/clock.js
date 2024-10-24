function updateClock() {
    const now = new Date();
    const timeElement = document.getElementById('time');
    const dateElement = document.getElementById('date');

    const timeString = now.toLocaleTimeString('ru-RU', { hour12: false });
    const dateString = now.toLocaleDateString('ru-RU', { year: 'numeric', month: 'long', day: 'numeric' });

    timeElement.textContent = timeString;
    dateElement.textContent = dateString;
}

setInterval(updateClock, 1000);
updateClock();