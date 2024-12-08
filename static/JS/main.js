
// Evento para ocultar la barra de navegación en celulares
document.addEventListener("DOMContentLoaded", () => {
    const menuBtn = document.querySelector(".menu-btn");
    const navLinks = document.getElementById("nav-links");

    menuBtn.addEventListener("click", () => {
        navLinks.classList.toggle("show");
    });
});