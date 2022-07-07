import PowerSettingsNewIcon from "@mui/icons-material/PowerSettingsNew";
import { Box, Grid, IconButton, Typography } from "@mui/material";
import React, { FC } from "react";
import {
  componentBoxStyle,
  gridContainerStyle,
  gridItemStyle,
  subHeadingStyle,
} from "../../../Styles/DialogStyles";

interface IPowerButton {
  deviceName: string;
  deviceIP: string;
  onClick(): void;
  deviceState: boolean;
  disabled: boolean;
}

const powerButtonOnIconStyle = {
  color: "white",
  fontSize: "70px",
};

const powerButtonOffIconStyle = {
  color: "black",
  fontSize: "70px",
};

const deviceNameStyle = {
  color: "white",
  fontSize: "25px",
  fontFamily: "Ubuntu, -apple-system",
};

const PowerButton: FC<IPowerButton> = (props): JSX.Element => {
  return (
    <Box style={componentBoxStyle}>
      <Grid container style={gridContainerStyle}>
        <Grid item xs={6} style={gridItemStyle}>
          <Typography style={deviceNameStyle}>{props.deviceName}</Typography>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <Typography style={subHeadingStyle}>{props.deviceIP}</Typography>
        </Grid>
        <Grid item xs={6} style={gridItemStyle}>
          <IconButton
            color="primary"
            disabled={props.disabled}
            onClick={() => props.onClick()}
          >
            {props.deviceState ? (
              <PowerSettingsNewIcon style={powerButtonOnIconStyle} />
            ) : (
              <PowerSettingsNewIcon style={powerButtonOffIconStyle} />
            )}
          </IconButton>
        </Grid>
      </Grid>
    </Box>
  );
};

export default PowerButton;
