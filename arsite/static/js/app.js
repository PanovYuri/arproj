function activeBurger() {
    const burger = document.getElementsByClassName('navbar-burger')[0]
    const menu = document.getElementsByClassName('navbar-menu')[0]
    burger.classList.toggle('is-active')
    menu.classList.toggle('is-active')
}