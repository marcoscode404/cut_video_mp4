# uv add yt-dlp
import yt_dlp

def download_video(url, save_path="downloads/"):
    """
    Baixa um vídeo do YouTube usando yt_dlp.
    
    Args:
        url (str): URL do vídeo do YouTube.
        save_path (str): Caminho onde o vídeo será salvo.
    """
    try:
        ydl_opts = {
            'outtmpl': f'{save_path}%(title)s.%(ext)s',  # Nome do arquivo de saída
            'format': 'bestvideo+bestaudio/best',       # Melhor qualidade disponível
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Download concluído! Salvo em: {save_path}")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

if __name__ == "__main__":
    video_url = input("Digite a URL do vídeo do YouTube: ")
    save_path = input("Digite o caminho para salvar o vídeo (ou pressione Enter para o padrão): ") or "downloads/"
    download_video(video_url, save_path)
