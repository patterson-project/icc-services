import React, { FC, useState } from "react";
import { Box, Grid } from "@mui/material";
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import ColorWheel from "./ColorWheel";
import ColorPicker from "./ColorPicker";

const colorPickerBoxStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  width: "340px",
  height: "400px",
  backgroundColor: "#3B3B3B",
  borderRadius: "10px",
};

const colorSelectionTabsStyle = {
  width: "340px"
};

const ColorSelectionTab: FC = () => {
    const [colorSelectionMethod, setColorSelectionMethod] = useState(0);
    const tabComponents = [<ColorWheel/>,  <ColorPicker/>];

    const handleColorSelectionMethodChange = (event: React.SyntheticEvent, newValue: number) => {
        setColorSelectionMethod(newValue);
    };

    return (
        <Box style={colorPickerBoxStyle}>
            <Grid container>
              <Grid item xs={12}>
                {tabComponents[colorSelectionMethod]}
              </Grid>
              <Grid item xs={12}>
                <Tabs style={colorSelectionTabsStyle} value={colorSelectionMethod} onChange={handleColorSelectionMethodChange} variant="fullWidth">
                    <Tab label="Wheel" />
                    <Tab label="Chart"/>
                </Tabs>
              </Grid>
              
            </Grid>
        </Box>
    );
};

export default ColorSelectionTab;