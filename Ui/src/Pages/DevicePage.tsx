import { Grid, Typography } from "@mui/material";
import React, { FC } from "react";

import DeviceCard from "../Components/DevicePageComponents/DeviceCard";
import IccAppBar from "../Components/IccAppBar";
import { gridItemStyle, titleStyle } from "../Styles/DialogStyles";
import AddDeviceModal from "../Components/DevicePageComponents/AddDeviceModal";

const devicePageDivStyle = {
  height: "100%",
  margin: "0px",
  minHeight: "100vh",
  backgroundColor: "#151515",
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
      <AddDeviceModal />
    </div>
  );
};

export default DevicePage;
