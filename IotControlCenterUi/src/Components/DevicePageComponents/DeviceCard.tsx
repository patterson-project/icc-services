import { Box, Grid, IconButton, Typography } from "@mui/material";
import React, { FC } from "react";
import {
  gridContainerStyle,
  gridItemStyle,
  textStyle,
} from "../../Styles/DialogStyles";
import LightbulbIcon from "@mui/icons-material/Lightbulb";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";

const cardBoxStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  height: "100%",
  backgroundColor: "#2C2C2E",
  width: "90%",
  borderRadius: "10px",
  paddingBottom: "10px",
  overflow: "auto",
  animation: "ripple 1s",
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

const cardTitleStyle = {
  color: "white",
  fontSize: "30px",
  fontFamily: "Ubuntu, -apple-system",
  fontWeight: "bold",
};

interface IDeviceCard {
  deviceName: string;
  deviceIP: string;
  deviceModel: string;
  deviceType: string;
}

const DeviceCard: FC<IDeviceCard> = (props): JSX.Element => {
  const onClickCard = () => {
    console.log("Clicked");
  };

  return (
    <Box style={cardBoxStyle} onClick={onClickCard}>
      <Grid container style={gridContainerStyle}>
        <Grid item xs={10}>
          <Grid container style={gridContainerStyle}>
            <Grid item xs={2} style={gridItemStyle}>
              <LightbulbIcon style={iconStyle}></LightbulbIcon>
            </Grid>
            <Grid item xs={10} style={titleGridItemStyle}>
              <Typography style={cardTitleStyle}>{props.deviceName}</Typography>
            </Grid>
            <Grid item xs={12} style={textGridItemStyle}>
              <Typography style={textStyle}>{props.deviceModel}</Typography>
            </Grid>
            <Grid item xs={12} style={textGridItemStyle}>
              <Typography style={textStyle}>{props.deviceIP}</Typography>
            </Grid>
          </Grid>
        </Grid>
        <Grid item xs={2}>
          <IconButton size="medium">
            <DeleteIcon style={iconStyle} />
          </IconButton>
          <IconButton size="medium">
            <EditIcon style={iconStyle} />
          </IconButton>
        </Grid>
      </Grid>
    </Box>
  );
};

export default DeviceCard;
