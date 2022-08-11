import { Box, Divider, Grid, Typography } from "@mui/material";
import React, { FC, useEffect, useState } from "react";
import config from "../../../../config";
import {
  gridContainerStyle,
  gridItemStyle,
  pageDivStyle,
  subHeadingStyle,
  titleStyle,
} from "../../../../Styles/CommonStyles";
import { Device, State } from "../../../../types";
import { post } from "../../../../utils";
import PowerButton from "./PowerButton";

interface IPowerDialog {
  devices: Device[];
}

const categoryTitleBoxStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "left",
  marginLeft: "8%",
  paddingTop: "5px",
};

const categoryTitleStyle = {
  color: "white",
  fontSize: "25px",
  fontFamily: "Ubuntu, -apple-system",
  fontWeight: "bold",
};

const PowerDialog: FC<IPowerDialog> = (props) => {
  const [deviceStates, setDeviceStates] = useState<[Device, State][]>();

  useEffect(() => {
    const fetchPowerStates = async (): Promise<State[]> => {
      return fetch(config.DEVICE_MANAGER_ENDPOINT + "/states", {
        method: "GET",
      })
        .then((response) => response.json())
        .then((response) => {
          return response as State[];
        });
    };

    const mergeDeviceStates = async () => {
      const states: State[] = await fetchPowerStates();
      let newDeviceStates: [Device, State][] = [];
      for (let i = 0; i < props.devices.length; i++) {
        newDeviceStates.push([
          props.devices[i],
          states.find(
            (state) => state.device === props.devices[i]._id
          ) as State,
        ]);
      }
      setDeviceStates(newDeviceStates);
    };

    mergeDeviceStates();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const onClickPowerButton = (deviceState: [Device, State]) => {
    deviceState[1].state = !deviceState[1].state;
    post(config.DEVICE_MANAGER_ENDPOINT + "/states", deviceState[1]);
    if (deviceStates) {
      deviceStates[
        deviceStates.findIndex((ds) => deviceState[0]._id === ds[0]._id)
      ] = deviceState;
      setDeviceStates(deviceStates);
    }
  };

  return (
    <div style={pageDivStyle}>
      <Box style={gridItemStyle}>
        <Typography style={titleStyle}>Power</Typography>
      </Box>
      <Box style={gridItemStyle}>
        <Typography style={subHeadingStyle}>Control your devices</Typography>
      </Box>
      <Divider variant="middle" style={{ backgroundColor: "#555555" }} />
      <Box style={categoryTitleBoxStyle}>
        <Typography style={categoryTitleStyle}>Bedroom</Typography>
      </Box>
      <Grid container spacing={1.5} style={gridContainerStyle}>
        {deviceStates?.map((deviceState) => {
          return (
            <Grid item xs={12} style={gridItemStyle}>
              <PowerButton
                deviceName={deviceState[0].name}
                onClick={() => onClickPowerButton(deviceState)}
                deviceState={deviceState[1].state}
              />
            </Grid>
          );
        })}
      </Grid>
    </div>
  );
};

export default PowerDialog;
