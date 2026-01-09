const tabs = document.querySelectorAll('.nav-logo li a');
const contents = document.querySelectorAll('.tab');

tabs.forEach(tab => {
    tab.addEventListener('click', (e) => {
        e.preventDefault(); // Evitar que el <a> recargue la página

        // Quitar la clase active de todas las pestañas
        tabs.forEach(t => t.classList.remove('active'));

        // Agregar active a la pestaña clickeada
        tab.classList.add('active');

        // Quitar active de todas las secciones
        contents.forEach(c => c.classList.remove('active'));

        // Agregar active a la sección correspondiente
        const target = tab.dataset.tab; // ej: 'home' o 'personal'
        document.getElementById(target).classList.add('active');
    });
});