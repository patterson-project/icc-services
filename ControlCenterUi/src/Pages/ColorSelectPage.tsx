import { Grid, Typography } from "@mui/material";
import React, { FC } from "react";
import BrightnessSlider from "../Components/BrightnessSlider";
import ColorWheel from "../Components/ColorWheel";
import OperationButton from "../Components/OperationButton";
import LooksIcon from "@mui/icons-material/Looks";
import TheatersIcon from "@mui/icons-material/Theaters";
import ClearAllIcon from "@mui/icons-material/ClearAll";
import config from "../config";

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
    fetch(config.LED_API_URL + operation, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    }).catch((error) => {
      console.log("ERROR", error);
    });
  };

  return (
    <div style={colorSelectPageStyle}>
      <Grid container spacing={2} style={gridContainerStyle}>
        <Grid item xs={12} style={gridItemStyle}>
          <Typography style={titleStyle}>Title Change Test!</Typography>
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <ColorWheel />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <BrightnessSlider />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <OperationButton
            operationName="Rainbow"
            icon={<LooksIcon />}
            onClick={() => operationButtonOnClick("rainbow")}
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
