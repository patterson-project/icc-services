import { Box, Grid, Typography } from "@mui/material";
import React, { FC } from "react";
import AnimationIcon from "@mui/icons-material/Animation";
import IOperationButton from "../../OperationButton";
import SceneButtonBox from "../LightingComponents/SceneButtonBox";
import {
  gridContainerStyle,
  gridItemStyle,
  titleStyle,
  pageDivStyle,
  subHeadingStyle,
} from "../../../Styles/DialogStyles";
import { LightingRequest } from "../../../types";
import { post } from "../../../utils";
import config from "../../../config";

const buttonBoxStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  height: "100%",
  backgroundColor: "#2C2C2E",
  width: "90%",
  borderRadius: "10px",
  paddingBottom: "10px",
};

const onClickOcean = () => {
  const sceneRequest: LightingRequest = {
    operation: "ocean",
  };
  post(config.OCEAN_SCENE_ENDPOINT, sceneRequest);
};

const onClickRose = () => {
  const sceneRequest: LightingRequest = {
    operation: "rose",
  };
  post(config.ROSE_SCENE_ENDPOINT, sceneRequest);
};

const onClickRainbow = () => {
  const sceneRequest: LightingRequest = {
    operation: "rainbow",
  };
  post(config.RAINBOW_SCENE_ENDPOINT, sceneRequest);
};

const onClickCandy = () => {
  const sceneRequest: LightingRequest = {
    operation: "candy",
  };
  post(config.CANDY_SCENE_ENDPOINT, sceneRequest);
};

const onClickPeachy = () => {
  const sceneRequest: LightingRequest = {
    operation: "peachy",
  };
  post(config.PEACHY_SCENE_ENDPOINT, sceneRequest);
};

const onClickJungle = () => {
  const sceneRequest: LightingRequest = {
    operation: "jungle",
  };
  post(config.JUNGLE_SCENE_ENDPOINT, sceneRequest);
};

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
