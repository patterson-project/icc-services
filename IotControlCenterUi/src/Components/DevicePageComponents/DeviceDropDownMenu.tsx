import React, { FC, useState } from "react";
import TextField from "@mui/material/TextField";

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
}

const DeviceDropDownMenu: FC<IDeviceDropDownMenu> = (props) => {
  const [deviceType, setType] = useState("");
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setType(event.target.value);
  };

  return (
    <div>
      <TextField
        id={props.id}
        select
        label={props.label}
        value={deviceType}
        variant={"filled"}
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
        onChange={handleChange}
        SelectProps={{
          native: true,
        }}
      >
        {deviceTypes.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </TextField>
    </div>
  );
};

export default DeviceDropDownMenu;
