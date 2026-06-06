const fs = require('fs');

async function testOllama() {
    console.log("Testing Ollama API with fetch...");
    try {
        const response = await fetch('http://localhost:11434/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                model: 'minimax-m3:cloud',
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
            console.log("Response start:", data.response.substring(0, 100));
            if (data.response.startsWith('iVBORw0KGgo') || data.response.length > 1000) {
                console.log("Looks like base64 data. Length:", data.response.length);
                fs.writeFileSync('test_output.png', Buffer.from(data.response, 'base64'));
                console.log("Saved test_output.png");
            } else {
                console.log("Full response text:", data.response);
            }
        }
    } catch(e) {
        console.error("Error:", e.message);
    }
}
testOllama();
