import React, { FC, useState } from "react";
import { Box, Grid } from "@mui/material";
import { useTheme } from "@mui/material/styles";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import ColorWheel from "./ColorWheel";
import ColorChart from "./ColorChart";
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
  backgroundColor: "#2d3387", //1C2C54
  borderRadius: "10px",
};

const colorSelectionTabsStyle = {
  width: "100%",
  borderRadius: "10px",
  color: "#424242",
};

const gridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const tabLabelStyle = {
  fontSize: "16px",
  fontFamily: "Ubuntu, -apple-system",
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
            TabIndicatorProps={{
              style: {
                backgroundColor: "#FFFFFF",
              },
            }}
          >
            <Tab
              label={<span style={tabLabelStyle}>Chart</span>}
              {...a11yProps(0)}
            />
            <Tab
              label={<span style={tabLabelStyle}>Wheel</span>}
              {...a11yProps(1)}
            />
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
              <ColorChart
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
