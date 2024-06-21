from flask import Flask, request, jsonify
import werkzeug

# Atualizações para compatibilidade
werkzeug.cached_property = werkzeug.utils.cached_property

app = Flask(__name__)

# Armazenar os comentários em um dicionário onde a chave é o ID da matéria
comments = {}

@app.route("/")
def hello():
   return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD com AWS e Terraform</title>
    <style>
        body {
            background-color: navy;
            color: white;
            font-family: Arial, sans-serif;
            padding: 20px;
            margin: 0; /* Remove margens padrão */
        }
        .container {
            max-width: 800px; /* Define a largura máxima do conteúdo */
            margin: 0 auto; /* Centraliza o conteúdo na tela */
        }
        h1 {
            padding: 10px;
            border-radius: 5px;
        }
        img {
            margin-right: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>CI/CD (Continuous Integration/Continuous Deployment) com infraestrutura na AWS via Terraform.</h1>
        <h1>Tecnologias que utilizei nesse projeto:</h1>   
        <h1>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" height="50" width="50" title="Linux">
            <img src="https://raw.githubusercontent.com/Paulino02/logos.svg/master/amazon-web-services-2.svg" height="50" width="50" title="AWS">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original-wordmark.svg" height="50" width="50" title="Docker">
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" height="50" width="50" title="Python">
            <img src="https://raw.githubusercontent.com/Paulino02/logos.svg/master/terraformio-icon.svg" height="50" width="50" title="Terraform">
        </h1>
    </div>
</body>
</html>
'''

@app.route('/api/comment/new', methods=['POST'])
def create_comment():
    data = request.get_json()
    email = data.get('email')
    comment = data.get('comment')
    content_id = data.get('content_id')

    if not email or not comment or content_id is None:
        return jsonify({'error': 'Missing required fields'}), 400

    if content_id not in comments:
        comments[content_id] = []

    comments[content_id].append({'email': email, 'comment': comment})
    return jsonify({'message': 'Comment created successfully'}), 201

@app.route('/api/comment/list/<int:content_id>', methods=['GET'])
def list_comments(content_id):
    if content_id not in comments:
        return jsonify({'error': 'Content not found'}), 404

    return jsonify(comments[content_id])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

