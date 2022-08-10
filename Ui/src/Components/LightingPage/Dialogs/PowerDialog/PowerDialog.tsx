import { Devices, PropaneSharp } from "@mui/icons-material";
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
import { Device, LightingPowerStatus, State } from "../../../../types";
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
  const [buttonsDisabled, setButtonsDisabled] = useState<boolean>(true);
  const [deviceStates, setDeviceStates] = useState<Array<[Device, State]>>();

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
      let newDeviceStates: Array<[Device, State]> = [];
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
  }, []);

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
        <Grid item xs={12} style={gridItemStyle}>
          <PowerButton
            deviceName="Led Strip"
            onClick={() => onClickLedStripPower()}
            deviceState={ledStripState}
            disabled={buttonsDisabled}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <PowerButton
            deviceName="Bulb One"
            onClick={() => onClickBulbOnePower()}
            deviceState={bulbOneState}
            disabled={buttonsDisabled}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <PowerButton
            deviceName="Bulb Two"
            onClick={() => onClickBulbTwoPower()}
            deviceState={bulbTwoState}
            disabled={buttonsDisabled}
          />
        </Grid>
      </Grid>
    </div>
  );
};

export default PowerDialog;
