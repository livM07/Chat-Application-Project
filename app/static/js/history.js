const chatLog = document.getElementById('chat-log');
function getConversations(event) {
    event.preventDefault();


    fetch('/get_conversations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.text())
    .then(reply => {

        x = JSON.parse(reply)
        console.log(x)

        y = x.length
        console.log(y)

        for (var i=0; i<x.length/2; i++) {
            const rowDiv = document.createElement('div');
            rowDiv.classList.add('row', 's', 'rounded-pill', 'justify-content-center', 'text-center', 'rowStyling', 'border', 'bg-light')
            const col1 = document.createElement('div');
            col1.classList.add('col-12', 'text-center', 'conversationElement')
            const col2 = document.createElement('div');
            //col2.classList.add('col-4')

            col1.innerHTML = `<strong>${x[2*i+1]}</strong>`;

            rowDiv.appendChild(col1)
            rowDiv.appendChild(col2)
            
            rowDiv.value = x[2*i]

            //rowDiv.onclick = function(){alert("conversationID: " + rowDiv.value)}
            rowDiv.onclick = function(){window.location.href='/chat/'+rowDiv.value}

            if(x[2*i+1] != "") {
                chatLog.appendChild(rowDiv);
            } 
        }

    });
}

document.onload(getConversations(event))