const header__left__menu = document.querySelector('.header__left__menu')
const show__menu = document.querySelector('.show__menu')

show__menu.addEventListener('click', () => {
   if (header__left__menu.style.display == 'none') {
      header__left__menu.style.display = 'flex'
      show__menu.innerHTML = '<i class="fa-solid fa-xmark"></i>'
   } else {
      header__left__menu.style.display = 'none'
      show__menu.innerHTML = '<i class="fa-solid fa-bars"></i>'
   }
})