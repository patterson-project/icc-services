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
import useDidMountEffect from "../utils";
import config from "../config";

interface ColorPickerProps {
  setModifyingColor: Dispatch<SetStateAction<boolean>>;
}

const colorPickerBoxStyle = {
  display: "flex",
  alignItems: "top",
  justifyContent: "center",
  width: "340px",
  height: "340px",
  borderRadius: "10px",
  paddingTop: "20px",
};

const colorPickerStyle = {
  width: "280px",
  height: "280px",
};

const defaultColor: HsvColor = {
  h: 0,
  s: 0.5,
  v: 0.2,
};

const ColorPicker: FC<ColorPickerProps> = (props) => {
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
    const hslaRequest: HsvRequest = {
      operation: "hsv",
      h: hsvColor.h,
      s: hsvColor.s,
      v: hsvColor.v,
    };

    fetch(config.LED_STRIP_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(hslaRequest),
    }).catch((error) => {
      console.log("ERROR", error);
    });
  }, [hsvColor]);

  return (
    <Box style={colorPickerBoxStyle}>
      <HsvColorPicker
        style={colorPickerStyle}
        color={hsvColor}
        onChange={debouncedHsvColorChangeHandler}
        onTouchStart={onTouchStart}
        onTouchEnd={onTouchEnd}
      />
    </Box>
  );
};

export default ColorPicker;
