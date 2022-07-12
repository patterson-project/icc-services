import {
  AppBar,
  Box,
  Divider,
  IconButton,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  SwipeableDrawer,
  Toolbar,
  Typography,
} from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import React, { FC, useState } from "react";
import HomeIcon from "@mui/icons-material/Home";
import LightbulbIcon from "@mui/icons-material/Lightbulb";
import DevicesIcon from "@mui/icons-material/Devices";
import { useNavigate } from "react-router-dom";

const appBarTitleStyle = {
  color: "white",
  fontFamily: "Ubuntu, -apple-system",
  fontSize: "16px",
};

const appBarStyle = {
  backgroundColor: "#222222",
};

const listItemTextStyle = {
  color: "white",
  fontFamily: "Ubuntu, -apple-system",
  fontSize: "16px",
};

const iconStyle = {
  color: "white",
};

const IccAppBar: FC = () => {
  const [drawerOpen, setDrawerOpen] = useState<boolean>(false);
  let navigate = useNavigate();

  const toggleDrawer =
    (open: boolean) => (event: React.KeyboardEvent | React.MouseEvent) => {
      if (
        event &&
        event.type === "keydown" &&
        ((event as React.KeyboardEvent).key === "Tab" ||
          (event as React.KeyboardEvent).key === "Shift")
      ) {
        return;
      }

      setDrawerOpen(open);
    };

  const getListItemTextSpan = (listItemText: string) => {
    return <span style={listItemTextStyle}>{listItemText}</span>;
  };

  const list = () => (
    <Box
      sx={{ width: "auto" }}
      role="presentation"
      onClick={toggleDrawer(false)}
      onKeyDown={toggleDrawer(false)}
    >
      <List>
        <ListItem button onClick={() => navigate("/home")}>
          <ListItemIcon>
            <HomeIcon style={iconStyle} />
          </ListItemIcon>
          <ListItemText primary={getListItemTextSpan("Home")} />
        </ListItem>
        <ListItem button onClick={() => navigate("/")}>
          <ListItemIcon>
            <LightbulbIcon style={iconStyle} />
          </ListItemIcon>
          <ListItemText primary={getListItemTextSpan("Lighting")} />
        </ListItem>
        <ListItem button onClick={() => navigate("/device")}>
          <ListItemIcon>
            <DevicesIcon style={iconStyle} />
          </ListItemIcon>
          <ListItemText primary={getListItemTextSpan("Devices")} />
        </ListItem>
      </List>
      <Divider />
    </Box>
  );

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar style={appBarStyle} position="static">
        <Toolbar>
          <IconButton color="inherit" onClick={toggleDrawer(true)}>
            <MenuIcon />
          </IconButton>
          <Typography
            style={appBarTitleStyle}
            variant="h6"
            component="div"
            sx={{ flexGrow: 1 }}
          >
            IoT Control Center
          </Typography>
        </Toolbar>
        <SwipeableDrawer
          PaperProps={{
            sx: {
              backgroundColor: "#181818",
            },
          }}
          anchor="top"
          open={drawerOpen}
          onClose={toggleDrawer(false)}
          onOpen={toggleDrawer(true)}
        >
          {list()}
        </SwipeableDrawer>
      </AppBar>
    </Box>
  );
};

export default IccAppBar;
