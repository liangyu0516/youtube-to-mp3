import os, shutil
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from pytube import YouTube
from moviepy.editor import AudioFileClip


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

class SongView(View):
    def get(self, request):
        for filename in os.listdir('media/'):
            file_path = os.path.join('media/', filename)
            os.remove(file_path)

        url = request.GET.get('url')

        if not url:
            return JsonResponse({'success': False, 'error': 'Invalid parameters'})

        try:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            file_path = stream.download('media')

            audio_clip = AudioFileClip(file_path)
            audio_path = file_path.replace('.mp4', '.mp3')
            audio_clip.write_audiofile(audio_path)
            audio_clip.close()
            os.remove(file_path)
            file_path = audio_path

            download_url = f'media/{os.path.basename(file_path)}'
            return JsonResponse({'success': True, 'downloadUrl': download_url})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
