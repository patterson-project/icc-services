import React from "react";
import ColorPicker from "@radial-color-picker/react-color-picker";
import "@radial-color-picker/react-color-picker/dist/react-color-picker.min.css";
import config from "./config";
import { Box } from "@mui/material";

interface RgbRequest {
  operation: string;
  r?: number;
  g?: number;
  b?: number;
}

const colorWheelStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  backgroundColor: "#3B3B3B",
  padding: "20px",
  borderRadius: "6px",
};

function ColorWheel() {
  const onChange = (hue: number) => {
    const rgb = hslToRgb(hue);
    const ledRequest: RgbRequest = {
      operation: "rgb",
      r: rgb.r,
      g: rgb.g,
      b: rgb.b,
    };

    fetch(config.LED_API_URL + "rgb", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(ledRequest),
    }).catch((error) => {
      console.log("ERROR", error);
    });
  };

  const onSelect = () => {
    fetch(config.LED_API_URL + "off", {
      method: "GET",
    }).catch((error) => {
      console.log("ERROR", error);
    });
  };

  const hslToRgb = (h: number) => {
    var s = 100;
    var l = 50;
    var r, g, b, m, c, x;

    if (!isFinite(h)) h = 0;
    if (!isFinite(s)) s = 0;
    if (!isFinite(l)) l = 0;

    h /= 60;
    if (h < 0) h = 6 - (-h % 6);
    h %= 6;

    s = Math.max(0, Math.min(1, s / 100));
    l = Math.max(0, Math.min(1, l / 100));

    c = (1 - Math.abs(2 * l - 1)) * s;
    x = c * (1 - Math.abs((h % 2) - 1));

    if (h < 1) {
      r = c;
      g = x;
      b = 0;
    } else if (h < 2) {
      r = x;
      g = c;
      b = 0;
    } else if (h < 3) {
      r = 0;
      g = c;
      b = x;
    } else if (h < 4) {
      r = 0;
      g = x;
      b = c;
    } else if (h < 5) {
      r = x;
      g = 0;
      b = c;
    } else {
      r = c;
      g = 0;
      b = x;
    }

    m = l - c / 2;
    r = Math.round((r + m) * 255);
    g = Math.round((g + m) * 255);
    b = Math.round((b + m) * 255);

    return { r: r, g: g, b: b };
  };

  return (
    <Box style={colorWheelStyle}>
      <ColorPicker onChange={onChange} onSelect={onSelect} />
    </Box>
  );
}

export default ColorWheel;
