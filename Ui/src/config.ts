/* Uncomment and set domain to local db for testing */
// const domain = window.location.href;
const domain = "http://10.0.0.86/";

const config = {
  DEVICE_MANAGER_SERVICE_ENDPOINT: `${domain}devices`,
  LIGHTING_SERVICE_ENDPOINT: `${domain}lighting`
};

export default config;
