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
import { Device, LightingRequest, State } from "../../../../types";
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
  const [deviceStates, setDeviceStates] = useState<State[]>([]);

  useEffect(() => {
    const fetchPowerStates = async () => {
      return fetch(config.DEVICE_MANAGER_ENDPOINT + "/states", {
        method: "GET",
      })
        .then((response) => {
          if (!response.ok) {
            console.log("Failed to fetch states");
          } else {
            return response.json();
          }
        })
        .then((response) => {
          setDeviceStates(response as State[]);
        });
    };

    fetchPowerStates();

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => console.log("CHANGED"), [deviceStates]);

  const onClickPowerButton = (state: State) => {
    const device = props.devices.find((device) => device._id === state.device);

    let operation: string;
    if (state.state) {
      operation = "off";
    } else {
      operation = "on";
    }

    const lightingRequest: LightingRequest = {
      target: state.device,
      operation: operation,
    };

    let url: string = "";
    if (device?.model === "Kasa Bulb") {
      url = config.BULB_ENDPOINT;
    } else if (device?.model === "Custom Led Strip") {
      url = config.CUSTOM_LED_STRIP_ENDPOINT;
    }

    fetch(url + "/request", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(lightingRequest),
    })
      .then((response) => {
        if (!response.ok) {
          console.log("Failed to set device power state");
        }
      })
      .then(async () => {
        let newStates: State[] | undefined = [...deviceStates];
        const stateIndex = deviceStates?.findIndex((s) => s._id === state._id);
        if (newStates !== undefined && stateIndex !== undefined) {
          state.state = !state.state;
          newStates[stateIndex] = state;

          console.log(`New States: ${JSON.stringify(newStates)}`);
          setDeviceStates(newStates);
        }
      });
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
        {deviceStates.map((state) => {
          const device: Device | undefined = props.devices.find(
            (device) => device._id === state.device
          );
          return (
            <Grid item xs={12} style={gridItemStyle}>
              <PowerButton
                deviceName={device?.name ?? ""}
                onClick={() => onClickPowerButton(state)}
                deviceState={state.state}
              />
            </Grid>
          );
        })}
      </Grid>
    </div>
  );
};

export default PowerDialog;
