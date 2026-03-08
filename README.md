🤖 NXM Discord Bot

Bot de Discord feito em Python usando discord.py para gerenciamento de clã.

Ele possui:

📋 Sistema de recrutamento com formulário

✅ / ❌ Aprovar ou recusar candidatos

🎭 Adicionar cargo automaticamente ao aprovado

📅 Sistema de criação de eventos

👥 Confirmação de presença em eventos

📊 Lista de quem vai ou não vai

📦 Requisitos

Antes de usar o bot, instale:

Python 3.9+

Biblioteca discord.py

Instalar dependência:

pip install discord.py
🚀 Como usar

Baixe ou clone o repositório

git clone https://github.com/seuusuario/nxm-discord-bot.git

Abra o arquivo:

bot.py

Edite as configurações no topo do código.

⚙️ Configuração

No início do código existem algumas variáveis que precisam ser alteradas.

TOKEN = "" 
🔑 TOKEN

Coloque o token do seu bot do Discord.

Você pega em:

Discord Developer Portal
https://discord.com/developers/applications

GUILD_ID = 1461903016071532669
🏠 GUILD_ID

ID do servidor do Discord onde o bot será usado.

ID_CARGO_MOD = 1473638960289943624
🛡️ ID_CARGO_MOD

Cargo de moderador/staff.

Quem tiver esse cargo poderá:

Criar eventos

Ver lista de presença

CANAL_RECRUTAMENTO_ID = 1474929472158564502
📋 CANAL_RECRUTAMENTO_ID

Canal onde as inscrições de recrutamento serão enviadas.

ID_CARGO_APROVADO = 1473638963112841247
🎭 ID_CARGO_APROVADO

Cargo que o jogador recebe quando for aprovado no recrutamento.

CANAL_EVENTO_ID = 1473639113331708097
📅 CANAL_EVENTO_ID

Canal onde os eventos serão enviados.

CANAL_AUSENCIAS_ID = 1474919650616676544
❌ CANAL_AUSENCIAS_ID

Canal para registrar ausências (caso queira usar futuramente).

📋 Sistema de Recrutamento

Comando:

/recrutamento

Abre um formulário com:

Nick in-game

Clans passadas

FPS em Glad

Vídeo jogando

Depois de enviado:

Vai para o canal de recrutamento

Staff pode Aprovar ou Recusar

✔ Aprovar

Envia mensagem no PV do jogador

Adiciona o cargo configurado

❌ Recusar

Envia mensagem no PV informando que foi recusado

📅 Sistema de Evento

Comando:

/evento

Apenas staff pode usar.

Abre formulário pedindo:

Servidor

Horário

Quantos por clan

Depois o bot envia uma mensagem com botões:

✅ Vai
❌ Não vai
📋 Lista

✅ Vai

Confirma presença no evento.

❌ Não vai

O bot envia DM pedindo motivo da ausência.

📋 Lista

Apenas staff pode ver.

Mostra:

Quem vai

Quem não vai

▶️ Rodar o Bot

Execute:

python bot.py

Se estiver tudo correto aparecerá:

Comandos slash sincronizados!
Bot conectado como ...
🔐 Intents necessários

No painel do bot ative:

MESSAGE CONTENT INTENT

SERVER MEMBERS INTENT

No:

Discord Developer Portal

📁 Estrutura recomendada
nxm-discord-bot
│
├── bot.py
├── README.md
└── requirements.txt

requirements.txt:

discord.py
