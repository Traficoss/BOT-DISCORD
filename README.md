# 🤖 NXM Discord Bot

Bot de **Discord feito em Python usando discord.py** para gerenciamento de clã.

## 📋 Funções do Bot

- 📋 Sistema de **recrutamento com formulário**
- ✅ / ❌ **Aprovar ou recusar candidatos**
- 🎭 **Adicionar cargo automaticamente ao aprovado**
- 📅 **Sistema de criação de eventos**
- 👥 **Confirmação de presença em eventos**
- 📊 **Lista de quem vai ou não vai**

---

# 📦 Requisitos

Antes de usar o bot, instale:

- Python **3.9 ou superior**
- Biblioteca **discord.py**

Instalar dependência:

```bash
pip install discord.py
```

---

# 🚀 Como usar

## 1️⃣ Baixe ou clone o repositório

```bash
git clone https://github.com/seuusuario/nxm-discord-bot.git
```

## 2️⃣ Abra o arquivo

```
bot.py
```

## 3️⃣ Configure os dados do seu servidor

No topo do código existem algumas variáveis que **precisam ser alteradas**.

---

# ⚙️ Configuração

## 🔑 TOKEN

```python
TOKEN = ""
```

Coloque o **TOKEN do seu bot do Discord**.

Você pode pegar ele em:

https://discord.com/developers/applications

---

## 🏠 ID do servidor

```python
GUILD_ID = 1461903016071532669
```

ID do **servidor do Discord**.

---

## 🛡️ Cargo de Staff / Moderador

```python
ID_CARGO_MOD = 1473638960289943624
```

Cargo que poderá:

- Criar eventos
- Ver lista de presença

---

## 📋 Canal de Recrutamento

```python
CANAL_RECRUTAMENTO_ID = 1474929472158564502
```

Canal onde **as inscrições serão enviadas**.

---

## 🎭 Cargo do aprovado

```python
ID_CARGO_APROVADO = 1473638963112841247
```

Cargo que o jogador recebe quando **for aprovado no recrutamento**.

---

## 📅 Canal de Eventos

```python
CANAL_EVENTO_ID = 1473639113331708097
```

Canal onde os **eventos serão enviados**.

---

## ❌ Canal de Ausências

```python
CANAL_AUSENCIAS_ID = 1474919650616676544
```

Canal usado para **registrar ausências** (caso queira usar futuramente).

---

# 📋 Sistema de Recrutamento

Comando:

```
/recrutamento
```

Abre um formulário com:

- Nick in-game
- Clans passadas
- FPS em Glad
- Vídeo jogando

Depois de enviado:

- Vai para o **canal de recrutamento**
- Staff pode **Aprovar ou Recusar**

### ✔ Aprovar

- Envia mensagem no **PV do jogador**
- Adiciona o **cargo configurado**

### ❌ Recusar

- Envia mensagem informando que foi recusado.

---

# 📅 Sistema de Evento

Comando:

```
/evento
```

Apenas **staff pode usar**.

Abre formulário pedindo:

- Servidor
- Horário
- Quantos por clan

Depois o bot envia uma mensagem com botões:

```
✅ Vai
❌ Não vai
📋 Lista
```

---

## ✅ Vai

Confirma presença no evento.

---

## ❌ Não vai

O bot envia **DM pedindo motivo da ausência**.

---

## 📋 Lista

Apenas staff pode ver.

Mostra:

- Quem vai
- Quem não vai

---

# ▶️ Rodar o Bot

Execute:

```bash
python bot.py
```

Se tudo estiver correto aparecerá no terminal:

```
Comandos slash sincronizados!
Bot conectado como ...
```

---

# 🔐 Intents necessários

No painel do bot ative:

- MESSAGE CONTENT INTENT
- SERVER MEMBERS INTENT

No painel:

https://discord.com/developers/applications

---

# 📁 Estrutura recomendada

```
nxm-discord-bot
│
├── bot.py
├── README.md
└── requirements.txt
```

requirements.txt:

```
discord.py
```

---

# 💡 Melhorias futuras

Ideias que podem ser adicionadas:

- Sistema de **logs**
- **Banco de dados**
- Comando para **cancelar eventos**
- Sistema de **ausências automático**
- Painel de recrutamento com botão

---

# 👨‍💻 Autor

Projeto criado para gerenciamento de clã **NXM** no Discord.
