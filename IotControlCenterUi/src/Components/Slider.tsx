import { Box, Grid, Slider as MuiSlider, Typography } from "@mui/material";
import React, { FC } from "react";

interface ISlider {
  onChange(value: number): void;
  startIcon: JSX.Element;
  endIcon: JSX.Element;
  min: number;
  max: number;
  defaultValue: number;
  step: number;
  title?: string;
}

const brightnessBoxSliderStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  height: "100%",
  backgroundColor: "#3B3B3B",
  width: "90%",
  borderRadius: "10px",
  paddingBottom: "10px",
  paddingTop: "10px",
};

const gridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const sliderTitleStyle = {
  color: "white",
  fontSize: "20px",
  fontFamily: "Ubuntu, -apple-system",
  fontWeight: "bold",
};

const Slider: FC<ISlider> = (props): JSX.Element => {
  return (
    <Box style={brightnessBoxSliderStyle}>
      <Grid container spacing={2}>
        {props.title != null && (
          <Grid item xs={12} style={gridItemStyle}>
            <Typography style={sliderTitleStyle}>{props.title}</Typography>
          </Grid>
        )}
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
