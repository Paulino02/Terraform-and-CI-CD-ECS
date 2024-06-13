# Desafio DevOps JR - Considerações Gerais

Você deve fazer um deploy automatizado de uma aplicação em ambiente nuvem da sua preferencia que atenda/resolva o problema proposto.

Considere como um projeto novo, pense em uma construção visando desde ao fluxo de desenvolvimento, publicação do artefato e deploy da aplicação.

Implemente apenas um ambiente de desenvolvimento, mas que seja preparado para diferentes ambientes de deploy (desenvolvimento e homologação) com configurações apropriadas.


# O Problema

O desafio que você deve resolver é a implantação da infraestrutura (obrigatório) usando ferramentas open source da sua preferência.

A aplicação será uma API REST cuja a função está disponível neste arquivo comment.py deste diretório. Através dela os internautas enviarão comentários em texto de uma máteria e acompanharão o que outras pessoas estão falando sobre o assunto em destaque. O funcionamento básico da API consiste em uma rota para inserção dos comentários e uma rota para listagem.

Os comandos de interação com a API são os seguintes:

* Criando e listando comentários por matéria

```
# matéria 1
curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"alice@example.com","comment":"first post!","content_id":1}'
curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"alice@example.com","comment":"ok, now I am gonna say something more useful","content_id":1}'
curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"bob@example.com","comment":"I agree","content_id":1}'

# matéria 2
curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"bob@example.com","comment":"I guess this is a good thing","content_id":2}'
curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"charlie@example.com","comment":"Indeed, dear Bob, I believe so as well","content_id":2}'
curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"eve@example.com","comment":"Nah, you both are wrong","content_id":2}'

# listagem matéria 1
curl -sv host/api/comment/list/1

# listagem matéria 2
curl -sv host/api/comment/list/2
```


# O que será avaliado na sua solução?

* Automação da infra, provisionamento dos hosts/Containers (Dockerfile)

* Pipeline de deploy automatizado CI/CD -  (Pode utilizar o seu repositório pessoal para registrar os commits e a construção da Pipeline)

* Monitoramento dos serviços e métricas da aplicação - Desejável

* Aplicar conceitos cloud native - Diferencial 

# Dicas

Será avaliado a maneira em que você executa as atividades deste desafio. Crie um arquivo chamado *DOCS.md* e insira o passo a passo para construir esta solução. Com as possibilidades, opcões e boas práticas.

Automatize o máximo possível;

Em caso de dúvidas, pergunte.
