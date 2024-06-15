# Infraestrutura
Utilizei o Terraform para subir minha infra na AWS.
Serviços que utilizei: IAM, VPC, ECR, ECS, Application Load Balancer (ALB) e Target Group.

# Dockerfile
Criei um dockerfile para Containerizar a API Flask do arquivo comment.py
Tive Problemas com as dependências, então fui em busca de uma solução e deu certo.

# CI/CD 
Utilizei o GitHub Actions no meu CI-CD, no CI ele pega o arquivo dockerfile para criar a imagem docker e
em seguida, no CD, ele envia essa imagem para o ECR da aws e então vai pra o container no ECS que já está configurado
pelo Terraform.

# ALB
Configurei o ALB no terraform para acessar a API, containerizada no ECS, via browser. Esse método é escalável e
fornece alta disponibilidade para aplicações containerizadas na AWS.

# Dificuldades
Tive problemas com a task-definition do ECS porque estava faltando uma permissão IAM que não tinha sido posta no código
do Terraform. Também tive um pouco de dificuldade inicial em entender o funcionamento da API, visto que nunca tinha estudado
API, mas logo consegui entender.

# Testes
Utilizei os seguintes comando para testar a interação com a API.

#### Criando e listando comentários por matéria
- matéria 1

curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"alice@example.com","comment":"first post!","content_id":1}'

curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"alice@example.com","comment":"ok, now I am gonna say something more useful","content_id":1}'

curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"bob@example.com","comment":"I agree","content_id":1}'

- matéria 2

curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"bob@example.com","comment":"I guess this is a good thing","content_id":2}'

curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"charlie@example.com","comment":"Indeed, dear Bob, I believe so as well","content_id":2}'

curl -sv host/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"eve@example.com","comment":"Nah, you both are wrong","content_id":2}'

- listagem matéria 1

curl -sv host/api/comment/list/1

- listagem matéria 2

curl -sv host/api/comment/list/2

# Monitoramento dos serviços e métricas da aplicação
Por padrão, o ECS oferece monitoramento básico e coleta de métricas para containers que estão rodando uma aplicação. 
Essas métricas são coletadas e disponibilizadas através do Amazon CloudWatch, o serviço de monitoramento e gerenciamento de logs da AWS.
Aqui estão algumas das métricas básicas que o ECS coleta:

- CPU Utilization: Utilização da CPU pelos containers.

- Memory Utilization: Utilização de memória pelos containers.

- Disk I/O: Operações de entrada/saída de disco.

- Network I/O: Tráfego de rede (dados enviados e recebidos).
