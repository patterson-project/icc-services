import { Grid, Typography } from "@mui/material";
import React, { FC, useEffect, useState } from "react";
import DeviceCard from "./DeviceCard";
import IccAppBar from "../Common/IccAppBar";
import { gridItemStyle, titleStyle } from "../../Styles/CommonStyles";
import AddDeviceModal from "./AddDeviceModal";
import { Device } from "../../types";
import config from "../../config";

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
  const [devices, setDevices] = useState<Device[]>([]);

  useEffect(() => {
    fetch(config.DEVICE_MANAGER_ENDPOINT, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((data) => {
        setDevices(data as Device[]);
      });
  }, []);

  return (
    <div style={devicePageDivStyle}>
      <IccAppBar />
      <Grid container spacing={2} style={deviceGridContainerStyle}>
        <Grid item xs={12} style={gridItemStyle}>
          <Typography style={titleStyle}>Devices</Typography>
        </Grid>
        {devices?.map((device) => (
          <Grid item xs={12} style={gridItemStyle}>
            <DeviceCard
              devices={devices}
              setDevices={setDevices}
              deviceId={device._id}
              deviceName={device.name}
              deviceModel={device.model}
              deviceIp={device.ip}
              deviceType={device.type}
            />
          </Grid>
        ))}
      </Grid>
      <AddDeviceModal devices={devices} setDevices={setDevices} />
    </div>
  );
};

export default DevicePage;
