import { Box, Grid, styled } from "@mui/material";
import Switch, { SwitchProps } from "@mui/material/Switch";
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

const IOSSwitch = styled((props: SwitchProps) => (
  <Switch focusVisibleClassName=".Mui-focusVisible" disableRipple {...props} />
))(({ theme }) => ({
  width: 42,
  height: 26,
  padding: 0,
  "& .MuiSwitch-switchBase": {
    padding: 0,
    margin: 2,
    transitionDuration: "300ms",
    "&.Mui-checked": {
      transform: "translateX(16px)",
      color: "#fff",
      "& + .MuiSwitch-track": {
        backgroundColor: theme.palette.mode === "dark" ? "#2ECA45" : "#65C466",
        opacity: 1,
        border: 0,
      },
      "&.Mui-disabled + .MuiSwitch-track": {
        opacity: 0.5,
      },
    },
    "&.Mui-focusVisible .MuiSwitch-thumb": {
      color: "#33cf4d",
      border: "6px solid #fff",
    },
    "&.Mui-disabled .MuiSwitch-thumb": {
      color:
        theme.palette.mode === "light"
          ? theme.palette.grey[100]
          : theme.palette.grey[600],
    },
    "&.Mui-disabled + .MuiSwitch-track": {
      opacity: theme.palette.mode === "light" ? 0.7 : 0.3,
    },
  },
  "& .MuiSwitch-thumb": {
    boxSizing: "border-box",
    width: 22,
    height: 22,
  },
  "& .MuiSwitch-track": {
    borderRadius: 26 / 2,
    backgroundColor: theme.palette.mode === "light" ? "#E9E9EA" : "#39393D",
    opacity: 1,
    transition: theme.transitions.create(["background-color"], {
      duration: 500,
    }),
  },
}));

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
              <IOSSwitch
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
              <IOSSwitch
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
              <IOSSwitch
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
