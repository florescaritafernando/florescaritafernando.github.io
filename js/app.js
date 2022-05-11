const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".menu")

navToggle.addEventListener("click", () => {
    navMenu.classList.toggle("menu-visible")
})