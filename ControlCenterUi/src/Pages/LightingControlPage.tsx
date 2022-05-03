import { Grid, Typography } from "@mui/material";
import React, { FC, useState } from "react";
import Slider from "../Components/Slider";
import OperationButton from "../Components/OperationButton";
import LooksIcon from "@mui/icons-material/Looks";
import config from "../config";
import ColorSelectionTab from "../Components/ColorSelectionTab";
import BrightnessLowIcon from "@mui/icons-material/BrightnessLow";
import BrightnessHighIcon from "@mui/icons-material/BrightnessHigh";
import AccessTimeIcon from "@mui/icons-material/AccessTime";
import MoreTimeIcon from "@mui/icons-material/MoreTime";
import { BrightnessRequest, LightingRequest } from "../types";
import LightingDeviceSwitches from "../Components/LightingDeviceSwitches";

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

const iconStyle = {
  color: "white",
  fontSize: "medium",
};

const ColorSelectPage: FC = () => {
  const [sequenceDelay, setSequenceDelay] = useState<number>(50);
  const [bulbOneTarget, setBulbOneTarget] = useState<boolean>(true);
  const [bulbTwoTarget, setBulbTwoTarget] = useState<boolean>(true);
  const [ledStripTarget, setLedStripTarget] = useState<boolean>(true);

  const rainbowButtonOnClick = () => {
    const rainbowRequest: LightingRequest = {
      operation: "rainbow",
    };

    fetch(config.LED_STRIP_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(rainbowRequest),
    }).catch((error) => {
      console.log("ERROR", error);
    });
  };

  const rainbowCycleButtonOnClick = () => {
    const rainbowCycleRequest: LightingRequest = {
      operation: "rainbow_cycle",
    };

    fetch(config.LED_STRIP_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(rainbowCycleRequest),
    }).catch((error) => {
      console.log("ERROR", error);
    });
  };

  const onChangeBrightness = (value: number) => {
    const brightnessRequest: BrightnessRequest = {
      operation: "brightness",
      brightness: value,
    };

    fetch(config.LED_STRIP_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(brightnessRequest),
    }).catch((error) => {
      console.log("ERROR", error);
    });
  };

  return (
    <div style={colorSelectPageStyle}>
      <Grid container spacing={2} style={gridContainerStyle}>
        <Grid item xs={12} style={gridItemStyle}>
          <Typography style={titleStyle}>Led Control</Typography>
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <ColorSelectionTab />
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
            startIcon={<BrightnessLowIcon style={iconStyle} />}
            endIcon={<BrightnessHighIcon style={iconStyle} />}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <Slider
            min={10}
            max={100}
            step={5}
            defaultValue={sequenceDelay}
            onChange={setSequenceDelay}
            startIcon={<AccessTimeIcon style={iconStyle} />}
            endIcon={<MoreTimeIcon style={iconStyle} />}
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
