const ip = require('ip');

const ip_address = ip.address();

const config = {
  LED_STRIP_ENDPOINT: `${ip_address}/lighting/ledstrip`,
  BULB_1_ENDPOINT: `${ip_address}/lighting/lighting/bulb1`,
  BULB_2_ENDPOINT: `${ip_address}/lighting/bulb2`,
  SCENE_ENDPOINT: `${ip_address}/lighting/scene`,
  DEVICE_MANAGER_ENDPOINT: `${ip_address}/devices`
};

export default config;
