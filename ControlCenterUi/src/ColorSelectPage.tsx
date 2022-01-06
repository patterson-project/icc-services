import { Grid, Typography } from "@mui/material";
import React, { useState } from "react";
import ColorWheel from "./ColorWheel";

const colorSelectPageStyle = {
  height: "100%",
  margin: "0px",
  minHeight: "100vh",
  backgroundColor: "#222222",
};

const colorWheelStyle = {
  marginTop: "40px",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const titleStyle = {
  color: "white",
};

function ColorSelectPage() {
  return (
    <div style={colorSelectPageStyle}>
      <Grid container spacing={2}>
        <Grid item xs={12} style={colorWheelStyle}>
          <ColorWheel />
        </Grid>
      </Grid>
    </div>
  );
}

export default ColorSelectPage;
