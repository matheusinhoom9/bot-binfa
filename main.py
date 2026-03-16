import os
import discord
from discord.ext import commands
from discord.ui import View, Button

# Prefixo do bot
bot = commands.Bot(command_prefix="!")

# -------------------------------
# COMANDO: !informar
# -------------------------------
@bot.command()
async def informar(ctx):
    embed = discord.Embed(
        title="<:BInfA:1462094511176945786> Departamento do Batalhão de Infantaria da Aeronáutica",
        description=(
            "Bem-vindo ao canal de informações oficiais da Infantaria da Aeronáutica.\n\n"
            "Aqui estão disponíveis documentos, regras e links importantes sobre o nosso grande BInfA.\n\n"
            "Leiam atentamente cada detalhe das informações, garantindo o correto entendimento e evitando possíveis divergências."
        ),
        color=0x1F8B4C  # Verde militar
    )

    # Imagem do embed
    embed.set_image(url="https://cdn.discordapp.com/attachments/1429653674908450886/1481059237697163274/lv_0_20260310193832.jpg?ex=69b6ca7&is=69b53b27&hm=ab1626e3d9749dcc0e8cfadb8a6aec026e001ea7865390a1ace296f7309cebc7&")

    # Botões com links
    view = View()

    view.add_item(Button(
        label="📊 Planilha de Atividade",
        url="https://docs.google.com/spreadsheets/d/1LfR6hYtoXSk0dxegwX5t6SPS5-zZmzIasWAWJ8fQzOo/edit?usp=drivesdk",
        style=discord.ButtonStyle.link
    ))

    view.add_item(Button(
        label="📜 Regimento Interno",
        url="https://docs.google.com/document/d/1kwbf5gOn8i44x-YDUgp6YJ7tW_aQVMq6cM-PwZ7uR8k/edit?usp=drivesdk",
        style=discord.ButtonStyle.link
    ))

    view.add_item(Button(
        label="🏹 Etapa do CApI",
        url="https://docs.google.com/document/d/13w5kYRwmM6F0dVxpmfUZrw1H9R-YZaGv0BpTEfnDwoQ/edit?usp=drivesdk",
        style=discord.ButtonStyle.link
    ))

    view.add_item(Button(
        label="📘 Apostila dos Alunos",
        url="https://docs.google.com/document/d/1THzSvrt9UiFMQ-IBU-njq4XbxoY31mlo38ch9UsGvPg/edit?usp=drivesdk",
        style=discord.ButtonStyle.link
    ))

    view.add_item(Button(
        label="🏅 Medalhas",
        url="https://docs.google.com/document/d/17EIg0iTeY8kAbTSa0IHqGmV5NPombYXSoKrOz3nFPNo/edit?usp=drivesdk",
        style=discord.ButtonStyle.link
    ))

    view.add_item(Button(
        label="📄 Documento Informacional",
        url="https://docs.google.com/document/d/1k7Whq_nrlrXhkjtVcfOR7KHuodS2JLYoPKRDe5a5qzA/edit?usp=drivesdk",
        style=discord.ButtonStyle.link
    ))

    embed.set_footer(text="Painel de documentos oficiais do Batalhão de Infantaria da Aeronáutica.")

    await ctx.send(embed=embed, view=view)

# -------------------------------
# COMANDO DE TESTE: !ping
# -------------------------------
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# -------------------------------
# AQUI É O TOKEN
# -------------------------------
token = os.getenv("DISCORD_TOKEN")
bot.run(token)