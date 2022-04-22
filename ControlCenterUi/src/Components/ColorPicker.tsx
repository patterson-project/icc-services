import React, { FC, useCallback, useState } from "react";
import { HsvColorPicker, HsvColor } from 'react-colorful';
import debounce from "lodash.debounce";
import { Box } from "@mui/material";
import { HsvRequest } from "../types";
import useDidMountEffect from "../utils";
import config from "../config";

const colorPickerBoxStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  width: "340px",
  height: "340px",
  borderRadius: "10px",
};

const colorPickerStyle = {
  width: "280px",
  height: "280px",
}

const defaultColor: HsvColor = {
    h: 0,
    s: 0.5,
    v: 0.2,
};

const ColorPicker: FC = () => {
    const [hsvColor, setHsvColor] = useState<HsvColor>(defaultColor);
    
    const changeColor = (newHsvColor: HsvColor) => {
      setHsvColor(newHsvColor);
    };

    const debouncedHslaColorChangeHandler = useCallback(debounce(changeColor, 300), []);

    useDidMountEffect(() => {
      const hslaRequest: HsvRequest = {
        operation: "hsv",
        h: hsvColor.h,
        s: hsvColor.s,
        v: hsvColor.v
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
    }, [hsvColor]); 
  
    return (
      <Box style={colorPickerBoxStyle}>
        <HsvColorPicker style={colorPickerStyle} color={hsvColor} onChange={debouncedHslaColorChangeHandler}/> 
      </Box>
    );
  };
  
  export default ColorPicker;