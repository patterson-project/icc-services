import { BottomNavigation, BottomNavigationAction, Box } from "@mui/material";
import React, { FC, useEffect, useState } from "react";
import ColorLensIcon from "@mui/icons-material/ColorLens";
import PowerSettingsNewIcon from "@mui/icons-material/PowerSettingsNew";
import AllInclusiveIcon from "@mui/icons-material/AllInclusive";
import ColorDialog from "./Dialogs/ColorDialog/ColorDialog";
import SceneDialog from "./Dialogs/SceneDialog/SceneDialog";
import PowerDialog from "./Dialogs/PowerDialog/PowerDialog";
import IccAppBar from "../Common/IccAppBar";
import { Device } from "../../types";
import config from "../../config";

const lightingPageBoxStyle = {
  marginBottom: "50px",
};

const bottomNavigationStyle = {
  backgroundColor: "#222222",
  paddingBottom: "20px",
};

const bottomNavigationLabelStyle = {
  fontFamily: "Ubuntu, -apple-system",
  fontSize: "16px",
};

const iconStyle = {
  color: "white",
  size: "large",
};

const LightingPage: FC = () => {
  const [value, setValue] = useState<number>(0);
  const [devices, setDevices] = useState<Device[]>([]);

  useEffect(() => {
    fetch(config.DEVICE_MANAGER_ENDPOINT, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((data) => {
        setDevices(data as Device[]);
      });
  }, []);

  const lightingComponents = [
    <ColorDialog devices={devices} />,
    <SceneDialog />,
    <PowerDialog />,
  ];

  const handleBottomNavigationChange = (
    _event: React.SyntheticEvent,
    newValue: number
  ) => {
    setValue(newValue);
  };

  const getBottomNavigationLabelSpan = (label: string) => {
    return <span style={bottomNavigationLabelStyle}>{label}</span>;
  };

  return (
    <Box style={lightingPageBoxStyle}>
      <IccAppBar />
      {lightingComponents[value]}
      <BottomNavigation
        style={bottomNavigationStyle}
        sx={{ position: "fixed", bottom: 0, width: 1.0 }}
        value={value}
        onChange={handleBottomNavigationChange}
      >
        <BottomNavigationAction
          label={getBottomNavigationLabelSpan("Colors")}
          value={0}
          icon={<ColorLensIcon style={iconStyle} />}
        />
        <BottomNavigationAction
          label={getBottomNavigationLabelSpan("Environments")}
          value={1}
          icon={<AllInclusiveIcon style={iconStyle} />}
        />
        <BottomNavigationAction
          label={getBottomNavigationLabelSpan("Power")}
          value={2}
          icon={<PowerSettingsNewIcon style={iconStyle} />}
        />
      </BottomNavigation>
    </Box>
  );
};

export default LightingPage;
