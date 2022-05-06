import { Box, Grid, Typography } from "@mui/material";
import FormControlLabel from "@mui/material/FormControlLabel";
import React, { FC } from "react";
import { IosSwitch } from "./IosSwitch";
interface ILightingDeviceSwitches {
  setBulbOneTarget(value: boolean): void;
  setBulbTwoTarget(value: boolean): void;
  setLedStripTarget(value: boolean): void;
}

const lightingDeviceSwitchesStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  height: "auto",
  backgroundColor: "#3B3B3B",
  width: "90%",
  borderRadius: "10px",
  paddingBottom: "20px",
};

const gridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const switchLabelStyle = {
  fontSize: "15px",
  display: "flex",
  alignItems: "center",
  fontFamily: "Ubuntu, -apple-system",
  justifyContent: "center",
};

const formControlLabelStyle = {
  color: "white",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const switchTitleStyle = {
  color: "white",
  fontSize: "20px",
  marginTop: "10px",
  marginBottom: "5px",
  fontFamily: "Ubuntu, -apple-system",
  fontWeight: "bold",
};

const LightingDeviceSwitches: FC<ILightingDeviceSwitches> = (
  props
): JSX.Element => {
  const getLabelSpan = (label: string) => {
    return <span style={switchLabelStyle}>{label}</span>;
  };
  return (
    <Box style={lightingDeviceSwitchesStyle}>
      <Grid container rowSpacing={1.5}>
        <Grid item xs={12} style={gridItemStyle}>
          <Typography style={switchTitleStyle}>Target</Typography>
        </Grid>
        <Grid item xs={4} style={gridItemStyle}>
          <FormControlLabel
            style={formControlLabelStyle}
            control={
              <IosSwitch
                onChange={(event) =>
                  props.setBulbOneTarget(event.target.checked)
                }
              />
            }
            label={getLabelSpan("Bulb One")}
            labelPlacement="bottom"
          />
        </Grid>
        <Grid item xs={4} style={gridItemStyle}>
          <FormControlLabel
            style={formControlLabelStyle}
            control={
              <IosSwitch
                onChange={(event) =>
                  props.setBulbTwoTarget(event.target.checked)
                }
              />
            }
            label={getLabelSpan("Bulb Two")}
            labelPlacement="bottom"
          />
        </Grid>
        <Grid item xs={4} style={gridItemStyle}>
          <FormControlLabel
            style={formControlLabelStyle}
            control={
              <IosSwitch
                onChange={(event) =>
                  props.setLedStripTarget(event.target.checked)
                }
              />
            }
            label={getLabelSpan("Strip")}
            labelPlacement="bottom"
          />
        </Grid>
      </Grid>
    </Box>
  );
};

export default LightingDeviceSwitches;
