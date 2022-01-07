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

function ColorSelectPage() {
  return (
    <div style={colorSelectPageStyle}>
      <Grid container spacing={2}>
        <Grid item xs={12} style={gridItemStyle}>
          <Typography style={titleStyle}>Led Control</Typography>
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <ColorWheel />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <BrightnessSlider />
        </Grid>
      </Grid>
    </div>
  );
}

export default ColorSelectPage;
