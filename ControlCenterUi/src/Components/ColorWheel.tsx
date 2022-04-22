import React, { Dispatch, FC, SetStateAction } from "react";
import ColorPicker from "@radial-color-picker/react-color-picker";
import "@radial-color-picker/react-color-picker/dist/react-color-picker.min.css";
import config from "../config";
import { Box } from "@mui/material";
import { HsvRequest, LightingRequest } from "../types";

interface ColorWheelProps {
  setModifyingColor: Dispatch<SetStateAction<boolean>>;
}

const colorWheelStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  width: "340px",
  height: "340px",
  borderRadius: "10px",
};

const ColorWheel: FC<ColorWheelProps> = (props): JSX.Element => {
  const onChange = (hue: number) => {
    const hslaRequest: HsvRequest = {
      operation: "hsv",
      h: hue
    };

    fetch(config.LIGHTING_API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(hslaRequest),
    }).catch((error) => {
      console.log("ERROR", error);
    });
    
    props.setModifyingColor(false);
  };

  const onInput = () => {
    props.setModifyingColor(true);
  };

  const onSelect = () => {
    const offRequest: LightingRequest = {
      operation: "off"
    }

    fetch(config.LIGHTING_API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(offRequest)
    }).catch((error) => {
      console.log("ERROR", error);
    });
  };

  return (
    <Box style={colorWheelStyle}>
      <ColorPicker onChange={onChange} onSelect={onSelect} onInput={onInput} />
    </Box>
  );
};

export default ColorWheel;
