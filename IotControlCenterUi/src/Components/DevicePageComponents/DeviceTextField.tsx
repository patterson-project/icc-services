import { TextField } from "@mui/material";
import React, { Dispatch, FC, SetStateAction } from "react";

interface IDeviceTextField {
  id: string;
  label: string;
  setText: Dispatch<SetStateAction<string>>;
}

const DeviceTextField: FC<IDeviceTextField> = (props) => {
  return (
    <TextField
      onChange={(event) => props.setText(event.target.value)}
      autoFocus
      margin="dense"
      id={props.id}
      label={props.label}
      InputProps={{
        style: {
          color: "white",
          fontSize: "15px",
          fontFamily: "Ubuntu, -apple-system",
        },
      }}
      InputLabelProps={{
        style: {
          color: "white",
          fontSize: "15px",
          fontFamily: "Ubuntu, -apple-system",
        },
      }}
      fullWidth
      variant="filled"
    />
  );
};

export default DeviceTextField;
