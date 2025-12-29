# 🚀 THE BEAT LIFE CLUB - DEPLOY AUTOMÁTICO GITHUB PAGES

## COPIE E COLE ESTE BLOCO INTEIRO NO POWERSHELL:

```powershell
# ══════════════════════════════════════════════════════════════════
# DEPLOY AUTOMÁTICO - THE BEAT LIFE CLUB
# ══════════════════════════════════════════════════════════════════

Write-Host "
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     THE BEAT LIFE CLUB - SUBINDO DASHBOARD ONLINE            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
" -ForegroundColor Cyan

# 1. Abrir GitHub para criar repositório
Write-Host "`n[1/4] Abrindo GitHub..." -ForegroundColor Yellow
Start-Process "https://github.com/new"
Start-Sleep -Seconds 3

Write-Host "`n╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  NO GITHUB QUE ABRIU, FAÇA ISSO:                             ║" -ForegroundColor Cyan
Write-Host "║                                                              ║" -ForegroundColor Cyan
Write-Host "║  1. Repository name: thebeat-apresentacao                    ║" -ForegroundColor White
Write-Host "║  2. Marque: Public                                           ║" -ForegroundColor White
Write-Host "║  3. Clique: Create repository                                ║" -ForegroundColor White
Write-Host "║                                                              ║" -ForegroundColor Cyan
Write-Host "║  QUANDO TERMINAR, PRESSIONE ENTER AQUI...                    ║" -ForegroundColor Yellow
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Read-Host

# 2. Pegar URL do repositório
Write-Host "`n[2/4] Cole a URL do repositório que foi criado:" -ForegroundColor Yellow
Write-Host "Exemplo: https://github.com/seu-usuario/thebeat-apresentacao" -ForegroundColor Gray
$repoUrl = Read-Host "URL"

# 3. Configurar Git e fazer push
Write-Host "`n[3/4] Enviando arquivos para o GitHub..." -ForegroundColor Yellow
cd "C:\Users\Gabriel\Downloads\INSTAGRAM BEAT CLUB\deploy_online"

git remote add origin $repoUrl
git branch -M main
git push -u origin main

Write-Host "`n✅ Arquivos enviados!" -ForegroundColor Green

# 4. Ativar GitHub Pages
Write-Host "`n[4/4] Abrindo configurações do GitHub Pages..." -ForegroundColor Yellow
$settingsUrl = $repoUrl.Replace(".git", "") + "/settings/pages"
Start-Process $settingsUrl
Start-Sleep -Seconds 3

Write-Host "`n╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  NA PÁGINA QUE ABRIU (Settings > Pages):                     ║" -ForegroundColor Cyan
Write-Host "║                                                              ║" -ForegroundColor Cyan
Write-Host "║  1. Em 'Source', selecione: main                             ║" -ForegroundColor White
Write-Host "║  2. Clique em: Save                                          ║" -ForegroundColor White
Write-Host "║  3. Aguarde 1-2 minutos                                      ║" -ForegroundColor White
Write-Host "║  4. Atualize a página                                        ║" -ForegroundColor White
Write-Host "║  5. COPIE O LINK que aparecer no topo                        ║" -ForegroundColor White
Write-Host "║                                                              ║" -ForegroundColor Cyan
Write-Host "║  O link será algo como:                                      ║" -ForegroundColor Gray
Write-Host "║  https://seu-usuario.github.io/thebeat-apresentacao          ║" -ForegroundColor Gray
Write-Host "║                                                              ║" -ForegroundColor Cyan
Write-Host "║  ESSE É O LINK PERMANENTE PARA ENVIAR AO CLIENTE! 🎯         ║" -ForegroundColor Green
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan

Write-Host "`n✅ DEPLOY CONCLUÍDO COM SUCESSO!" -ForegroundColor Green
Write-Host "`nO dashboard ficará online PERMANENTEMENTE no GitHub Pages." -ForegroundColor White
Write-Host "Link será: $repoUrl".Replace("github.com", "github.io").Replace(".git", "") -ForegroundColor Cyan

Read-Host "`nPressione ENTER para finalizar"
```

═══════════════════════════════════════════════════════════════════

## OU SE PREFERIR PASSO A PASSO MANUAL:

### PASSO 1: Criar Repositório no GitHub

1. Acesse: https://github.com/new
2. Nome: `thebeat-apresentacao`
3. Marque: **Public**
4. Clique: **Create repository**

### PASSO 2: Copiar comandos Git

Na página que abrir, copie a URL que aparece tipo:
`https://github.com/SEU-USUARIO/thebeat-apresentacao.git`

### PASSO 3: Execute no PowerShell:

```powershell
cd "C:\Users\Gabriel\Downloads\INSTAGRAM BEAT CLUB\deploy_online"
git remote add origin https://github.com/SEU-USUARIO/thebeat-apresentacao.git
git branch -M main
git push -u origin main
```

(Pode pedir login do GitHub - use suas credenciais)

### PASSO 4: Ativar GitHub Pages

1. Vá em: `https://github.com/SEU-USUARIO/thebeat-apresentacao/settings/pages`
2. Em **Source**, selecione: `main`
3. Clique em: **Save**
4. Aguarde 1-2 minutos
5. Atualize a página
6. **COPIE O LINK** que aparecer no topo verde

### LINK FINAL:

Será algo como:
`https://SEU-USUARIO.github.io/thebeat-apresentacao`

**ESSE É O LINK PERMANENTE! 🎯**

═══════════════════════════════════════════════════════════════════

## VANTAGENS GITHUB PAGES:

✅ **PERMANENTE** (não cai em 1 hora)
✅ **GRÁTIS** para sempre
✅ **RÁPIDO** (CDN global)
✅ **PROFISSIONAL**
✅ **HTTPS** automático
✅ Você pode **ATUALIZAR** depois se precisar

═══════════════════════════════════════════════════════════════════

## ALTERNATIVA RÁPIDA: GOOGLE DRIVE

Se quiser algo SUPER rápido (mas menos profissional):

1. Faça ZIP da pasta `deploy_online`
2. Suba no Google Drive
3. Compartilhe como "Qualquer pessoa com o link"
4. Envie o link pro cliente baixar e abrir o HTML localmente

═══════════════════════════════════════════════════════════════════

## 📧 MENSAGEM PARA O CLIENTE:

```
Olá!

Segue a apresentação completa do calendário editorial de Janeiro 2025:

🔗 Link: https://SEU-USUARIO.github.io/thebeat-apresentacao

📊 Conteúdo completo:
- 13 posts com todas as mídias
- Carrosseis interativos
- Vídeos em HD
- Legendas completas
- Calendário visual

A apresentação está online permanentemente e pode ser acessada 
de qualquer dispositivo (desktop, tablet, mobile).

Abraço,
Kendy
```

═══════════════════════════════════════════════════════════════════

## ESCOLHA SUA OPÇÃO:

**A)** Executar script automático do PowerShell (copiar/colar)
**B)** Seguir passo a passo manual
**C)** Fazer ZIP e subir no Google Drive

═══════════════════════════════════════════════════════════════════