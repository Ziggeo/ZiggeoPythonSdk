
class ZiggeoConfig:
    def __init__(self):
        self.server_api_url = "https://srv-api.ziggeo.com"

        self.regions = {"r1":"https://srv-api-eu-west-1.ziggeo.com"}

        self.api_url = "https://api-us-east-1.ziggeo.com"

        self.api_regions = {"r1":"https://api-eu-west-1.ziggeo.com"}

        self.cdn_url = "https://video-cdn.ziggeo.com"

        self.cdn_regions = {"r1":"https://video-cdn-eu-west-1.ziggeo.com"}

        self.resilience_factor = 5
        self.request_timeout = 60