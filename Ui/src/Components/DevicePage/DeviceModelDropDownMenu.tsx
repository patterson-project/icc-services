import React, { FC, useEffect, useState } from "react";
import TextField from "@mui/material/TextField";
import { useDidMountEffect } from "../../utils";
import { drop } from "lodash";

interface DeviceModel {
  value: string;
  label: string;
}

const lightingDeviceModels: DeviceModel[] = [
  {
    value: "Kasa Bulb",
    label: "Kasa Bulb",
  },
  {
    value: "Custom Led Strip",
    label: "Custom Led Strip",
  },
  {
    value: "Kasa Led Strip",
    label: "Kasa Led Strip",
  },
];

const powerDeviceModels: DeviceModel[] = [
  {
    value: "Kasa Plug",
    label: "Kasa Plug",
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
    console.log(props.type);
    if (props.type === "Lighting") {
      setDropDownList(lightingDeviceModels);
    } else if (props.type === "Power") {
      setDropDownList(powerDeviceModels);
    } else {
      setDropDownList(null);
    }
  }, [props.type]);

  useEffect(() => {
    if (dropDownList) {
      props.setModel(dropDownList[0].value);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [dropDownList]);

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
