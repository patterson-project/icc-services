import React, { FC } from "react";
import IccAppBar from "../Components/IccAppBar";

const devicePageDivStyle = {
  height: "100%",
  margin: "0px",
  minHeight: "100vh",
  backgroundColor: "#151515",
};

const DevicePage: FC = () => {
  return (
    <div style={devicePageDivStyle}>
      <IccAppBar />
    </div>
  );
};

export default DevicePage;
