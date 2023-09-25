<h1 align="center">Mãos Amigas</h1>
<p>
O sistema "Mãos Amigas" foi desenvolvido como parte de um projeto acadêmico, com o objetivo de aplicar e aprimorar os conhecimentos adquiridos durante o curso. É importante ressaltar que, por se tratar de um projeto acadêmico, o sistema pode apresentar algumas limitações, inconsistências e funcionalidades que ainda não foram totalmente implementadas.
</p>
<p>
O principal propósito do sistema é facilitar o processo de doação, fornecendo uma plataforma para que instituições que necessitam de auxílio possam cadastrar suas solicitações. Por meio do sistema, os usuários têm a oportunidade de verificar as diferentes possibilidades de doação disponíveis e, se desejarem, podem fazer suas doações presencialmente.
</p>
<p>
No entanto, é importante estar ciente de que o sistema ainda está em desenvolvimento e pode passar por atualizações e melhorias no futuro. A equipe responsável pelo projeto está trabalhando continuamente para aprimorar a funcionalidade e a usabilidade do sistema, garantindo uma experiência cada vez melhor para os usuários.
</p>
<p>
Agradecemos pela compreensão e colaboração durante essa fase de implementação do sistema "Mãos Amigas".
</p>
<h4 align="center"> 
	🚧  Status 🚀 Refatorando o código  🚧
</h4>

<!-- <h1 align="center">
  <img alt="Imagem de inicio" title="#ControleDeEstoque" src="staticFile/imagens/Apresentação.png" />
</h1> -->
<p text-align="justify">Este repositório tem foco, na criação de uma aplicação de doações, interligado a um banco de dados provido pelo próprio Framework Django facilitando dessa forma a manipulação de seus dados.</p>
<p text-align="justify">Este projeto faz parte do meu portfólio pessoal, então, ficarei feliz caso você forneça algum feedback, código, estrutura, funcionalidade ou qualquer melhoria que você possa relatar para melhora-lo.Você pode usar este projeto como quiser, seja para estudar, fazer melhorias, você quem manda!.</p>

<blockquote>
Este é um projeto totalmente grátis!
</blockquote>

### 🏁 Features

- [x] Cadastro de Usuário Físico
- [x] Cadastro de Usuário Jurídico
- [x] Cadastro de Doações/Solitações
- [x] Listagem de Solicitações
- [x] Listagem de Instituições
- [x] Listagem de Instituições por cidade
- [x] Visualizar usuário Jurídico
- [x] Visualizar usuário Físico
- [x] Visualizar doação/solicitação
- [x] Visualizar doação/solicitação por categoria
- [x] Contatar responsável pela doação/solicitação para doar
- [x] Editar Usuário Físico
- [x] Editar Usuário Jurídico
- [x] Editar doação/solicitação
- [x] Painel Administrativo para usuários jurídicos informando sobre suas doações/solicitações
- [x] Relatório a respeito da doação/solicitação, informando quantidade de acessos total e do mês atual.
- [x] Painel Administrativo de contatos que cada doação/solicitação obteve
- [x] Inativar Solicitação
- [x] Recuperação de Senha
- [x] Home informando sobre o projeto, membros e as solicitações mais acessadas

### 🛠 Tecnologias
<p>As seguintes ferramentas foram usadas na construção do projeto:</p>

- [Django](https://www.djangoproject.com/start/)
- [Bootstrap](https://getbootstrap.com/)


<h1>Rodando o projeto</h1>
<h4>Clonando o projeto</h4>
<p>Dentro da pasta onde o projeto ficará armazenado, abra o terminal.</p>


<h4>Linux</h4>
<blockquote>
  Observação: Foi utilizado a distro Linux Mint(versão 20.1), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!
</blockquote>
<h4>Linux</h4>

``` 
sudo apt-get install python3-venv
```

<h4>Preparando o Projeto</h4>

```
python3 -m venv env
source env/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations users
python manage.py makemigrations base
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```

### Autor
---


 <img style="border-radius: 50%;" src="static/images/undraw_female_avatar_efig.svg" width="100px;" alt=""/>
 <sub><b>Camila Adriana</b></sub></a> <a href="www.linkedin.com/in/camila-adriana-gomes-de-jesus-04767b1ba" title="Foto de perfil"></a><br>
Feito com ❤️ por Camila Adriana 👋🏽 Entre em contato!

[![Twitter Badge](https://img.shields.io/badge/-@camilaA58109563-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/Camila)](https://twitter.com/CamilaA58109563?s=09) [![Linkedin Badge](https://img.shields.io/badge/-Camila-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/Camila/)](https://www.linkedin.com/in/camila-adriana-gomes-de-jesus-04767b1ba/) 