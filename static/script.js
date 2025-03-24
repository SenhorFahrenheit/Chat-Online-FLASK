// cria a conexão websocket
var socket = io.connect("http://" + window.location.hostname + ":" + location.port);

// recebe a mensagem do servidor
socket.on("message", function(msg) {
    var chatBox = document.getElementById("chat-box");
    var newMessage = document.createElement("p");
    newMessage.textContent = msg;
    chatBox.appendChild(newMessage);
});

function sendMessage() {
    var messageInput = document.getElementById("message");
    var message = messageInput.value;
    if (message.trim() !== "") {
        // envia a mensagem para o servidor
        socket.send(message);
        messageInput.value = "";
    }
}
