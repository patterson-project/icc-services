import React, { FC, useEffect, useState } from "react";
import TextField from "@mui/material/TextField";
import { MenuItem } from "@mui/material";

interface DeviceModel {
  value: string;
  label: string;
}

const lightingDeviceModels: DeviceModel[] = [
  {
    value: "kasa-kl-215",
    label: "Kasa KL-215",
  },
];

interface IDeviceModelDropDownMenu {
  id: string;
  label: string;
  deviceType: string;
  setModel: (model: string) => void;
}

const DeviceModelDropDownMenu: FC<IDeviceModelDropDownMenu> = (props) => {
  const [deviceModel, setModel] = useState<string>();
  const [dropDownList, setDropDownList] = useState<DeviceModel[] | null>();

  useEffect(() => {
    if (props.deviceType === "lighting") {
      setDropDownList(lightingDeviceModels);
    } else {
      setDropDownList(null);
    }
  }, [props.deviceType]);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setModel(event.target.value);
    props.setModel(event.target.value);
  };

  return (
    <div style={{ width: "100%" }}>
      <TextField
        id={props.id}
        select
        label={props.label}
        value={deviceModel}
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
        {dropDownList?.map((option) => (
          <option value={option.value}>{option.label}</option>
        ))}
      </TextField>
    </div>
  );
};

export default DeviceModelDropDownMenu;
