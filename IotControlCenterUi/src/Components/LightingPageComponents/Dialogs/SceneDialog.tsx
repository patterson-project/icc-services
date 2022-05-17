import { Grid, Typography } from "@mui/material";
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
      <Grid container spacing={2} style={gridContainerStyle}>
        <Grid item xs={12} style={gridItemStyle}>
          <Typography style={titleStyle}>Scenes</Typography>
        </Grid>
      </Grid>
    </div>
  );
};

export default SceneDialog;
