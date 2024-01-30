from django.shortcuts import render
import ffmpeg_streaming
from django.conf.urls.static import static
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
# Create your views here.

def stream_view(request):
    return render(request,"streaming/index.html")

def stream_data(request):
    video = ffmpeg_streaming.input('/home/kengni/projets/skul/python/miagex/assets/videos/video.mp4')
    _360p = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
    _480p = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
    _720p = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))

    hls = video.hls(Formats.h264())
    hls.representations(_360p, _480p, _720p)
    hls.output('/home/kengni/projets/skul/python/miagex/assets/videos/video.m3u8')
