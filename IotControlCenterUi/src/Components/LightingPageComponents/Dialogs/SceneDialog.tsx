import { Box, Grid, Typography } from "@mui/material";
import React, { FC } from "react";
import AnimationIcon from "@mui/icons-material/Animation";
import IOperationButton, { sceneButtonStyle } from "../../OperationButton";
import {
  gridContainerStyle,
  gridItemStyle,
  sceneTitleStyle,
} from "../../../Styles/DialogStyles";
import { LightingRequest } from "../../../types";
import { post } from "../../../utils";
import config from "../../../config";

const sceneDialogDivStyle = {
  height: "100%",
  margin: "0px",
  minHeight: "100vh",
  background: "linear-gradient(#079BF6, #3A66B4)",
  // background: "linear-gradient(#ffffff, #9198e5)",
  // backgroundColor: "#151515",
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
    <div style={sceneDialogDivStyle}>
      <Box style={gridItemStyle}>
        <Typography style={sceneTitleStyle}>Select a Scene</Typography>
      </Box>
      <Grid container spacing={2} style={gridContainerStyle}>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Ocean"}
            style={sceneButtonStyle}
            onClick={onClickOcean}
            icon={<AnimationIcon></AnimationIcon>}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Rose"}
            style={sceneButtonStyle}
            onClick={onClickRose}
            icon={<AnimationIcon></AnimationIcon>}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Rainbow"}
            style={sceneButtonStyle}
            onClick={onClickRainbow}
            icon={<AnimationIcon></AnimationIcon>}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Candy"}
            style={sceneButtonStyle}
            onClick={onClickCandy}
            icon={<AnimationIcon></AnimationIcon>}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Peachy"}
            style={sceneButtonStyle}
            onClick={onClickPeachy}
            icon={<AnimationIcon></AnimationIcon>}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Jungle"}
            style={sceneButtonStyle}
            onClick={onClickJungle}
            icon={<AnimationIcon></AnimationIcon>}
          ></IOperationButton>
        </Grid>
      </Grid>
    </div>
  );
};

export default SceneDialog;
