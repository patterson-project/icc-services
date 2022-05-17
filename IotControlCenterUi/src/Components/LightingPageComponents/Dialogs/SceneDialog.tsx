import { Box, Grid, Typography } from "@mui/material";
import React, { FC } from "react";
import {
  gridContainerStyle,
  gridItemStyle,
  titleStyle,
} from "../../../Styles/DialogStyles";

const sceneDialogDivStyle = {
  height: "100%",
  margin: "0px",
  minHeight: "100vh",
  backgroundColor: "#151515",
};

const SceneDialog: FC = () => {
  return (
    <div style={sceneDialogDivStyle}>
      <Box style={gridItemStyle}>
        <Typography style={titleStyle}>Scenes</Typography>
      </Box>
      <Grid container spacing={1.5} style={gridContainerStyle}>
        <Grid item xs={12} style={gridItemStyle}></Grid>
      </Grid>
    </div>
  );
};

export default SceneDialog;
