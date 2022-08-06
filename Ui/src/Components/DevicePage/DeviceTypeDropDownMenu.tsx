import React, { FC, useEffect, useState } from "react";
import TextField from "@mui/material/TextField";
import { MenuItem } from "@mui/material";

interface DeviceTypes {
  value: string;
  label: string;
}

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

interface IDeviceTypeDropDownMenu {
  id: string;
  label: string;
  setType: (type: string) => void;
}

const DeviceTypeDropDownMenu: FC<IDeviceTypeDropDownMenu> = (props) => {
  const [deviceType, setType] = useState<string>();

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setType(event.target.value);
    props.setType(event.target.value);
  };

  return (
    <div style={{ width: "100%" }}>
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
          shrink: true,
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
        {deviceTypes?.map((type) => (
          <option value={type.value}>{type.label}</option>
        ))}
      </TextField>
    </div>
  );
};

export default DeviceTypeDropDownMenu;
