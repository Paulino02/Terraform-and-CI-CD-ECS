# Infraestrutura
Utilizei o Terraform para subir minha infra na AWS.
Serviços que utilizei: IAM, VPC, ECR, ECS, Application Load Balancer (ALB) E Target Group.

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

# Dificuldadea
Tive problemas com a task-definition do ECS porque estava faltando uma permissão IAM que não tinha sido posta no código
do Terraform. Também tive um pouco de dificuldade inicial em entender o funcionamento da API, visto que nunca tinha estudado
API, mas logo consegui entender.
