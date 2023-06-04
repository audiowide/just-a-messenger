console.log('copy_message.js is a worker');

const copys = document.querySelectorAll('.copy')
const text_for_copy = document.querySelectorAll('.text_for_copy')

// write text to clipboard
for (let i = 0; i < copys.length; i++) {
   copys[i].addEventListener('click', () => {
      navigator.clipboard.writeText(text_for_copy[i].innerHTML)
      copys[i].style.fontSize = '26px'

      setTimeout(() => {
         copys[i].style.fontSize = '20px'
      }, 300)  
   })
}