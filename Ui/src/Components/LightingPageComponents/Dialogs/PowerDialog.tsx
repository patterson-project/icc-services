import { Box, Divider, Grid, Typography } from "@mui/material";
import React, { FC, useEffect, useState } from "react";
import config from "../../../config";
import {
  gridContainerStyle,
  gridItemStyle,
  pageDivStyle,
  subHeadingStyle,
  titleStyle,
} from "../../../Styles/DialogStyles";
import { LightingPowerStatus, LightingRequest } from "../../../types";
import { post } from "../../../utils";
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
  const [buttonsDisabled, setButtonsDisabled] = useState<boolean>(true);

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
    setButtonsDisabled(false);
  }, []);

  const onClickBulbOnePower = () => {
    setBulbOneState(!bulbOneState);
    const powerRequest: LightingRequest = {
      operation: bulbOneState ? "off" : "on",
    };

    post(config.BULB_1_ENDPOINT + "/request", powerRequest);
  };

  const onClickBulbTwoPower = () => {
    setBulbTwoState(!bulbTwoState);
    const powerRequest: LightingRequest = {
      operation: bulbTwoState ? "off" : "on",
    };

    post(config.BULB_2_ENDPOINT + "/request", powerRequest);
  };

  const onClickLedStripPower = () => {
    setLedStripState(!ledStripState);
    const powerRequest: LightingRequest = {
      operation: ledStripState ? "off" : "on",
    };

    post(config.LED_STRIP_ENDPOINT + "/request", powerRequest);
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
