import React, { FC } from "react";
import IccAppBar from "../Common/IccAppBar";

const homePageDivStyle = {
  height: "100%",
  margin: "0px",
  minHeight: "100vh",
  backgroundColor: "#151515",
};

const HomePage: FC = () => {
  return (
    <div style={homePageDivStyle}>
      <IccAppBar />
    </div>
  );
};

export default HomePage;
