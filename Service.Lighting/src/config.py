import os

class Config:
    MONGO_DB_URL = f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin"
    LED_STRIP_SERVICE_URL = "http://10.0.0.63:8000"
    BULB_CONTROLLER_URL = "http://bulb-controller-cluster-ip.default.svc.cluster.local:8000"
