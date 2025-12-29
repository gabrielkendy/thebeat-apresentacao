"""
═══════════════════════════════════════════════════════════════════
AUTOMAÇÃO MLABS - THE BEAT LIFE CLUB
Script de upload automático de posts no Instagram via MLabs
═══════════════════════════════════════════════════════════════════
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
from datetime import datetime, timedelta

# ═══════════════════════════════════════════════════════════════════
# CONFIGURAÇÕES
# ═══════════════════════════════════════════════════════════════════

# Caminho base dos posts
BASE_PATH = r"C:\Users\Gabriel\Downloads\INSTAGRAM BEAT CLUB\POSTS_ORGANIZADOS"

# Credenciais MLabs (VOCÊ PRECISA PREENCHER)
MLABS_EMAIL = ""  # ⬅️ COLOQUE SEU EMAIL AQUI
MLABS_SENHA = ""  # ⬅️ COLOQUE SUA SENHA AQUI

# Calendário de publicações (Janeiro 2025)
CALENDARIO = [
    {"data": "2025-01-06", "hora": "07:30", "post": 1},
    {"data": "2025-01-08", "hora": "12:30", "post": 2},
    {"data": "2025-01-10", "hora": "18:30", "post": 3},
    {"data": "2025-01-13", "hora": "07:30", "post": 4},
    {"data": "2025-01-15", "hora": "12:30", "post": 5},
    {"data": "2025-01-17", "hora": "18:30", "post": 6},
    {"data": "2025-01-20", "hora": "07:30", "post": 7},
    {"data": "2025-01-22", "hora": "12:30", "post": 8},
    {"data": "2025-01-24", "hora": "18:30", "post": 9},
    {"data": "2025-01-27", "hora": "07:30", "post": 10},
    {"data": "2025-01-29", "hora": "12:30", "post": 11},
    {"data": "2025-01-31", "hora": "18:30", "post": 12},
    {"data": "2025-02-03", "hora": "07:30", "post": 13},
]

# Lista de posts organizados
POSTS = [
    {"numero": 1, "pasta": "POST_01_CARROSSEL_Ecosystem", "tipo": "carrossel"},
    {"numero": 2, "pasta": "POST_02_VIDEO_BannerStreet", "tipo": "video"},
    {"numero": 3, "pasta": "POST_03_CARROSSEL_Hormonios", "tipo": "carrossel"},
    {"numero": 4, "pasta": "POST_04_VIDEO_BeatNike", "tipo": "video"},
    {"numero": 5, "pasta": "POST_05_CARROSSEL_Ozempic", "tipo": "carrossel"},
    {"numero": 6, "pasta": "POST_06_VIDEO_Helicoptero", "tipo": "video"},
    {"numero": 7, "pasta": "POST_07_CARROSSEL_Sauna", "tipo": "carrossel"},
    {"numero": 8, "pasta": "POST_08_VIDEO_Kettlebell", "tipo": "video"},
    {"numero": 9, "pasta": "POST_09_CARROSSEL_BemEstar", "tipo": "carrossel"},
    {"numero": 10, "pasta": "POST_10_VIDEO_Lapidando", "tipo": "video"},
    {"numero": 11, "pasta": "POST_11_VIDEO_RedBull", "tipo": "video"},
    {"numero": 12, "pasta": "POST_12_VIDEO_Cinematic", "tipo": "video"},
    {"numero": 13, "pasta": "POST_13_VIDEO_BannerMockup", "tipo": "imagem"},
]


# ═══════════════════════════════════════════════════════════════════
# FUNÇÕES AUXILIARES
# ═══════════════════════════════════════════════════════════════════

def ler_legenda(pasta_post):
    """Lê o arquivo LEGENDA.txt da pasta do post"""
    caminho_legenda = os.path.join(BASE_PATH, pasta_post, "LEGENDA.txt")
    try:
        with open(caminho_legenda, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            # Remove o cabeçalho decorativo e retorna só a legenda
            linhas = conteudo.split('\n')
            legenda_limpa = []
            pular = True
            for linha in linhas:
                if linha.startswith('#TheBeat'):
                    pular = False
                if not pular and not linha.startswith('━'):
                    legenda_limpa.append(linha)
            return '\n'.join(legenda_limpa).strip()
    except Exception as e:
        print(f"❌ Erro ao ler legenda de {pasta_post}: {e}")
        return ""


def obter_arquivos_post(pasta_post, tipo):
    """Obtém lista de arquivos de mídia da pasta do post"""
    caminho_pasta = os.path.join(BASE_PATH, pasta_post)
    arquivos = []
    
    extensoes_validas = ['.mp4', '.png', '.jpg', '.jpeg']
    
    for arquivo in os.listdir(caminho_pasta):
        # Ignora LEGENDA.txt e pastas PSD
        if arquivo == "LEGENDA.txt" or arquivo == "PSD":
            continue
        
        # Verifica extensão
        ext = os.path.splitext(arquivo)[1].lower()
        if ext in extensoes_validas:
            caminho_completo = os.path.join(caminho_pasta, arquivo)
            arquivos.append(caminho_completo)
    
    # Ordena alfabeticamente para manter sequência
    arquivos.sort()
    return arquivos


def aguardar_elemento(driver, by, value, timeout=10):
    """Aguarda elemento aparecer na página"""
    try:
        elemento = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return elemento
    except Exception as e:
        print(f"⚠️ Timeout aguardando elemento: {value}")
        return None


# ═══════════════════════════════════════════════════════════════════
# FUNÇÕES PRINCIPAIS
# ═══════════════════════════════════════════════════════════════════

def iniciar_navegador():
    """Inicializa o Chrome com Selenium"""
    print("🌐 Iniciando navegador Chrome...")
    
    chrome_options = Options()
    # Usar perfil do Chrome existente (mantém login)
    chrome_options.add_argument(r"user-data-dir=C:\Users\Gabriel\AppData\Local\Google\Chrome\User Data")
    chrome_options.add_argument("--profile-directory=Default")
    
    # Outras opções úteis
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def fazer_login_mlabs(driver):
    """Faz login no MLabs"""
    print("🔐 Acessando MLabs...")
    
    driver.get("https://app.mlabs.com.br/login")
    time.sleep(3)
    
    # Se já estiver logado, pula
    if "dashboard" in driver.current_url or "home" in driver.current_url:
        print("✅ Já está logado!")
        return True
    
    # Tenta fazer login
    try:
        email_input = aguardar_elemento(driver, By.NAME, "email")
        senha_input = aguardar_elemento(driver, By.NAME, "password")
        
        if email_input and senha_input:
            email_input.send_keys(MLABS_EMAIL)
            senha_input.send_keys(MLABS_SENHA)
            
            # Procura botão de login
            botao_login = driver.find_element(By.XPATH, "//button[@type='submit']")
            botao_login.click()
            
            time.sleep(5)
            print("✅ Login realizado!")
            return True
    except Exception as e:
        print(f"⚠️ Erro no login: {e}")
        print("👉 Por favor, faça login manualmente e pressione ENTER quando estiver logado...")
        input()
        return True
    
    return False
