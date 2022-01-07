import { Grid, Typography } from "@mui/material";
import React from "react";
import BrightnessSlider from "./BrightnessSlider";
import ColorWheel from "./ColorWheel";

const colorSelectPageStyle = {
  height: "100%",
  margin: "0px",
  minHeight: "100vh",
  backgroundColor: "#222222",
};

const gridStyle = {
  marginTop: "20px",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const titleStyle = {
  color: "white",
  fontSize: "40px",
  fontFamily: "Ubuntu",
};

function ColorSelectPage() {
  return (
    <div style={colorSelectPageStyle}>
      <Grid container spacing={2}>
        <Grid item xs={12} style={gridStyle}>
          <Typography style={titleStyle}>Led Control</Typography>
        </Grid>
        <Grid item xs={12} style={gridStyle}>
          <ColorWheel />
        </Grid>
        <Grid item xs={12} style={gridStyle}>
          <BrightnessSlider />
        </Grid>
      </Grid>
    </div>
  );
}

export default ColorSelectPage;
