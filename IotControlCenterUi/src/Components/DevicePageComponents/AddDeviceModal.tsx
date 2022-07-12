import React, { FC } from "react";
import { Box, Grid, Modal, Typography } from "@mui/material";
import Fab from "@mui/material/Fab";
import AddIcon from "@mui/icons-material/Add";
import TextField from "@mui/material/TextField";
import { gridContainerStyle, gridItemStyle } from "../../Styles/DialogStyles";

const modalDivStyle = {
  height: "100%",
  margin: "0px",
  minHeight: "100vh",
  backgroundColor: "#151515",
};

const modalBoxStyle = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  boxShadow: 24,
  width: "90%",
  bgcolor: "#2C2C2E",
  p: 16,
};

const addDeviceButton = {
  position: "fixed",
  bottom: 16,
  right: 16,
};

const floatingLabelFocusStyle = {
  color: "white",
};

const addDevicePageStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  height: "100%",
  width: "90%",
  borderRadius: "10px",
  paddingBottom: "10px",
  overflow: "auto",
};

const AddDeviceModal: FC = () => {
  const [open, setOpen] = React.useState(false);
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
      <Modal open={open} onClose={handleClose}>
        <Box sx={modalBoxStyle}>
          <Grid container style={gridContainerStyle}>
            <Grid item style={gridItemStyle} xs={12}>
              <TextField fullWidth label="Device Name" variant="standard" />
            </Grid>
          </Grid>
        </Box>
      </Modal>
    </div>
  );
};

export default AddDeviceModal;
