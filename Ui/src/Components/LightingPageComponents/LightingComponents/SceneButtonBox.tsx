import { Box, Grid } from "@mui/material";
import React, { FC } from "react";
import config from "../../../config";
import {
  gridContainerStyle,
  gridItemStyle,
} from "../../../Styles/DialogStyles";
import { LightingRequest } from "../../../types";
import { post } from "../../../utils";
import IOperationButton from "../../OperationButton";

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

const SceneButtonBox: FC = () => {
  return (
    <Box style={buttonBoxStyle}>
      <Grid container spacing={2} style={gridContainerStyle}>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Ocean"}
            color={"#2a5cd1"}
            onClick={onClickOcean}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Rose"}
            color={"#f368f7"}
            onClick={onClickRose}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Candy"}
            color={"#ab5dc7"}
            onClick={onClickCandy}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Rainbow"}
            image={"url(/image.png)"}
            onClick={onClickRainbow}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Peachy"}
            color={"#f09f48"}
            onClick={onClickPeachy}
          ></IOperationButton>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IOperationButton
            operationName={"Jungle"}
            color={"#227a1c"}
            onClick={onClickJungle}
          ></IOperationButton>
        </Grid>
      </Grid>
    </Box>
  );
};

export default SceneButtonBox;
