import { Box, Grid, Typography } from "@mui/material";
import React, { FC } from "react";
import {
  gridContainerStyle,
  gridItemStyle,
  subTitleStyle,
  textStyle,
  titleStyle,
} from "../../Styles/DialogStyles";
import LightbulbIcon from "@mui/icons-material/Lightbulb";

const cardBoxStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  height: "100%",
  backgroundColor: "#2C2C2E",
  width: "90%",
  borderRadius: "10px",
  paddingBottom: "10px",
};

const iconStyle = {
  color: "white",
};

const titleGridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "left",
};

const textGridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "left",
  paddingLeft: "15px",
};

interface IDeviceCard {
  deviceName: string;
  deviceIP: string;
  deviceModel: string;
}

const DeviceCard: FC<IDeviceCard> = (props): JSX.Element => {
  return (
    <Box style={cardBoxStyle}>
      <Grid container style={gridContainerStyle}>
        <Grid item xs={2} style={gridItemStyle}>
          <LightbulbIcon style={iconStyle}></LightbulbIcon>
        </Grid>
        <Grid item xs={10} style={titleGridItemStyle}>
          <Typography style={titleStyle}>{props.deviceName}</Typography>
        </Grid>
        <Grid item xs={12} style={textGridItemStyle}>
          <Typography style={textStyle}>{props.deviceModel}</Typography>
        </Grid>
        <Grid item xs={12} style={textGridItemStyle}>
          <Typography style={textStyle}>{props.deviceIP}</Typography>
        </Grid>
      </Grid>
    </Box>
  );
};

export default DeviceCard;
