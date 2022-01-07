import { Box, Grid, Slider } from "@mui/material";
import BrightnessLowIcon from "@mui/icons-material/BrightnessLow";
import BrightnessHighIcon from "@mui/icons-material/BrightnessHigh";
import React from "react";
import config from "./config";

interface BrightnessRequest {
  operation: string;
  brightness: number;
}

const brightnessSliderStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  height: "50px",
  backgroundColor: "#3B3B3B",
  width: "300px",
  paddingLeft: "12px",
  paddingRight: "12px",
  borderRadius: "6px",
  marginBottom: "20px",
};

const iconStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  paddingTop: "7px",
  color: "white",
  fontSize: "medium",
};

function BrightnessSlider() {
  const onChangeBrightness = (value: number) => {
    const brightnessRequest: BrightnessRequest = {
      operation: "brightness",
      brightness: value,
    };

    fetch(config.LED_API_URL + "brightness", {
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
    <Box style={brightnessSliderStyle}>
      <Grid container spacing={2}>
        <Grid item xs={1}>
          <BrightnessLowIcon style={iconStyle} />
        </Grid>
        <Grid item xs={10}>
          <Slider
            aria-label="Brightness"
            defaultValue={100}
            step={10}
            valueLabelDisplay="auto"
            marks
            min={0}
            max={100}
            onChangeCommitted={(_e, v) => onChangeBrightness(v as number)}
          />
        </Grid>
        <Grid item xs={1}>
          <BrightnessHighIcon style={iconStyle} />
        </Grid>
      </Grid>
    </Box>
  );
}

export default BrightnessSlider;
