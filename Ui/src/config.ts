
// const domain = window.location.href;
const domain = "http://10.0.0.86/";

const config = {
  CUSTOM_LED_STRIP_ENDPOINT: `${domain}lighting/customledstrip`,
  BULB_ENDPOINT: `${domain}lighting/bulb`,
  SCENE_ENDPOINT: `${domain}lighting/scene`,
  DEVICE_MANAGER_ENDPOINT: `${domain}devices`
};

export default config;
