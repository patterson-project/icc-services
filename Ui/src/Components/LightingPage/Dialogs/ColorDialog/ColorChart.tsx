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
import { Device, HsvRequest } from "../../../../types";
import { post, useDidMountEffect } from "../../../../utils";
import config from "../../../../config";
import { ObjectId } from "mongodb";

interface IColorChart {
  targetDevices: Device[];
  setModifyingColor: Dispatch<SetStateAction<boolean>>;
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
    props.targetDevices?.forEach((target) => {
      const hsvRequest: HsvRequest = {
        _id: target._id as ObjectId,
        operation: "hsv",
        h: hsvColor.h,
        s: hsvColor.s,
        v: hsvColor.v,
      };

      if (target.model === "Kasa KL-215") {
        post(config.BULB_ENDPOINT + "/request", hsvRequest);
      }
    });
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
