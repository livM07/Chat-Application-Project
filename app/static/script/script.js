// Home Page Carousel
$(document).ready(function() {
  $('#imageCarousel').carousel({
    interval: 3000
  });
});

// Chat
const chatForm = document.getElementById('chat-form');
const chatInput = document.getElementById('chat-input');
const locationInput = document.getElementById('location-input');

const chatLog = document.getElementById('chat-log');
const chatTitle = document.getElementById('chat-title');

var locButton = document.getElementById("loc-button");
var locCon = document.getElementById("location-container");
var chatCon = document.getElementById("chat-container");
var username = document.getElementById("username");

locButton.addEventListener("click", function() {
    var loc = locationInput.value.trim()
    setTitle(loc);
});

console.log(window.location.pathname);
path = window.location.pathname;

pathElements = path.split('/');
if (pathElements.length == 3) {
    console.log('hi')
    getMessages(pathElements[2]);
}

function sendMessage(event) {
    console.log('hi');
    event.preventDefault();
    const message = chatInput.value.trim();
    console.log(message);
    const location = locationInput.value.trim();
    console.log(location);
    if (message === '' || location === '') return;
    console.log('hey3');

    //setTitle(location);
    appendMessage(username, message);
    console.log('hey');

    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `message=${encodeURIComponent(message)}&location=${encodeURIComponent(location)}`
    })
    .then(response => response.text())
    .then(reply => {
        appendMessage('TravelBot', reply);
        chatInput.value = '';
    });
}

function getMessages(id) {
    console.log('hi1')
    fetch('/get_messages/' + id, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.text())
    .then(reply => {
        console.log('hi2');
        console.log(reply);
        x = JSON.parse(reply);
        title = x[0];
        msgs = x[1];

        setTitle(title);
        locationInput.value = title;
        json = JSON.parse(msgs);
        for (let i = 0; i < json.messages.length; i ++) {
            appendMessage(json.messages[i].author, json.messages[i].message);
        }
    });

}

function appendMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.innerHTML = `<strong>${sender}: </strong>${message}`;
    chatLog.appendChild(messageElement);
}

function setTitle(title) {
    const titleElement = document.createElement('div');
    titleElement.innerHTML = `<strong>${title}</strong>`;
    chatTitle.appendChild(titleElement);
    locCon.style.display = "none";
    chatCon.style.display = "block";
}

// History
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