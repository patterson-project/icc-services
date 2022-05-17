import { Box, Divider, Grid, Typography } from "@mui/material";
import React, { FC, useEffect, useState } from "react";
import config from "../../../config";
import {
  gridContainerStyle,
  gridItemStyle,
  pageDivStyle,
  titleStyle,
} from "../../../Styles/DialogStyles";
import { LightingRequest } from "../../../types";
import { post } from "../../../utils";
import PowerButton from "../LightingComponents/PowerButton";

const categoryTitleStyle = {
  color: "white",
  fontSize: "25px",
  fontFamily: "Ubuntu, -apple-system",
  fontWeight: "bold",
};

const PowerDialog: FC = () => {
  const [bulbOneState, setBulbOneState] = useState(true);
  const [bulbTwoState, setBulbTwoState] = useState(true);
  const [ledStripState, setLedStripState] = useState(true);

  useEffect(() => {
    const powerRequest: LightingRequest = {
      operation: bulbOneState ? "on" : "off",
    };

    post(config.BULB_1_ENDPOINT, powerRequest);
  }, [bulbOneState]);

  useEffect(() => {
    const powerRequest: LightingRequest = {
      operation: bulbTwoState ? "on" : "off",
    };

    post(config.BULB_2_ENDPOINT, powerRequest);
  }, [bulbTwoState]);

  useEffect(() => {
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
      <Box style={gridItemStyle}>
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
