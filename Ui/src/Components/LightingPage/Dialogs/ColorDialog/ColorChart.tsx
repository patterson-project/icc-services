import React, { FC, useCallback, useState } from "react";
import { HsvColorPicker, HsvColor } from "react-colorful";
import debounce from "lodash.debounce";
import { Box } from "@mui/material";
import { Device, HsvRequest } from "../../../../types";
import { post, useDidMountEffect } from "../../../../utils";
import config from "../../../../config";
import { ObjectId } from "mongodb";

interface IColorChart {
  targetDevices: Device[];
}

const colorChartBoxStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  width: "90%",
  height: "350px",
  backgroundColor: "#2C2C2E",
  borderRadius: "10px",
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

  // eslint-disable-next-line react-hooks/exhaustive-deps
  const debouncedHsvColorChangeHandler = useCallback(
    debounce(changeColor, 30),
    []
  );

  useDidMountEffect(() => {
    props.targetDevices?.forEach((device) => {
      const hsvRequest: HsvRequest = {
        target: device._id as ObjectId,
        operation: "hsv",
        h: hsvColor.h,
        s: hsvColor.s,
        v: hsvColor.v,
      };

      // TODO: add snackbar here on success ?
      post(config.LIGHTING_SERVICE_ENDPOINT + "/request", hsvRequest);
    });
  }, [hsvColor]);

  return (
    <Box style={colorChartBoxStyle}>
      <HsvColorPicker
        style={colorChartStyle}
        color={hsvColor}
        onChange={debouncedHsvColorChangeHandler}
      />
    </Box>
  );
};

export default ColorChart;
