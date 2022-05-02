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
  justifyContent: "center",
  height: "80px",
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

const switchLabelStyle = {
  fontSize: "15px",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const formControlLabelStyle = {
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
      <Grid container rowSpacing={1.5}>
        <Grid item xs={4} style={gridItemStyle}>
          <FormControlLabel
            style={formControlLabelStyle}
            control={
              <Switch
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
              <Switch
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
              <Switch
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
