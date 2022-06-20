import { Box, Grid, Typography } from "@mui/material";
import React, { FC } from "react";
import AnimationIcon from "@mui/icons-material/Animation";
import IOperationButton from "../../OperationButton";
import {
  gridContainerStyle,
  gridItemStyle,
  titleStyle,
} from "../../../Styles/DialogStyles";
import { LightingRequest } from "../../../types";
import { post } from "../../../utils";
import config from "../../../config";

const sceneDialogDivStyle = {
  height: "100%",
  margin: "0px",
  minHeight: "100vh",
  backgroundColor: "#151515",
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
        <Typography style={titleStyle}>Scenes</Typography>
      </Box>
      <Grid container spacing={2} style={gridContainerStyle}>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Ocean"}
            onClick={onClickOcean}
            icon={<AnimationIcon></AnimationIcon>}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Rose"}
            onClick={onClickRose}
            icon={<AnimationIcon></AnimationIcon>}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Rainbow"}
            onClick={onClickRainbow}
            icon={<AnimationIcon></AnimationIcon>}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Candy"}
            onClick={onClickCandy}
            icon={<AnimationIcon></AnimationIcon>}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Peachy"}
            onClick={onClickPeachy}
            icon={<AnimationIcon></AnimationIcon>}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Jungle"}
            onClick={onClickJungle}
            icon={<AnimationIcon></AnimationIcon>}
          ></IOperationButton>
        </Grid>
      </Grid>
    </div>
  );
};

export default SceneDialog;
