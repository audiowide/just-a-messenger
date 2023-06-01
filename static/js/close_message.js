const message_closes = document.querySelectorAll('.message_close');
const messages = document.querySelectorAll('.message')

for (let i = 0; i < message_closes.length; i++) {
   message_closes[i].onclick = () => {
      messages[i].style.opacity = '0';
      setTimeout(() => {
         messages[i].style.display = 'none';
      }, 100)
   }
}