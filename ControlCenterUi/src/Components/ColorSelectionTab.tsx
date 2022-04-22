import React, { FC, useState } from "react";
import { Box, Grid } from "@mui/material";
import { useTheme } from '@mui/material/styles';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import ColorWheel from "./ColorWheel";
import ColorPicker from "./ColorPicker";
import SwipeableViews from "react-swipeable-views";
import {useSwipeable} from "react-swipeable";

const colorPickerBoxStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  width: "340px",
  height: "390px",
  backgroundColor: "#3B3B3B",
  borderRadius: "10px",
};

const colorSelectionTabsStyle = {
  width: "340px",
};

const colorSelectionTabsGridStyle = {
  borderRadius: "10px"
};

const swipeConfig = {
  preventDefaultTouchmoveEvent: false
};

const swipeStyle = {
  touchAction: 'pan-y'
};

interface TabPanelProps {
  children?: React.ReactNode;
  dir?: string;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
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
    'aria-controls': `full-width-tabpanel-${index}`,
  };
}

const ColorSelectionTab: FC = () => {
    const theme = useTheme();
    const [value, setValue] = useState(0);
    const [modifyingColor, setModifyingColor] = useState(false);

    const handleChange = (event: React.SyntheticEvent, newValue: number) => {
      setValue(newValue);
    };

    const handleChangeIndex = (index: number) => {
      setValue(index);
    };

    const swipeHandler = useSwipeable({
      onSwiped: (eventData) => console.log("User Swiped!", eventData),
      ...swipeConfig,
    });

    return (
        <Box style={colorPickerBoxStyle}>
            <Grid container>
              <Grid style={colorSelectionTabsGridStyle} item xs={12}>
                <Tabs style={colorSelectionTabsStyle} value={value} onChange={handleChange} variant="fullWidth">
                    <Tab label="Wheel" {...a11yProps(0)}/>
                    <Tab label="Chart" {...a11yProps(1)}/>
                </Tabs>
              </Grid>
              <Grid item xs={12}>
                <div {...swipeHandler} style={swipeStyle}>
                  <SwipeableViews
                    axis={theme.direction === 'rtl' ? 'x-reverse' : 'x'}
                    index={value}
                    onChangeIndex={handleChangeIndex}
                    disabled={modifyingColor}
                  >
                    <TabPanel value={value} index={0} dir={theme.direction}>
                      <ColorWheel setModifyingColor={setModifyingColor}/>
                    </TabPanel>
                    <TabPanel value={value} index={1} dir={theme.direction}>
                      <ColorPicker setModifyingColor={setModifyingColor}/>
                    </TabPanel>
                  </SwipeableViews>
                </div>
              </Grid>
            </Grid>
        </Box>
    );
};

export default ColorSelectionTab;