import React, {
  Dispatch,
  FC,
  SetStateAction,
  useCallback,
  useState,
} from "react";
import { HsvColorPicker, HsvColor } from "react-colorful";
import debounce from "lodash.debounce";
import { Box } from "@mui/material";
import { HsvRequest } from "../types";
import { post, useDidMountEffect } from "../utils";
import config from "../config";

interface IColorChart {
  setModifyingColor: Dispatch<SetStateAction<boolean>>;
  ledStripTarget: boolean;
  bulbOneTarget: boolean;
  bulbTwoTarget: boolean;
}

const colorChartBoxStyle = {
  display: "flex",
  alignItems: "top",
  justifyContent: "center",
  width: "340px",
  height: "340px",
  borderRadius: "10px",
  paddingTop: "20px",
};

const colorChartStyle = {
  width: "280px",
  height: "280px",
};

const defaultColor: HsvColor = {
  h: 0,
  s: 50,
  v: 50,
};

const ColorChart: FC<IColorChart> = (props) => {
  const [hsvColor, setHsvColor] = useState<HsvColor>(defaultColor);

  const changeColor = (newHsvColor: HsvColor) => {
    setHsvColor(newHsvColor);
  };

  const debouncedHsvColorChangeHandler = useCallback(
    debounce(changeColor, 30),
    []
  );

  const onTouchStart = () => {
    props.setModifyingColor(true);
  };

  const onTouchEnd = () => {
    props.setModifyingColor(false);
  };

  useDidMountEffect(() => {
    const hsvRequest: HsvRequest = {
      operation: "hsv",
      h: hsvColor.h,
      s: hsvColor.s,
      v: hsvColor.v,
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
  }, [hsvColor]);

  return (
    <Box style={colorChartBoxStyle}>
      <HsvColorPicker
        style={colorChartStyle}
        color={hsvColor}
        onChange={debouncedHsvColorChangeHandler}
        onTouchStart={onTouchStart}
        onTouchEnd={onTouchEnd}
      />
    </Box>
  );
};

export default ColorChart;
