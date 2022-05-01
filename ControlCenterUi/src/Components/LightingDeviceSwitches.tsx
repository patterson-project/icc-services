import { Box, Grid } from "@mui/material";
import Switch from "@mui/material/Switch";
import FormLabel from "@mui/material/FormLabel";
import FormControl from "@mui/material/FormControl";
import FormGroup from "@mui/material/FormGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import FormHelperText from "@mui/material/FormHelperText";
import React, { FC } from "react";

interface ILightingDeviceSwitches {
  onChange(value: boolean): void;
}

const LightingDeviceSwitchesStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  height: "50px",
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

//<Switch inputProps={{ "aria-label": "controlled" }} />

const LightingDeviceSwitches: FC<ILightingDeviceSwitches> = (
  props
): JSX.Element => {
  return (
    <Box style={LightingDeviceSwitchesStyle}>
      <Grid item xs={6} style={gridItemStyle}></Grid>
    </Box>
  );
};

export default LightingDeviceSwitches;
