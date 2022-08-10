import { Box, Grid, Typography } from "@mui/material";
import FormControlLabel from "@mui/material/FormControlLabel";
import React, { FC } from "react";
import { Device } from "../../../../types";
import { IosSwitch } from "../../../Common/IosSwitch";
interface ILightingDeviceSwitch {
  devices: Device[];
  targetDevices: Device[] | undefined;
  setTargetDevices: (targets: Device[]) => void;
}

const lightingDeviceSwitchesStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  height: "auto",
  backgroundColor: "#2C2C2E",
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

const LightingDeviceSwitch: FC<ILightingDeviceSwitch> = (
  props
): JSX.Element => {
  const getLabelSpan = (label: string) => {
    return <span style={switchLabelStyle}>{label}</span>;
  };
  return (
    <Box style={lightingDeviceSwitchesStyle}>
      <Grid container rowSpacing={1.5}>
        <Grid item xs={12} style={gridItemStyle}>
          <Typography style={switchTitleStyle}>Device</Typography>
        </Grid>
        {props.devices?.map((device) => {
          return (
            <Grid item xs={4} style={gridItemStyle}>
              <FormControlLabel
                style={formControlLabelStyle}
                control={
                  <IosSwitch
                    onChange={(event) => {
                      if (event.target.checked) {
                        const newTargets = props.targetDevices?.concat(
                          device as Device
                        ) as Device[];
                        props.setTargetDevices(newTargets);
                      } else {
                        const newTargets = props.targetDevices?.filter(
                          (target) => {
                            return target._id !== device._id;
                          }
                        ) as Device[];
                        props.setTargetDevices(newTargets);
                      }

                      console.log(`${props.targetDevices}`);
                    }}
                  />
                }
                label={getLabelSpan(device.name)}
                labelPlacement="bottom"
              />
            </Grid>
          );
        })}
      </Grid>
    </Box>
  );
};

export default LightingDeviceSwitch;
