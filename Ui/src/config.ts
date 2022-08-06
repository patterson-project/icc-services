const config = {
  LED_STRIP_ENDPOINT: "http://lighting-service-cluster-ip.default.svc.cluster.local/lighting/ledstrip",
  BULB_1_ENDPOINT: "http://lighting-service-cluster-ip.default.svc.cluster.local/lighting/lighting/bulb1",
  BULB_2_ENDPOINT: "http://lighting-service-cluster-ip.default.svc.cluster.local/lighting/bulb2",
  SCENE_ENDPOINT: "http://lighting-service-cluster-ip.default.svc.cluster.local/lighting/scene",
  DEVICE_MANAGER_ENDPOINT: "http://device-manager-cluster-ip.default.svc.cluster.local/devices"
};

export default config;
