import React, { FC } from "react";
import Button from "@mui/material/Button";

interface OperationButtonProps {
  operationName: string;
  onClick(): void;
  icon: JSX.Element;
}

const buttonStyle = {
  fontFamily: "Ubuntu, -apple-system",
  fontSize: "16px",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  width: "90%",
  height: "50px",
  borderRadius: "10px",
  backgroundColor: "#3B3B3B",
};

const OperationButton: FC<OperationButtonProps> = (props): JSX.Element => {
  return (
    <Button
      style={buttonStyle}
      variant="outlined"
      startIcon={props.icon}
      onClick={props.onClick}
    >
      {props.operationName}
    </Button>
  );
};

export default OperationButton;
