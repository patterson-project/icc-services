import React, { FC, useState } from "react";
import { Box, Grid } from "@mui/material";
import { useTheme } from "@mui/material/styles";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import ColorWheel from "./ColorWheel";
import ColorPicker from "./ColorPicker";
import SwipeableViews from "react-swipeable-views";

interface IColorSelectionTab {
  ledStripTarget: boolean;
  bulbOneTarget: boolean;
  bulbTwoTarget: boolean;
}

const colorPickerBoxStyle = {
  display: "flex",
  alignItems: "top",
  justifyContent: "center",
  width: "90%",
  height: "390px",
  backgroundColor: "#3B3B3B",
  borderRadius: "10px",
};

const colorSelectionTabsStyle = {
  width: "100%",
  borderRadius: "10px",
};

const gridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

interface ITabPanel {
  children?: React.ReactNode;
  dir?: string;
  index: number;
  value: number;
}

function TabPanel(props: ITabPanel) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`full-width-tabpanel-${index}`}
      aria-labelledby={`full-width-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Grid item xs={12}>
          {children}
        </Grid>
      )}
    </div>
  );
}

function a11yProps(index: number) {
  return {
    id: `full-width-tab-${index}`,
    "aria-controls": `full-width-tabpanel-${index}`,
  };
}

const ColorSelectionTab: FC<IColorSelectionTab> = (props): JSX.Element => {
  const theme = useTheme();
  const [value, setValue] = useState(0);
  const [modifyingColor, setModifyingColor] = useState(false);

  const handleChange = (_event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  const handleChangeIndex = (index: number) => {
    setValue(index);
  };

  return (
    <Box style={colorPickerBoxStyle}>
      <Grid container>
        <Grid item xs={12}>
          <Tabs
            style={colorSelectionTabsStyle}
            value={value}
            onChange={handleChange}
            variant="fullWidth"
          >
            <Tab label="Chart" {...a11yProps(0)} />
            <Tab label="Wheel" {...a11yProps(1)} />
          </Tabs>
        </Grid>
        <Grid style={gridItemStyle} item xs={12}>
          <SwipeableViews
            axis={theme.direction === "rtl" ? "x-reverse" : "x"}
            index={value}
            onChangeIndex={handleChangeIndex}
            disabled={modifyingColor}
          >
            <TabPanel value={value} index={0} dir={theme.direction}>
              <ColorPicker
                ledStripTarget={props.ledStripTarget}
                bulbOneTarget={props.bulbOneTarget}
                bulbTwoTarget={props.bulbTwoTarget}
                setModifyingColor={setModifyingColor}
              />
            </TabPanel>
            <TabPanel value={value} index={1} dir={theme.direction}>
              <ColorWheel
                ledStripTarget={props.ledStripTarget}
                bulbOneTarget={props.bulbOneTarget}
                bulbTwoTarget={props.bulbTwoTarget}
                setModifyingColor={setModifyingColor}
              />
            </TabPanel>
          </SwipeableViews>
        </Grid>
      </Grid>
    </Box>
  );
};

export default ColorSelectionTab;
