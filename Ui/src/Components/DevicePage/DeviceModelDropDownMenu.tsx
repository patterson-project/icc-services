import React, { FC, useEffect, useState } from "react";
import TextField from "@mui/material/TextField";
import { useDidMountEffect } from "../../utils";

interface DeviceModel {
  value: string;
  label: string;
}

const lightingDeviceModels: DeviceModel[] = [
  {
    value: "kasa-bulb",
    label: "Kasa Bulb",
  },
  {
    value: "custom-led-strip",
    label: "Custom Led Strip",
  },
  {
    value: "kasa-led-strip",
    label: "Kasa Led Strip",
  },
];

interface IDeviceModelDropDownMenu {
  id: string;
  label: string;
  type: string;
  model: string;
  setModel: (model: string) => void;
}

const DeviceModelDropDownMenu: FC<IDeviceModelDropDownMenu> = (props) => {
  const [dropDownList, setDropDownList] = useState<DeviceModel[] | null>(
    lightingDeviceModels
  );

  useDidMountEffect(() => {
    if (props.type === "Lighting") {
      setDropDownList(lightingDeviceModels);
    } else {
      setDropDownList(null);
    }
  }, [props.type]);

  useEffect(() => {
    props.setModel(lightingDeviceModels[0].label);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    props.setModel(event.target.value);
  };

  return (
    <div style={{ width: "100%" }}>
      <TextField
        id={props.id}
        select
        label={props.label}
        value={props.model}
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
