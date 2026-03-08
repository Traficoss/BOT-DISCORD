import discord
from discord import app_commands

# ---------------- CONFIGURAÇÃO ----------------
TOKEN = "" # SEU TOKEN
GUILD_ID = 1461903016071532669
ID_CARGO_MOD = 1473638960289943624 # CARGO STAFF 
CANAL_RECRUTAMENTO_ID = 1474929472158564502 # CANAL DE REC
ID_CARGO_APROVADO = 1473638963112841247 # CARGO QUE A PESSOA FOR APROVADA DE RECRUTAMENTO
CANAL_EVENTO_ID = 1473639113331708097 # ID DO CANAL DE EVENTOS
CANAL_AUSENCIAS_ID = 1474919650616676544 # CANAL DE AUSENCIAS

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# ---------------- BOT ----------------
class NXMBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        guild = discord.Object(id=GUILD_ID)
        await self.tree.sync(guild=guild)
        print("Comandos slash sincronizados!")

    async def on_ready(self):
        print(f"Bot conectado como {self.user}")

bot = NXMBot()

# ---------------- RECRUTAMENTO ----------------
class FormularioNXM(discord.ui.Modal, title="RECRUTAMENTO - NXM"):
    nick = discord.ui.TextInput(label="Nick in-game", required=True)
    clans = discord.ui.TextInput(label="Clans passadas", style=discord.TextStyle.paragraph, required=True)
    fps = discord.ui.TextInput(label="FPS em Glad", required=True)
    video = discord.ui.TextInput(label="Link do vídeo jogando", style=discord.TextStyle.paragraph, required=False)

    async def on_submit(self, interaction: discord.Interaction):
        canal = bot.get_channel(CANAL_RECRUTAMENTO_ID)
        embed = discord.Embed(
            title="📋 Nova inscrição - RECRUTAMENTO NXM",
            color=discord.Color.purple()
        )
        embed.add_field(name="Nick in-game", value=self.nick.value, inline=False)
        embed.add_field(name="Clans passadas", value=self.clans.value, inline=False)
        embed.add_field(name="FPS em Glad", value=self.fps.value, inline=False)
        embed.add_field(name="Vídeo jogando", value=self.video.value or "Não enviado", inline=False)
        embed.set_footer(text=f"ID do usuário: {interaction.user.id}")

        view = BotoesAprovacaoNXM(interaction.user)
        await canal.send(embed=embed, view=view)
        await interaction.response.send_message("✅ Sua inscrição foi enviada!", ephemeral=True)

class BotoesAprovacaoNXM(discord.ui.View):
    def __init__(self, candidato):
        super().__init__(timeout=None)
        self.candidato = candidato

    @discord.ui.button(label="Aprovar", style=discord.ButtonStyle.success)
    async def aprovar(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            await self.candidato.send("# 🎉 Parabéns! Você foi aprovado no clã NXM!")
        except:
            pass
        guild = interaction.guild
        if guild:
            member = guild.get_member(self.candidato.id)
            if member:
                cargo = guild.get_role(ID_CARGO_APROVADO)
                if cargo:
                    await member.add_roles(cargo)
        await interaction.response.send_message("Candidato aprovado ✅", ephemeral=True)

    @discord.ui.button(label="Recusar", style=discord.ButtonStyle.danger)
    async def recusar(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            await self.candidato.send("❌ Sua inscrição foi recusada. Tente novamente futuramente.")
        except:
            pass
        await interaction.response.send_message("Candidato recusado ❌", ephemeral=True)

@bot.tree.command(name="recrutamento", description="Enviar formulário de recrutamento NXM")
async def recrutamento(interaction: discord.Interaction):
    await interaction.response.send_modal(FormularioNXM())

# ---------------- EVENTO ----------------
def apenas_mod_ou_superior():
    async def predicate(interaction: discord.Interaction):
        member = interaction.user
        guild = interaction.guild
        if not guild:
            return False
        roles_ids = [role.id for role in member.roles]
        return ID_CARGO_MOD in roles_ids or any(role.position >= guild.get_role(ID_CARGO_MOD).position for role in member.roles)
    return app_commands.check(predicate)

class ModalEvento(discord.ui.Modal, title="📅 Novo Evento - NXM"):
    servidor = discord.ui.TextInput(label="Servidor", required=True)
    horario = discord.ui.TextInput(label="Horário", required=True)
    qtd_por_clan = discord.ui.TextInput(label="Quantos por Clan", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        canal = bot.get_channel(CANAL_EVENTO_ID)
        if not canal:
            await interaction.response.send_message("❌ Canal de eventos não encontrado.", ephemeral=True)
            return

        embed = discord.Embed(
            title="📅 Evento NXM",
            color=discord.Color.green()
        )
        embed.add_field(name="Servidor", value=self.servidor.value, inline=False)
        embed.add_field(name="Horário", value=self.horario.value, inline=False)
        embed.add_field(name="Quantos por Clan", value=self.qtd_por_clan.value, inline=False)
        embed.set_footer(text=f"Organizador: {interaction.user}")

        view = ViewEvento()
        await canal.send(embed=embed, view=view)
        await interaction.response.send_message("✅ Evento enviado!", ephemeral=True)

class ViewEvento(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.usuarios_vao = []
        self.usuarios_nao_vao = []

    @discord.ui.button(emoji="✅", style=discord.ButtonStyle.success)
    async def vai(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user not in self.usuarios_vao:
            self.usuarios_vao.append(interaction.user)
        if interaction.user in self.usuarios_nao_vao:
            self.usuarios_nao_vao.remove(interaction.user)
        await interaction.response.send_message("✅ Sua presença foi confirmada! (Apenas você vê)", ephemeral=True)

    @discord.ui.button(emoji="❌", style=discord.ButtonStyle.danger)
    async def nao_vai(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user not in self.usuarios_nao_vao:
            self.usuarios_nao_vao.append(interaction.user)
        if interaction.user in self.usuarios_vao:
            self.usuarios_vao.remove(interaction.user)

        try:
            await interaction.user.send("❌ Você marcou que não vai. Qual o motivo?")
            await interaction.response.send_message("Sua ausência foi registrada, verifique seu PV.", ephemeral=True)
        except:
            await interaction.response.send_message("Não consegui enviar PV. Talvez seu DM esteja fechado.", ephemeral=True)

    @discord.ui.button(emoji="📋", style=discord.ButtonStyle.secondary)
    async def lista(self, interaction: discord.Interaction, button: discord.ui.Button):
        member = interaction.user
        guild = interaction.guild
        if not guild or ID_CARGO_MOD not in [r.id for r in member.roles]:
            await interaction.response.send_message("❌ Você não tem permissão.", ephemeral=True)
            return

        vao = ", ".join([u.mention for u in self.usuarios_vao]) or "Nenhum"
        nao = ", ".join([u.mention for u in self.usuarios_nao_vao]) or "Nenhum"

        embed = discord.Embed(title="📋 Lista de presença do evento", color=discord.Color.blue())
        embed.add_field(name="✅ Vai", value=vao, inline=False)
        embed.add_field(name="❌ Não Vai", value=nao, inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.tree.command(name="evento", description="Criar um evento do clã NXM")
@apenas_mod_ou_superior()
async def evento(interaction: discord.Interaction):
    await interaction.response.send_modal(ModalEvento())

# ---------------- RODAR BOT ----------------
bot.run(TOKEN)