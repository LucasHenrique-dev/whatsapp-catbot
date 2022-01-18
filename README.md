# :cat: CatBot
![image](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## :dart: Projeto de estudo sobre chatbot

O chatbot criado neste projeto é bem básico e possui respostas simples para entradas de valores simples. Foi usado o [Twilio](https://www.twilio.com/pt-br/) para se obter o número de celular do bot e [ngrok](https://ngrok.com) para criação do servidor onde o bot foi hospedado.
Palavras chaves que fazem o bot responder:
- gato: Bot responde com uma foto aleatória de um gato
- bom dia/boa tarde/boa noite: Bot responde a saudação com uma foto de gato
- meow ou miau: Bot responde com um emoji de gato
- segredo: Bot ~~responde com~~... 🐾🐾 😼

Qualquer outra mensagem o bot ficará nervoso e responderá apenas com um "meow"

## 🚀 Usando o CatBot

Para usar o CatBot é necessáio clonar o repositório:

* Basta digitar ` git clone https://github.com/LucasHenrique-dev/whatsapp-catbot.git` no terminal.

Depois seguir os passos de preparação do ambiente (atualmente o bot não possui um servidor próprio, por isso para usá-lo será necessário criar uma conta na Twilio e usar um servidor para hospedar o bot)

## ☕ Preparando o Ambiete

Para usar catbot, siga estas etapas:

1. Faça uma conta na Twilio:
    * Acesse o site: https://www.twilio.com/pt-br/.
1. Criada a conta chega-se a hora de registrar um número para o bot:
    * Acesse o guia da Twilio para o whatsapp sandbox: https://www.twilio.com/console/sms/whatsapp/learn
1. Garantindo o sucesso das etapas anteriores hora de baixar o ngrok:
   * Acesse o site: https://ngrok.com
1. Possuindo as ferramentas está na hora de criar o ambiente virtual:
   1. Utilizando o terminal no mesmo diretório em que se encontra o projeto do catbot, digite os seguintes códigos:

      Criação do ambiente virtual:
      ```shell
      python -m venv whatsapp-bot-venv
      ```
      Ativação do ambiente:
      ```shell
      whatsapp-bot-venv\Scripts\activate
      ```
      Instalação, no ambiente, das dependências necessárias para o projeto:
      ```shell
      pip install twilio flask
      ```
      Ativação do bot:
      ```shell
      python chat_bot.py
      ```
1. Agora é ativar o servidor do ngrok:
   1. Extraia os arquivos baixados no passo 3
   2. Execute _ngrok.exe_
   3. Nesse terminal digite `ngrok http porta` (_porta_ é a porta onde o bot está rodando no passo 4; exemplo: porta 5000 então digite 5000)
   4. Será gerado um link https terminado com _.ngork.io_, ele será necessário para o passo final
1. Finalmente, vá nas configurações do whatsapp sandbox e ponha o link do passo anterior no campo _WHEN A MESSAGE COMES IN_, salve e aproveite o bot!

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE) para mais detalhes.

[⬆ Voltar ao topo](#cat-catbot)<br>
