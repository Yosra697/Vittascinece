// Fonction pour Text-to-Speech
function generateTTS() {
    const text = document.getElementById("tts-text").value;
    const gender = document.getElementById("tts-gender").value;
    const speed = document.getElementById("tts-speed").value || 1.0;

    fetch("/tts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, gender, speed }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.audio_url) {
                const audio = document.getElementById("tts-audio");
                audio.src = data.audio_url;
                audio.play();
            } else {
                alert("Error: " + data.error);
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("Une erreur est survenue lors de la génération audio.");
        });
}


function startTranscription() {
    console.log("Initializing WebSocket connection to ws://127.0.0.1:5000/stt...");

    const socket = new WebSocket("ws://127.0.0.1:5050/stt");

    socket.onopen = () => {
        console.log("WebSocket connection established.");
        alert("Microphone activated. Please speak!");

        // Now it's safe to send the message
        console.log("Sending 'start' message to the server...");
        socket.send("start");
    };

    socket.onmessage = (event) => {
        console.log("Message received from server:", event.data);
        const output = document.getElementById("stt-output");
        output.innerText += event.data + "\n"; // Append received text to the output area
    };

    socket.onerror = (error) => {
        console.error("WebSocket encountered an error:", error);
        alert("An error occurred with the WebSocket connection. Check the console for details.");
    };

    socket.onclose = (event) => {
        console.log(`WebSocket connection closed. Code: ${event.code}, Reason: ${event.reason}`);
        alert("Transcription ended.");
    };
}

