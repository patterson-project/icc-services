import React, { FC, forwardRef, useState } from "react";
import {
  createTheme,
  Dialog,
  DialogActions,
  Grid,
  IconButton,
  Slide,
  ThemeProvider,
  Typography,
} from "@mui/material";
import Fab from "@mui/material/Fab";
import AddIcon from "@mui/icons-material/Add";
import CheckIcon from "@mui/icons-material/Check";
import { TransitionProps } from "@mui/material/transitions";
import DeviceTextField from "./DeviceTextField";
import DeviceTypeDropDownMenu from "./DeviceTypeDropDownMenu";
import CloseIcon from "@mui/icons-material/Close";
import { gridContainerStyle } from "../../Styles/CommonStyles";
import DeviceModelDropDownMenu from "./DeviceModelDropDownMenu";
import { post } from "../../utils";
import config from "../../config";
import { AddDeviceDto, Device } from "../../types";

interface IAddDeviceModal {
  devices: Device[];
  setDevices: (devices: Device[]) => void;
}

const modalDivStyle = {
  height: "100%",
  margin: "0px",
  minHeight: "100vh",
  backgroundColor: "#151515",
};

const dialogGridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  paddingRight: "20px",
  paddingLeft: "20px",
};

const dialogTitleGridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "start",
  paddingRight: "20px",
  paddingLeft: "20px",
};

const iconGridItemStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "end",
};

const iconStyle = {
  color: "white",
};

const dialogTitleStyle = {
  color: "white",
  fontSize: "20px",
  fontFamily: "Ubuntu, -apple-system",
  fontWeight: "bold",
};

const dialogContentStyle = {
  color: "white",
  fontSize: "15px",
  fontFamily: "Ubuntu, -apple-system",
  fontWeight: "light",
};

const backgroundTheme = createTheme({
  palette: {
    background: {
      paper: "#2C2C2E",
    },
    text: {
      primary: "#FFFFFF",
    },
  },
});

const Transition = forwardRef(function Transition(
  props: TransitionProps & {
    children: React.ReactElement<any, any>;
  },
  ref: React.Ref<unknown>
) {
  return <Slide direction="up" ref={ref} {...props} />;
});

const addDeviceButton = {
  position: "fixed",
  bottom: 16,
  right: 16,
};

const AddDeviceModal: FC<IAddDeviceModal> = (props) => {
  const [open, setOpen] = useState<boolean>(false);
  const [name, setName] = useState<string>("");
  const [ip, setIp] = useState<string>("");
  const [model, setModel] = useState<string>("");
  const [type, setType] = useState<string>("");

  const handleOpen = () => setOpen(true);
  const handleSave = () => {
    const device: AddDeviceDto = {
      name: name,
      type: type,
      model: model,
      ip: ip,
    };

    fetch(config.DEVICE_MANAGER_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(device),
    })
      .then((response) => {
        if (!response.ok) {
          console.log(`Failed to create device: ${response.statusText}`);
        } else {
          return response.json();
        }
      })
      .then((data) => {
        const newDevices = props.devices.concat(data.data as Device);
        props.setDevices(newDevices);
      });
    setOpen(false);
  };

  return (
    <div style={modalDivStyle}>
      <Fab
        color="primary"
        aria-label="add"
        sx={addDeviceButton}
        onClick={handleOpen}
      >
        <AddIcon />
      </Fab>
      <ThemeProvider theme={backgroundTheme}>
        <Dialog
          sx={{ bgcolor: "background.paper" }}
          open={open}
          onClose={handleSave}
          TransitionComponent={Transition}
        >
          <Grid container spacing={1} style={gridContainerStyle}>
            <Grid item xs={10} style={dialogTitleGridItemStyle}>
              <Typography style={dialogTitleStyle}>Add a Device</Typography>
            </Grid>
            <Grid item xs={2} style={iconGridItemStyle}>
              <IconButton size="large" onClick={handleSave}>
                <CloseIcon style={iconStyle} />
              </IconButton>
            </Grid>
            <Grid item xs={12} style={dialogGridItemStyle}>
              <Typography style={dialogContentStyle}>
                Fill in the following information to add a device
              </Typography>
            </Grid>
            <Grid item xs={12} style={dialogGridItemStyle}>
              <DeviceTypeDropDownMenu
                id="type-drop-down"
                label="Device Type"
                type={type}
                setType={setType}
              />
            </Grid>
            <Grid item xs={12} style={dialogGridItemStyle}>
              <DeviceModelDropDownMenu
                id="model-drop-down"
                label="Device Model"
                type={type}
                model={model}
                setModel={setModel}
              />
            </Grid>
            <Grid item xs={12} style={dialogGridItemStyle}>
              <DeviceTextField
                id="name"
                label="Device Name"
                setText={setName}
              />
            </Grid>
            <Grid item xs={12} style={dialogGridItemStyle}>
              <DeviceTextField id="ip" label="Device IP" setText={setIp} />
            </Grid>
          </Grid>
          <DialogActions>
            <IconButton size="large" onClick={handleSave}>
              <CheckIcon style={iconStyle} />
            </IconButton>
          </DialogActions>
        </Dialog>
      </ThemeProvider>
    </div>
  );
};

//change button

export default AddDeviceModal;
