@echo off
chcp 65001 >nul
echo.
echo ═══════════════════════════════════════════════════════════════════
echo     THE BEAT LIFE CLUB - DEPLOY AUTOMÁTICO GITHUB PAGES
echo ═══════════════════════════════════════════════════════════════════
echo.

cd /d "C:\Users\Gabriel\Downloads\INSTAGRAM BEAT CLUB\deploy_online"

echo [1/3] Configurando Git...
git config --global user.email "kendy@thebeat.com"
git config --global user.name "Gabriel Kendy"

echo.
echo [2/3] Adicionando arquivos...
git add .
git commit -m "The Beat Life Club - Apresentacao Janeiro 2025"

echo.
echo [3/3] Fazendo upload para GitHub...
git remote remove origin 2>nul
git remote add origin https://github.com/gabrielkendy/thebeat-apresentacao.git
git branch -M main
git push -u origin main

echo.
echo ═══════════════════════════════════════════════════════════════════
echo ✅ UPLOAD CONCLUÍDO!
echo ═══════════════════════════════════════════════════════════════════
echo.
echo Agora faça isto:
echo.
echo 1. Abra: https://github.com/gabrielkendy/thebeat-apresentacao/settings/pages
echo 2. Em "Branch", selecione: main
echo 3. Clique: Save
echo 4. Aguarde 2 minutos
echo.
echo Seu link será:
echo 🔗 https://gabrielkendy.github.io/thebeat-apresentacao
echo.
echo ═══════════════════════════════════════════════════════════════════
echo.
pause

start https://github.com/gabrielkendy/thebeat-apresentacao/settings/pages
