import React, {
  Dispatch,
  FC,
  SetStateAction,
  useCallback,
  useState,
} from "react";
import ColorPicker from "@radial-color-picker/react-color-picker";
import "@radial-color-picker/react-color-picker/dist/react-color-picker.min.css";
import config from "../../../../config";
import { Box } from "@mui/material";
import { Device, HsvRequest, LightingRequest } from "../../../../types";
import { post, useDidMountEffect } from "../../../../utils";
import debounce from "lodash.debounce";
import { ObjectId } from "mongodb";

interface IColorWheel {
  targetDevices: Device[] | undefined;
  setModifyingColor: Dispatch<SetStateAction<boolean>>;
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
    props.targetDevices?.forEach((device) => {
      const hsvRequest: HsvRequest = {
        _id: device._id as ObjectId,
        operation: "hsv",
        h: hue,
      };

      if (device.model === "Kasa KL-215") {
        post(config.BULB_ENDPOINT + "/request", hsvRequest);
      }
    });
  }, [hue]);

  const onSelect = () => {
    props.targetDevices?.forEach((device) => {
      const offRequest: LightingRequest = {
        _id: device._id as ObjectId,
        operation: "off",
      };

      if (device.model === "Kasa KL-215") {
        post(config.BULB_ENDPOINT + "/request", offRequest);
      }
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
