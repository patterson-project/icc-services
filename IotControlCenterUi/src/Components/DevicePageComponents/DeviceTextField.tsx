import { TextField } from "@mui/material";
import React, { Dispatch, FC, SetStateAction } from "react";

interface IDeviceTextField {
  id: string;
  label: string;
  setText: Dispatch<SetStateAction<string>>;
}

const inputLabelPropsStyle = {
  color: "white",
  fontSize: "15px",
  fontFamily: "Ubuntu, -apple-system",
};

const DeviceTextField: FC<IDeviceTextField> = (props) => {
  return (
    <TextField
      onChange={(event) => props.setText(event.target.value)}
      autoFocus
      margin="dense"
      id={props.id}
      label={props.label}
      InputProps={{
        style: inputLabelPropsStyle,
      }}
      InputLabelProps={{
        style: inputLabelPropsStyle,
      }}
      fullWidth
      variant="filled"
    />
  );
};

export default DeviceTextField;
