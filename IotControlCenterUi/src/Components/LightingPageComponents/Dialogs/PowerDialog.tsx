import { Box, Divider, Grid, Typography } from "@mui/material";
import React, { FC, useEffect, useState } from "react";
import config from "../../../config";
import {
  gridContainerStyle,
  gridItemStyle,
  pageDivStyle,
  titleStyle,
} from "../../../Styles/DialogStyles";
import { LightingPowerStatus, LightingRequest } from "../../../types";
import { post, useDidMountEffect } from "../../../utils";
import PowerButton from "../LightingComponents/PowerButton";

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

const PowerDialog: FC = () => {
  const [bulbOneState, setBulbOneState] = useState<boolean>(false);
  const [bulbTwoState, setBulbTwoState] = useState<boolean>(false);
  const [ledStripState, setLedStripState] = useState<boolean>(false);

  useEffect(() => {
    const fetchPowerStatus = async (
      url: string
    ): Promise<LightingPowerStatus> => {
      return fetch(url, {
        method: "GET",
      })
        .then((response) => response.json())
        .then((response) => {
          return response as LightingPowerStatus;
        });
    };

    const setPowerStates = async () => {
      const bulbOnePowerStatus: LightingPowerStatus = await fetchPowerStatus(
        config.BULB_1_ENDPOINT + "/status/on"
      );
      const bulbTwoPowerStatus: LightingPowerStatus = await fetchPowerStatus(
        config.BULB_2_ENDPOINT + "/status/on"
      );
      const ledStripPowerStatus: LightingPowerStatus = await fetchPowerStatus(
        config.LED_STRIP_ENDPOINT + "/status/on"
      );

      setBulbOneState(bulbOnePowerStatus.on);
      setBulbTwoState(bulbTwoPowerStatus.on);
      setLedStripState(ledStripPowerStatus.on);
    };

    setPowerStates();
  });

  useDidMountEffect(() => {
    const powerRequest: LightingRequest = {
      operation: bulbOneState ? "on" : "off",
    };

    post(config.BULB_1_ENDPOINT, powerRequest);
  }, [bulbOneState]);

  useDidMountEffect(() => {
    const powerRequest: LightingRequest = {
      operation: bulbTwoState ? "on" : "off",
    };

    post(config.BULB_2_ENDPOINT, powerRequest);
  }, [bulbTwoState]);

  useDidMountEffect(() => {
    const powerRequest: LightingRequest = {
      operation: ledStripState ? "on" : "off",
    };

    post(config.LED_STRIP_ENDPOINT, powerRequest);
  }, [ledStripState]);

  return (
    <div style={pageDivStyle}>
      <Box style={gridItemStyle}>
        <Typography style={titleStyle}>Power</Typography>
      </Box>
      <Divider variant="middle" style={{ backgroundColor: "#555555" }} />
      <Box style={categoryTitleBoxStyle}>
        <Typography style={categoryTitleStyle}>Bedroom</Typography>
      </Box>
      <Grid container spacing={1.5} style={gridContainerStyle}>
        <Grid item xs={12} style={gridItemStyle}>
          <PowerButton
            deviceName="Led Strip"
            onClick={() => setLedStripState(!ledStripState)}
            deviceState={ledStripState}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <PowerButton
            deviceName="Bulb One"
            onClick={() => setBulbOneState(!bulbOneState)}
            deviceState={bulbOneState}
          />
        </Grid>
        <Grid item xs={12} style={gridItemStyle}>
          <PowerButton
            deviceName="Bulb Two"
            onClick={() => setBulbTwoState(!bulbTwoState)}
            deviceState={bulbTwoState}
          />
        </Grid>
      </Grid>
    </div>
  );
};

export default PowerDialog;
