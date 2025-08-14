from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)  # Enable CORS for all routes

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            if char.islower():
                start = ord('a')
                new_pos = (ord(char) - start + shift_amount) % 26
                result += chr(start + new_pos)
            else:
                start = ord('A')
                new_pos = (ord(char) - start + shift_amount) % 26
                result += chr(start + new_pos)
        else:
            result += char
    return result

# Serve the main HTML page
@app.route("/")
def home():
    return render_template("index.html")

# API for Caesar Cipher
@app.route('/api/cipher', methods=['POST'])
def cipher():
    try:
        data = request.get_json()
        text = data.get('text', '')
        shift = int(data.get('shift', 3))
        mode = data.get('mode', 'encrypt')
        
        if mode not in ['encrypt', 'decrypt']:
            return jsonify({'success': False, 'error': 'Invalid mode'}), 400
        
        result = caesar_cipher(text, shift, mode)
        
        return jsonify({
            'success': True,
            'result': result,
            'original': text,
            'shift': shift,
            'mode': mode
        })
        
    except ValueError as e:
        return jsonify({'success': False, 'error': f'Invalid shift value: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
