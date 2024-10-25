# pip install moviepy
from moviepy.video.io.VideoFileClip import VideoFileClip

# Caminho do vídeo original e o caminho de saída
input_video_path = "Download.mp4"   # substitua pelo seu arquivo
output_video_path = "video_cortado.mp4"

# Tempo de início e fim do corte (em segundos)
start_time = 14  # exemplo: cortar a partir de 10 segundos
end_time = 50    # exemplo: até 30 segundos

# Carrega o vídeo e realiza o corte
with VideoFileClip(input_video_path) as video:
    video_cortado = video.subclip(start_time, end_time)
    video_cortado.write_videofile(output_video_path, codec="libx264")
