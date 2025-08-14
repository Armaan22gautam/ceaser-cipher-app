async function processCipher() {
    const text = document.getElementById('text-input').value;
    const shift = document.getElementById('shift-value').value;
    const mode = document.querySelector('.mode-toggle button.active').id.replace('-btn', '');
    
    try {
        const response = await fetch('http://localhost:5500/api/cipher', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text, shift, mode }),
            mode: 'cors'
        });
        
        if (!response.ok) throw new Error('Network response was not ok');
        
        const data = await response.json();
        document.getElementById('result-output').textContent = data.result;
        
    } catch (error) {
        console.error('Fetch error:', error);
        document.getElementById('result-output').textContent = 'Error: ' + error.message;
        document.getElementById('result-output').classList.add('error');
    }
}