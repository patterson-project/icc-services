import { BottomNavigation, BottomNavigationAction, Box } from "@mui/material";
import React, { FC, useState } from "react";
import ColorLensIcon from "@mui/icons-material/ColorLens";
import PowerSettingsNewIcon from "@mui/icons-material/PowerSettingsNew";
import AllInclusiveIcon from "@mui/icons-material/AllInclusive";
import ColorDialog from "../Components/LightingPageComponents/Dialogs/ColorDialog";
import SceneDialog from "../Components/LightingPageComponents/Dialogs/SceneDialog";
import PowerDialog from "../Components/LightingPageComponents/Dialogs/PowerDialog";

const lightingPageBoxStyle = {
  marginBottom: "30px",
};

const bottomNavigationStyle = {
  backgroundColor: "#222222",
};

const bottomNavigationLabelStyle = {
  fontFamily: "Ubuntu, -apple-system",
  fontSize: "16px",
};

const iconStyle = {
  color: "white",
  fontSize: "large",
};

const LightingPage: FC = () => {
  const [value, setValue] = useState<number>(0);
  const lightingComponents = [
    <ColorDialog />,
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
          label={getBottomNavigationLabelSpan("Scenes")}
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
