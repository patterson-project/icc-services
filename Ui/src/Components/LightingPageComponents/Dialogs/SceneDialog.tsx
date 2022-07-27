import { Box, Grid, Typography } from "@mui/material";
import React, { FC } from "react";
import SceneButtonBox from "../LightingComponents/SceneButtonBox";
import {
  gridContainerStyle,
  gridItemStyle,
  titleStyle,
  pageDivStyle,
  subHeadingStyle,
} from "../../../Styles/DialogStyles";

const SceneDialog: FC = () => {
  return (
    <div style={pageDivStyle}>
      <Box style={gridItemStyle}>
        <Typography style={titleStyle}>Environments</Typography>
      </Box>
      <Box style={gridItemStyle}>
        <Typography style={subHeadingStyle}>Select a preset scene</Typography>
      </Box>
      <Grid container spacing={1.5} style={gridContainerStyle}>
        <Grid item xs={12} style={gridItemStyle}>
          <SceneButtonBox></SceneButtonBox>
        </Grid>
      </Grid>
    </div>
  );
};

export default SceneDialog;
