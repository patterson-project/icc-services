import { Box, Grid, IconButton, Typography } from "@mui/material";
import React, { FC } from "react";
import { gridContainerStyle, textStyle } from "../../Styles/CommonStyles";
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
};

const iconStyle = {
  color: "white",
  fontSize: "23px",
  paddingTop: "2px",
};

const textGridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "left",
  paddingLeft: "20px",
};

const deviceTitleGridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "start",
};

const deviceInfoGridContainerStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  paddingLeft: "18px",
};

const cardTitleStyle = {
  color: "white",
  fontSize: "24px",
  fontFamily: "Ubuntu, -apple-system",
  fontWeight: "medium",
  paddingLeft: "8px",
};

interface IDeviceCard {
  deviceName: string;
  deviceIp: string;
  deviceModel: string;
  deviceType: string;
}

const DeviceCard: FC<IDeviceCard> = (props): JSX.Element => {
  return (
    <Box style={cardBoxStyle}>
      <Grid container style={gridContainerStyle}>
        <Grid item xs={10}>
          <Grid container>
            <Grid container style={deviceInfoGridContainerStyle}>
              <Grid item xs={12} style={deviceTitleGridItemStyle}>
                <LightbulbIcon style={iconStyle}></LightbulbIcon>
                <Typography style={cardTitleStyle}>
                  {props.deviceName}
                </Typography>
              </Grid>
            </Grid>
            <Grid item xs={12} style={textGridItemStyle}>
              <Typography style={textStyle}>{props.deviceModel}</Typography>
            </Grid>
            <Grid item xs={12} style={textGridItemStyle}>
              <Typography style={textStyle}>{props.deviceIp}</Typography>
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
