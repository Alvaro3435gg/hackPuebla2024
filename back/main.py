from flask import Flask, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)  # Permitir solicitudes CORS desde cualquier origen

# Configura tu cliente OpenAI
client = OpenAI(api_key="aqui va la api")

@app.route('/get_response')
def get_response():
    # Obtén la respuesta del modelo
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "responde unicamente con un si o con un no"},
            {"role": "user", "content": "las papas son tuberculos"}
        ]
    )
    content = completion.choices[0].message.content
    return jsonify({'response': content})

if __name__ == '__main__':
    app.run(debug=True)
