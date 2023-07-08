document.addEventListener('DOMContentLoaded', () => {
    const messagesList = document.getElementById('MessagesList')
    const chatSlug = document.querySelector('#chatSlug')

    const addNewMessage = document.querySelector('#addNewMessage')
    const messageCreateInput = document.querySelector('#MessageCreateInput')

    // get all messages
    const  getAllMessages = () => {
        messagesList.innerHTML = ''

        fetch(`/api/messages/${chatSlug.value}`)
            .then((res) => res.json())
            .then((messages) => {
                messages.forEach((message) => {
                const div = document.createElement('div')
                div.classList.add('message')
                div.id = `${message.id}_notification`;

                div.innerHTML = `
                <p>${message.message}</p>
                <div class="message__header">
                    <span>${message.created.split('').splice(0,19).join('')}</span>
                    <div>
                        <i class="fa-solid fa-trash"></i>
                        <i class="fa-solid fa-copy"></i>
                    </div>
                </div>
                `
                messagesList.appendChild(div)
                })
            })
            .catch((err) => {
                console.log(err)
            })
    }
    
    // Add a new message
    addNewMessage.addEventListener('submit', async (e) => {
        e.preventDefault()

        let formData = new FormData(addNewMessage);
        console.log(messageCreateInput.value)
        
        await fetch(`/api/messages/${chatSlug.value}`, {
            method: 'POST',
            body: formData
        })
            .then((res) => res.json())
            .then((messages) => {
                getAllMessages()
                messageCreateInput.value = ''
            })
            .catch((err) => {
                console.log(err)
            })
    })

    // update messages
    const updateMessages = () => {
        try {
            getAllMessages();
        } catch (err) {
            console.log(err)
        }
    };
    

    setInterval(updateMessages, 1000)

    setInterval(() => {
        console.log('1sec')
    }, 1000)

    getAllMessages()
})