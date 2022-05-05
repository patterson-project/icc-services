import { Grid, Typography } from "@mui/material";
import React, { FC, useState } from "react";
import Slider from "../Components/Slider";
import OperationButton from "../Components/OperationButton";
import LooksIcon from "@mui/icons-material/Looks";
import config from "../config";
import ColorSelectionTab from "../Components/ColorSelectionTab";
import BrightnessLowIcon from "@mui/icons-material/BrightnessLow";
import BrightnessHighIcon from "@mui/icons-material/BrightnessHigh";
import WbSunnyIcon from "@mui/icons-material/WbSunny";
import WbTwilightIcon from "@mui/icons-material/WbTwilight";
import { BrightnessRequest, LightingRequest, ColorTempRequest } from "../types";
import LightingDeviceSwitches from "../Components/LightingDeviceSwitches";
import { post } from "../utils";

const colorSelectPageStyle = {
  height: "100%",
  margin: "0px",
  minHeight: "100vh",
  backgroundColor: "#222222",
};

const gridContainerStyle = {
  marginTop: "0px",
  paddingBottom: "40px",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const gridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const titleStyle = {
  color: "white",
  fontSize: "40px",
  marginTop: "20px",
  fontFamily: "Ubuntu, -apple-system",
  fontWeight: "bold",
};

const leftIconStyle = {
  color: "white",
  fontSize: "medium",
  marginLeft: "15px",
};
const rightIconStyle = {
  color: "white",
  fontSize: "medium",
  marginRight: "15px",
};

const ColorSelectPage: FC = () => {
  const [sequenceDelay, setSequenceDelay] = useState<number>(50);
  const [bulbOneTarget, setBulbOneTarget] = useState<boolean>(false);
  const [bulbTwoTarget, setBulbTwoTarget] = useState<boolean>(false);
  const [ledStripTarget, setLedStripTarget] = useState<boolean>(false);

  const rainbowButtonOnClick = () => {
    const rainbowRequest: LightingRequest = {
      operation: "rainbow",
    };

    if (ledStripTarget) {
      post(config.LED_STRIP_ENDPOINT, rainbowRequest);
    }

    if (bulbOneTarget) {
      post(config.BULB_1_ENDPOINT, rainbowRequest);
    }

    if (bulbTwoTarget) {
      post(config.BULB_2_ENDPOINT, rainbowRequest);
    }
  };

  const rainbowCycleButtonOnClick = () => {
    const rainbowCycleRequest: LightingRequest = {
      operation: "rainbow_cycle",
    };

    if (ledStripTarget) {
      post(config.LED_STRIP_ENDPOINT, rainbowCycleRequest);
    }

    if (bulbOneTarget) {
      post(config.BULB_1_ENDPOINT, rainbowCycleRequest);
    }

    if (bulbTwoTarget) {
      post(config.BULB_2_ENDPOINT, rainbowCycleRequest);
    }
  };

  const onChangeBrightness = (value: number) => {
    const brightnessRequest: BrightnessRequest = {
      operation: "brightness",
      brightness: value,
    };

    if (ledStripTarget) {
      post(config.LED_STRIP_ENDPOINT, brightnessRequest);
    }

    if (bulbOneTarget) {
      post(config.BULB_1_ENDPOINT, brightnessRequest);
    }

    if (bulbTwoTarget) {
      post(config.BULB_2_ENDPOINT, brightnessRequest);
    }
  };

  const onChangeColorTemp = (value: number) => {
    const colortempRequest: ColorTempRequest = {
      operation: "temperature",
      temperature: value,
    };

    if (bulbOneTarget) {
      post(config.BULB_1_ENDPOINT, colortempRequest);
    }

    if (bulbTwoTarget) {
      post(config.BULB_2_ENDPOINT, colortempRequest);
    }
  };

  return (
    <div style={colorSelectPageStyle}>
      <Grid container spacing={2} style={gridContainerStyle}>
        <Grid item xs={12} style={gridItemStyle}>
          <Typography style={titleStyle}>Led Control</Typography>
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <ColorSelectionTab
            ledStripTarget={ledStripTarget}
            bulbOneTarget={bulbOneTarget}
            bulbTwoTarget={bulbTwoTarget}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <LightingDeviceSwitches
            setBulbOneTarget={setBulbOneTarget}
            setBulbTwoTarget={setBulbTwoTarget}
            setLedStripTarget={setLedStripTarget}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <Slider
            min={0}
            max={100}
            step={10}
            defaultValue={100}
            onChange={onChangeBrightness}
            startIcon={<BrightnessLowIcon style={leftIconStyle} />}
            endIcon={<BrightnessHighIcon style={rightIconStyle} />}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <Slider
            min={2500}
            max={6500}
            step={50}
            defaultValue={sequenceDelay}
            onChange={setSequenceDelay}
            startIcon={<WbTwilightIcon style={leftIconStyle} />}
            endIcon={<WbSunnyIcon style={rightIconStyle} />}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <OperationButton
            operationName="Rainbow"
            icon={<LooksIcon />}
            onClick={rainbowButtonOnClick}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <OperationButton
            operationName="Rainbow Cycle"
            icon={<LooksIcon />}
            onClick={rainbowCycleButtonOnClick}
          />
        </Grid>
      </Grid>
    </div>
  );
};

export default ColorSelectPage;
