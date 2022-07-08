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
  paddingBottom: "40px",
};

const onClickOcean = () => {
  const sceneRequest: LightingRequest = {
    operation: "ocean",
  };
  post(config.SCENE_ENDPOINT + "/ocean", sceneRequest);
};

const onClickRose = () => {
  const sceneRequest: LightingRequest = {
    operation: "rose",
  };
  post(config.SCENE_ENDPOINT + "/rose", sceneRequest);
};

const onClickRainbow = () => {
  const sceneRequest: LightingRequest = {
    operation: "rainbow",
  };
  post(config.SCENE_ENDPOINT + "/rainbow", sceneRequest);
};

const onClickCandy = () => {
  const sceneRequest: LightingRequest = {
    operation: "candy",
  };
  post(config.SCENE_ENDPOINT + "/candy", sceneRequest);
};

const onClickPeachy = () => {
  const sceneRequest: LightingRequest = {
    operation: "peachy",
  };
  post(config.SCENE_ENDPOINT + "/peachy", sceneRequest);
};

const onClickJungle = () => {
  const sceneRequest: LightingRequest = {
    operation: "jungle",
  };
  post(config.SCENE_ENDPOINT + "/jungle", sceneRequest);
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
