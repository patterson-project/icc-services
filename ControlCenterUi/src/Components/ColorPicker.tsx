import React, { FC, useCallback, useEffect, useState } from "react";
import { HslaColorPicker, HslaColor } from 'react-colorful';
import debounce from "lodash.debounce";
import { Box } from "@mui/material";
import { HslaRequest } from "../types";
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

const defaultColor: HslaColor = {
    h: 0,
    s: 0.5,
    l: 0.2,
    a: 1
};

const ColorPicker: FC = () => {
    const [hslaColor, setHslaColor] = useState<HslaColor>(defaultColor);
    
    const changeColor = (newHslaColor: HslaColor) => {
      setHslaColor(newHslaColor);
    };

    const debouncedHslaColorChangeHandler = useCallback(debounce(changeColor, 300), []);

    useEffect(() => {
      const hslaRequest: HslaRequest = {
        operation: "hsla",
        h: hslaColor.h,
        s: hslaColor.s,
        l: hslaColor.l,
        a: hslaColor.a
      };

      fetch(config.LED_API_URL + "lighting", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(hslaRequest),
      }).catch((error) => {
        console.log("ERROR", error);
      });
    });
  
    return (
      <Box style={colorPickerBoxStyle}>
        <HslaColorPicker style={colorPickerStyle} color={hslaColor} onChange={debouncedHslaColorChangeHandler}/> 
      </Box>
    );
  };
  
  export default ColorPicker;