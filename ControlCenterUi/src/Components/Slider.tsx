import { Box, Grid, Slider as MuiSlider } from "@mui/material";
import React, { FC } from "react";

interface ISlider {
  onChange(value: number): void;
  startIcon: JSX.Element;
  endIcon: JSX.Element;
  min: number;
  max: number;
  defaultValue: number;
  step: number;
}

const brightnessBoxSliderStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  height: "50px",
  backgroundColor: "#3B3B3B",
  width: "90%",
  borderRadius: "10px",
};

const gridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const Slider: FC<ISlider> = (props): JSX.Element => {
  return (
    <Box style={brightnessBoxSliderStyle}>
      <Grid container spacing={2}>
        <Grid item xs={1} style={gridItemStyle}>
          {props.startIcon}
        </Grid>
        <Grid item xs={10} style={gridItemStyle}>
          <MuiSlider
            defaultValue={props.defaultValue}
            valueLabelDisplay="auto"
            min={props.min}
            max={props.max}
            step={props.step}
            onChangeCommitted={(_e, v) => props.onChange(v as number)}
          />
        </Grid>
        <Grid item xs={1} style={gridItemStyle}>
          {props.endIcon}
        </Grid>
      </Grid>
    </Box>
  );
};

export default Slider;
