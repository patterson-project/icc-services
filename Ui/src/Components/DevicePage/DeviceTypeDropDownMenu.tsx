import React, { FC, useEffect } from "react";
import TextField from "@mui/material/TextField";

const deviceTypes = [
  {
    value: "lighting",
    label: "Lighting",
  },
];

interface IDeviceTypeDropDownMenu {
  id: string;
  label: string;
  type: string;
  setType: (type: string) => void;
}

const DeviceTypeDropDownMenu: FC<IDeviceTypeDropDownMenu> = (props) => {
  useEffect(() => {
    props.setType(deviceTypes[0].label);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    props.setType(event.target.value);
  };

  return (
    <div style={{ width: "100%" }}>
      <TextField
        id={props.id}
        select
        label={props.label}
        value={props.type}
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
