import React, { FC, forwardRef, useState } from "react";
import {
  Button,
  createTheme,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  Slide,
  ThemeProvider,
} from "@mui/material";
import Fab from "@mui/material/Fab";
import AddIcon from "@mui/icons-material/Add";
import TextField from "@mui/material/TextField";
import { TransitionProps } from "@mui/material/transitions";
import DeviceTextField from "./DeviceTextField";

const modalDivStyle = {
  height: "100%",
  margin: "0px",
  minHeight: "100vh",
  backgroundColor: "#151515",
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

const AddDeviceModal: FC = () => {
  const [open, setOpen] = useState<boolean>(false);
  const [name, setName] = useState<string>("");
  const [ip, setIp] = useState<string>("");
  const [model, setModel] = useState<string>("");
  const [type, setType] = useState<string>("");
  //type needs to be a drop
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

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
          onClose={handleClose}
          TransitionComponent={Transition}
        >
          <DialogTitle>Add a Device</DialogTitle>
          <DialogContent>
            <DialogContentText sx={{ color: "text.primary" }}>
              Fill in the following information to add a device.
            </DialogContentText>
            <DeviceTextField id="name" label="Device Name" setText={setName} />
            <DeviceTextField id="ip" label="Device IP" setText={setIp} />
            <DeviceTextField
              id="model"
              label="Device Model"
              setText={setModel}
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={handleClose}>Cancel</Button>
            <Button onClick={handleClose}>Add</Button>
          </DialogActions>
        </Dialog>
      </ThemeProvider>
    </div>
  );
};

//change button

export default AddDeviceModal;
