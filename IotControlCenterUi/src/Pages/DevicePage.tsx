import { Grid, Typography } from "@mui/material";
import React, { FC } from "react";
import Fab from "@mui/material/Fab";
import AddIcon from "@mui/icons-material/Add";
import DeviceCard from "../Components/DevicePageComponents/DeviceCard";
import IccAppBar from "../Components/IccAppBar";
import { gridItemStyle, titleStyle } from "../Styles/DialogStyles";

const devicePageDivStyle = {
  height: "100%",
  margin: "0px",
  minHeight: "100vh",
  backgroundColor: "#151515",
};

const addDeviceButton = {
  position: "fixed",
  bottom: 16,
  right: 16,
};

const deviceGridContainerStyle = {
  marginTop: "0px",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  paddingBottom: "15px",
};

const DevicePage: FC = () => {
  return (
    <div style={devicePageDivStyle}>
      <IccAppBar />
      <Grid container spacing={2} style={deviceGridContainerStyle}>
        <Grid item xs={12} style={gridItemStyle}>
          <Typography style={titleStyle}>Devices</Typography>
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <DeviceCard
            deviceName="Bed Lamp"
            deviceModel="TP-Link Kasa Smart Bulb"
            deviceIP="10.0.0.37"
            deviceType="Lighting"
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <DeviceCard
            deviceName="Bed Lamp"
            deviceModel="TP-Link Kasa Smart Bulb"
            deviceIP="10.0.0.37"
            deviceType="Lighting"
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <DeviceCard
            deviceName="Bed Lamp"
            deviceModel="TP-Link Kasa Smart Bulb"
            deviceIP="10.0.0.37"
            deviceType="Lighting"
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <DeviceCard
            deviceName="Bed Lamp"
            deviceModel="TP-Link Kasa Smart Bulb"
            deviceIP="10.0.0.37"
            deviceType="Lighting"
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <DeviceCard
            deviceName="Bed Lamp"
            deviceModel="TP-Link Kasa Smart Bulb"
            deviceIP="10.0.0.37"
            deviceType="Lighting"
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <DeviceCard
            deviceName="Bed Lamp"
            deviceModel="TP-Link Kasa Smart Bulb"
            deviceIP="10.0.0.37"
            deviceType="Lighting"
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <DeviceCard
            deviceName="Bed Lamp"
            deviceModel="TP-Link Kasa Smart Bulb"
            deviceIP="10.0.0.37"
            deviceType="Lighting"
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <DeviceCard
            deviceName="Bed Lamp"
            deviceModel="TP-Link Kasa Smart Bulb"
            deviceIP="10.0.0.37"
            deviceType="Lighting"
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <DeviceCard
            deviceName="Bed Lamp"
            deviceModel="TP-Link Kasa Smart Bulb"
            deviceIP="10.0.0.37"
            deviceType="Lighting"
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <DeviceCard
            deviceName="Bed Lamp"
            deviceModel="TP-Link Kasa Smart Bulb"
            deviceIP="10.0.0.37"
            deviceType="Lighting"
          />
        </Grid>
      </Grid>
      <Fab color="primary" aria-label="add" sx={addDeviceButton}>
        <AddIcon />
      </Fab>
    </div>
  );
};

export default DevicePage;
