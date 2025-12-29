import http.server
import socketserver
import os
import json
import mimetypes
from urllib.parse import unquote

PORT = 8000
BASE_DIR = r"C:\Users\Gabriel\Downloads\INSTAGRAM BEAT CLUB"

class TheBeatHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Handle API endpoints
        if self.path.startswith('/api/'):
            self.handle_api()
        else:
            # Serve static files
            super().do_GET()
    
    def handle_api(self):
        if '/api/posts' in self.path:
            self.send_api_response(self.get_posts_data())
        elif '/api/post/' in self.path:
            post_id = self.path.split('/')[-1]
            self.send_api_response(self.get_post_details(post_id))
        elif '/api/caption/' in self.path:
            folder = unquote(self.path.split('/')[-1])
            self.send_api_response(self.get_caption(folder))
        elif '/api/media/' in self.path:
            folder = unquote(self.path.split('/')[-1])
            self.send_api_response(self.get_media_files(folder))
    
    def send_api_response(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
    
    def get_posts_data(self):
        return {
            "posts": [
                {"id": 1, "folder": "POST_01_CARROSSEL_Ecosystem", "type": "Carrossel", "title": "Ecosystem", "date": "06/01/2025", "time": "07:30"},
                {"id": 2, "folder": "POST_02_VIDEO_BannerStreet", "type": "Vídeo", "title": "Banner Street", "date": "08/01/2025", "time": "12:30"},
                {"id": 3, "folder": "POST_03_CARROSSEL_Hormonios", "type": "Carrossel", "title": "O Que os Hormônios Dizem", "date": "10/01/2025", "time": "18:30"},
                {"id": 4, "folder": "POST_04_VIDEO_BeatNike", "type": "Vídeo", "title": "Beat + Nike", "date": "13/01/2025", "time": "07:30"},
                {"id": 5, "folder": "POST_05_CARROSSEL_Ozempic", "type": "Carrossel", "title": "Geração Ozempic", "date": "15/01/2025", "time": "12:30"},
                {"id": 6, "folder": "POST_06_VIDEO_Helicoptero", "type": "Vídeo", "title": "Helicóptero", "date": "17/01/2025", "time": "18:30"},
                {"id": 7, "folder": "POST_07_CARROSSEL_Sauna", "type": "Carrossel", "title": "Sauna - Biohack Cardíaco", "date": "20/01/2025", "time": "07:30"},
                {"id": 8, "folder": "POST_08_VIDEO_Kettlebell", "type": "Vídeo", "title": "Kettlebell Nike", "date": "22/01/2025", "time": "12:30"},
                {"id": 9, "folder": "POST_09_CARROSSEL_BemEstar", "type": "Carrossel", "title": "Bem-Estar Redefinido", "date": "24/01/2025", "time": "18:30"},
                {"id": 10, "folder": "POST_10_VIDEO_Lapidando", "type": "Vídeo", "title": "Lapidando", "date": "27/01/2025", "time": "07:30"},
                {"id": 11, "folder": "POST_11_VIDEO_RedBull", "type": "Vídeo", "title": "Red Bull Partnership", "date": "29/01/2025", "time": "12:30"},
                {"id": 12, "folder": "POST_12_VIDEO_Cinematic", "type": "Vídeo", "title": "Cinematic City", "date": "31/01/2025", "time": "18:30"},
                {"id": 13, "folder": "POST_13_VIDEO_BannerMockup", "type": "Imagem", "title": "Banner Mockup", "date": "03/02/2025", "time": "07:30"}
            ]
        }
    
    def get_caption(self, folder):
        caption_path = os.path.join(BASE_DIR, "POSTS_ORGANIZADOS", folder, "LEGENDA.txt")
        try:
            with open(caption_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Remove decorative lines
                lines = [l for l in content.split('\n') if not l.startswith('━')]
                caption = '\n'.join(lines).strip()
                return {"caption": caption}
        except:
            return {"caption": "Legenda não encontrada"}
    
    def get_media_files(self, folder):
        folder_path = os.path.join(BASE_DIR, "POSTS_ORGANIZADOS", folder)
        media = []
        try:
            for file in sorted(os.listdir(folder_path)):
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.mp4')) and file != "LEGENDA.txt":
                    media.append({
                        "filename": file,
                        "path": f"/POSTS_ORGANIZADOS/{folder}/{file}",
                        "type": "video" if file.endswith('.mp4') else "image"
                    })
        except:
            pass
        return {"media": media}

os.chdir(BASE_DIR)

with socketserver.TCPServer(("", PORT), TheBeatHandler) as httpd:
    print(f"""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║             THE BEAT LIFE CLUB - CONTENT HUB SERVER              ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝

🌐 Servidor rodando em: http://localhost:{PORT}

📊 Dashboard disponível em: http://localhost:{PORT}/dashboard.html

📁 Servindo arquivos de: {BASE_DIR}

⚡ Pressione Ctrl+C para parar o servidor

════════════════════════════════════════════════════════════════════
    """)
    httpd.serve_forever()
