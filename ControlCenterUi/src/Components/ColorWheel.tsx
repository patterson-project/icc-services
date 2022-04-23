import React, { Dispatch, FC, SetStateAction, useCallback, useState } from "react";
import ColorPicker from "@radial-color-picker/react-color-picker";
import "@radial-color-picker/react-color-picker/dist/react-color-picker.min.css";
import config from "../config";
import { Box } from "@mui/material";
import { HsvRequest, LightingRequest } from "../types";
import useDidMountEffect from "../utils";
import debounce from "lodash.debounce";

interface ColorWheelProps {
  setModifyingColor: Dispatch<SetStateAction<boolean>>;
}

const colorWheelStyle = {
  display: "flex",
  alignItems: "top",
  justifyContent: "center",
  width: "340px",
  height: "340px",
  borderRadius: "10px",
  paddingTop: "20px"
};

const ColorWheel: FC<ColorWheelProps> = (props): JSX.Element => {
  const [hue, setHue] = useState<number>(0);

  const changeHue = (hue: number) => {
    setHue(hue);
  }

  const debounceHueChangeHandler = useCallback(debounce(changeHue, 10), []);

  useDidMountEffect(() => {
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
  }, [hue]);
  
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

  const onTouchStart = () => {
    props.setModifyingColor(true);
  };

    const onTouchEnd = () => {
    props.setModifyingColor(false);
  };

  return (
    <Box style={colorWheelStyle}>
      <ColorPicker onTouchStart={onTouchStart} onTouchEnd={onTouchEnd} onSelect={onSelect} onInput={debounceHueChangeHandler} />
    </Box>
  );
};

export default ColorWheel;
