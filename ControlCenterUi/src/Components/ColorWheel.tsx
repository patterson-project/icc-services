import React, {
  Dispatch,
  FC,
  SetStateAction,
  useCallback,
  useState,
} from "react";
import ColorPicker from "@radial-color-picker/react-color-picker";
import "@radial-color-picker/react-color-picker/dist/react-color-picker.min.css";
import config from "../config";
import { Box } from "@mui/material";
import { HsvRequest, LightingRequest } from "../types";
import { post, useDidMountEffect } from "../utils";
import debounce from "lodash.debounce";

interface IColorWheel {
  setModifyingColor: Dispatch<SetStateAction<boolean>>;
  ledStripTarget: boolean;
  bulbOneTarget: boolean;
  bulbTwoTarget: boolean;
}

const colorWheelStyle = {
  display: "flex",
  alignItems: "top",
  justifyContent: "center",
  width: "340px",
  height: "340px",
  borderRadius: "10px",
  paddingTop: "20px",
};

const ColorWheel: FC<IColorWheel> = (props): JSX.Element => {
  const [hue, setHue] = useState<number>(0);

  const changeHue = (hue: number) => {
    setHue(hue);
  };

  const debounceHueChangeHandler = useCallback(debounce(changeHue, 30), []);

  useDidMountEffect(() => {
    const hsvRequest: HsvRequest = {
      operation: "hsv",
      h: hue,
    };

    if (props.ledStripTarget) {
      post(config.LED_STRIP_ENDPOINT, hsvRequest);
    }

    if (props.bulbOneTarget) {
      post(config.BULB_1_ENDPOINT, hsvRequest);
    }

    if (props.bulbTwoTarget) {
      post(config.BULB_2_ENDPOINT, hsvRequest);
    }
  }, [hue]);

  const onSelect = () => {
    const offRequest: LightingRequest = {
      operation: "off",
    };

    post(config.LED_STRIP_ENDPOINT, offRequest);
    post(config.BULB_1_ENDPOINT, offRequest);
    post(config.BULB_2_ENDPOINT, offRequest);
  };

  const onTouchStart = () => {
    props.setModifyingColor(true);
  };

  const onTouchEnd = () => {
    props.setModifyingColor(false);
  };

  return (
    <Box style={colorWheelStyle}>
      <ColorPicker
        onTouchStart={onTouchStart}
        onTouchEnd={onTouchEnd}
        onSelect={onSelect}
        onInput={debounceHueChangeHandler}
      />
    </Box>
  );
};

export default ColorWheel;
