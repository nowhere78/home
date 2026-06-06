const fs = require('fs');

async function testOllama() {
    console.log("Testing Ollama API with Gemma...");
    try {
        const response = await fetch('http://localhost:11434/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                model: 'gemma:latest',
                prompt: 'Hyper-realistic medical 3D rendering of arginine molecular structure, clean white background, professional medical textbook illustration',
                stream: false
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log("Response fields:", Object.keys(data));
        
        if (data.response) {
            console.log("Response start:", data.response.substring(0, 200));
        }
    } catch(e) {
        console.error("Error:", e.message);
    }
}
testOllama();
