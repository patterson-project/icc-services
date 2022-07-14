import React, {
  ChangeEvent,
  Dispatch,
  FC,
  SetStateAction,
  useState,
} from "react";
import TextField from "@mui/material/TextField";
import MenuItem from "@mui/material/MenuItem";

const deviceTypes = [
  {
    value: "lighting",
    label: "Lighting",
  },
  {
    value: "plug",
    label: "Plug",
  },
  {
    value: "switch",
    label: "Switch",
  },
];

interface IDeviceDropDownMenu {
  id: string;
  label: string;
  setType: Dispatch<SetStateAction<string>>;
}

const DeviceDropDownMenu: FC<IDeviceDropDownMenu> = (props) => {
  const [deviceType, setDeviceType] = useState("");

  return (
    <div>
      <TextField
        id={props.id}
        select
        label={props.label}
        value={deviceType}
        fullWidth
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
        onChange={(event) => props.setType(event.target.value)}
        SelectProps={{
          native: true,
        }}
      >
        {deviceTypes.map((option) => (
          <MenuItem key={option.value} value={option.value}>
            {option.label}
          </MenuItem>
        ))}
      </TextField>
    </div>
  );
};

export default DeviceDropDownMenu;
