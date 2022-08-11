import React, { FC } from "react";
import Button from "@mui/material/Button";

interface IOperationButton {
  operationName: string;
  onClick(): void;
  color?: string;
  image?: string;
}

const OperationButton: FC<IOperationButton> = (props): JSX.Element => {
  const buttonStyle = {
    fontFamily: "Ubuntu, -apple-system",
    fontWeight: "medium",
    fontSize: "16px",
    color: "white",
    display: "flex",
    alignItems: "flex-start",
    justifyContent: "left",
    width: "85%",
    height: "80px",
    borderRadius: "10px",
    backgroundColor: props.color,
    backgroundImage: props.image,
  };

  return (
    <Button style={buttonStyle} variant="text" onClick={props.onClick}>
      {props.operationName}
    </Button>
  );
};

export default OperationButton;
