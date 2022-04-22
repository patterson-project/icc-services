import { Grid, Typography } from "@mui/material";
import React, { FC } from "react";
import BrightnessSlider from "../Components/BrightnessSlider";
import OperationButton from "../Components/OperationButton";
import LooksIcon from "@mui/icons-material/Looks";
import TheatersIcon from "@mui/icons-material/Theaters";
import ClearAllIcon from "@mui/icons-material/ClearAll";
import config from "../config";
import ColorSelectionTab from "../Components/ColorSelectionTab";
import { LightingRequest, RainbowRequest } from "../types";

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

const ColorSelectPage: FC = () => {
  const operationButtonOnClick = (operation: string) => {
    const operationRequest: LightingRequest = {
      operation: operation
    };

    fetch(config.LIGHTING_API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(operationRequest)
    }).catch((error) => {
      console.log("ERROR", error);
    });
  };

  
  const rainbowButtonOnClick =  () => {
    const rainbowRequest: RainbowRequest = {
      operation: "rainbow",
      wait_ms: 50
    }

    fetch(config.LIGHTING_API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(rainbowRequest),
    }).catch((error) => {
      console.log("ERROR", error);
    })
  }
  
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
          <BrightnessSlider />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <OperationButton
            operationName="Rainbow"
            icon={<LooksIcon />}
            onClick={() => rainbowButtonOnClick()}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <OperationButton
            operationName="Rainbow Cycle"
            icon={<LooksIcon />}
            onClick={() => operationButtonOnClick("rainbowcycle")}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <OperationButton
            operationName="Color Wipe"
            icon={<ClearAllIcon />}
            onClick={() => operationButtonOnClick("colorwipe")}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <OperationButton
            operationName="Theater Chase"
            icon={<TheatersIcon />}
            onClick={() => operationButtonOnClick("theaterchase")}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <OperationButton
            operationName="Theater Chase Rainbow"
            icon={<TheatersIcon />}
            onClick={() => operationButtonOnClick("theaterchaserainbow")}
          />
        </Grid>
      </Grid>
    </div>
  );
};

export default ColorSelectPage;
