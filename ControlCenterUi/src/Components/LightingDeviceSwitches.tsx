import { Box, Grid } from "@mui/material";
import Switch from "@mui/material/Switch";
import FormControlLabel from "@mui/material/FormControlLabel";
import React, { FC } from "react";

interface ILightingDeviceSwitches {
  setBulbOneTarget(value: boolean): void;
  setBulbTwoTarget(value: boolean): void;
  setLedStripTarget(value: boolean): void;
}

const LightingDeviceSwitchesStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "space-evenly",
  height: "120px",
  backgroundColor: "#3B3B3B",
  width: "320px",
  paddingLeft: "10px",
  paddingRight: "10px",
  borderRadius: "10px",
};

const gridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const singleSwitchItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "start",
  paddingLeft: "25px",
};

const switchLabelStyle = {
  fontSize: "20px",
};

const switchStyle = {
  color: "white",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const LightingDeviceSwitches: FC<ILightingDeviceSwitches> = (
  props
): JSX.Element => {
  const getLabelSpan = (label: string) => {
    return <span style={switchLabelStyle}>{label}</span>;
  };
  return (
    <Box style={LightingDeviceSwitchesStyle}>
      <Grid container columnSpacing={2} rowSpacing={2}>
        <Grid item xs={6} style={gridItemStyle}>
          <FormControlLabel
            style={switchStyle}
            control={
              <Switch
                onChange={(event) =>
                  props.setBulbOneTarget(event.target.checked)
                }
              />
            }
            label={getLabelSpan("Bulb One")}
          />
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <FormControlLabel
            style={switchStyle}
            control={
              <Switch
                onChange={(event) =>
                  props.setBulbTwoTarget(event.target.checked)
                }
              />
            }
            label={getLabelSpan("Bulb Two")}
          />
        </Grid>
        <Grid item xs={6} style={singleSwitchItemStyle}>
          <FormControlLabel
            style={switchStyle}
            control={
              <Switch
                onChange={(event) =>
                  props.setLedStripTarget(event.target.checked)
                }
              />
            }
            label={getLabelSpan("Strip")}
          />
        </Grid>
      </Grid>
    </Box>
  );
};

export default LightingDeviceSwitches;
