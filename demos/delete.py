from Ziggeo import Ziggeo

ziggeo = Ziggeo("APP_TOKEN", "PRIVATE_KEY", "ENC_KEY")

print ziggeo.videos().delete("VIDEO_TOKEN")